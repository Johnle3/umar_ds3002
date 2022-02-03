#1.	Write a query to get Product name and quantity/unit.  
SELECT northwind.products.product_name, quantity_per_unit 
FROM northwind.products;

#2. Write a query to get current Product list (Product ID and name).
SELECT northwind.products.id, product_name 
FROM northwind.products;

#3. Write a query to get discontinued Product list (Product ID and name). 
#Note: I guess there are no products listed as discontinued?
SELECT northwind.products.id, product_name 
FROM northwind.products 
WHERE discontinued=1;

#4. Write a query to get most expense and least expensive Product list (name and unit price).  
SELECT northwind.products.product_name, list_price FROM northwind.products WHERE list_price in (SELECT MAX(list_price)
FROM products) or list_price in(Select MIN(list_price) FROM products);
 
#5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.
SELECT northwind.products.id, product_name, list_price 
FROM products
WHERE list_price < 20
ORDER BY list_price DESC;
   
#6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
SELECT northwind.products.id, product_name, list_price 
FROM products
WHERE list_price >= 15 and list_price <= 25
AND discontinued = False
ORDER BY list_price DESC;
   
#7. Write a query to get Product list (name, unit price) of above average price.  
SELECT northwind.products.product_name, list_price
FROM products
WHERE list_price > (Select avg(list_price) FROM products)
ORDER BY list_price DESC;

#8. Write a query to get Product list (name, unit price) of ten most expensive products. 
SELECT product_name, list_price 
FROM products 
ORDER BY list_price DESC 
LIMIT 10;
 
#9. Write a query to count current and discontinued products. 
SELECT Count(product_name)
FROM products
GROUP BY discontinued;

#10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  
SELECT product_name, reorder_level as units_in_stock, target_level as units_on_order
FROM products
WHERE reorder_level < target_level
ORDER BY units_in_stock DESC;
