access_token="1522410951143796737-YYWsI2DTjEcQS7cQxSi60kGQus22PO"
access_token_secret="JUMUXpFg9RaDHI3kROXf71WkhhDHzSuX3mKpVaMaEwfEf"
API_key="3uMQe1YQtlpZbYwzT3jCV4nvn"
API_secret_key="H5uDWYWzsU4QV5DMu6iPgS1RtTxavaDmKzn0059nUiqwcA0X0m"


import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("3uMQe1YQtlpZbYwzT3jCV4nvn", "H5uDWYWzsU4QV5DMu6iPgS1RtTxavaDmKzn0059nUiqwcA0X0m")
auth.set_access_token("1522410951143796737-YYWsI2DTjEcQS7cQxSi60kGQus22PO", "JUMUXpFg9RaDHI3kROXf71WkhhDHzSuX3mKpVaMaEwfEf")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")

    #AAAAAAAAAAAAAAAAAAAAAHUacQEAAAAAmv6tqi6o6Y30%2FPY2K%2BCir9QILhk%3DRKUEPCWUObeZ3zB667q1j767RlFpsM96JOqI7jRROmZqREJwMR


    #Client ID: U1BGMS0zZjhpQ1E3ZnVhb09CdVQ6MTpjaQ
    #Client Secret: 4OBAK11qycimgBBvvIXSxkg2RDlyvRTpgmZjsFHwQs76YzN3M1
