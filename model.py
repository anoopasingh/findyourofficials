import requests #API access
import os #access 
google_API_key = os.getenv("GOOGLE_API_KEY") #.env file, write code into app.py, to bring in the secret .env, get environemnt vbls 


def access_API(address): #get response from API
    api_endpoint = "https://www.googleapis.com/civicinfo/v2/representatives"
    address_query = f"&address={address}" #& queries, concat nto url
    api_key = f"?key={google_API_key}" #add into line 6, first thing
    api_url = api_endpoint + api_key + address_query
    print(api_url)
    response = requests.get(api_url).json()
    return response

#access_API("2983 Marion Ave")
