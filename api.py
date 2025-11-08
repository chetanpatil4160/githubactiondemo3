import requests
import pandas as pd 
import os

token=os.getenv("API_TOEKN")

#response = requests.get("https://jsonplaceholder.typicode.com/users")
#data = response.json()
#df = pd.DataFrame(data)
#df = df[["id","name"]] # getting only id name from data 
#print(df)

print(f"Token : {token}")