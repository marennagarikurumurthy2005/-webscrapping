import requests
from bs4 import BeautifulSoup


response=requests.get("https://www.flipkart.com/")

if response.status_code==200:
    print("Success")
    







