import requests
from bs4 import BeautifulSoup


response=requests.get("https://www.flipkart.com/")
responsedata=response.content

if response.status_code==200:
    soup=BeautifulSoup(responsedata,"html.parser")
    
    
    data=soup.prettify()
    count=1
    
    # TAGS
    tag=soup.find_all('link')
    for link in tag:
        
        print("link",count,":",link)
        count=count+1
        






