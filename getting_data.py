import requests
from bs4 import BeautifulSoup, Comment
import os
import csv


html = """
<html>
<head>
<!-- Head comment -->
<title>Test Page</title>
</head>
<body>
<p>Hello World</p>
<!-- Body comment -->
</body>
</html>
"""

response=requests.get("https://www.flipkart.com/")
responsedata=response.content

if response.status_code==200:
    soup=BeautifulSoup(html,"html.parser")
    
    
    data=soup.prettify()
    count=1
    
    """ # TAGS
    tag=soup.find_all('link')
    for link in tag:
        
        print("link",count,":",link)
        count=count+1 """
    
    # Navigating to a string
    """ navstr=soup.find_all('link')
    with open("data.txt", 'a', newline='') as file:
        for link in navstr:
            data=link.get("href")
            print(count,data)
            pre_save_data=(count,data)
            save_data=str(pre_save_data)
            file.write(f"{save_data} \n")
            count+=1   """ 
    



    """ tags=soup.find_all('link')
    with open("data.csv" , 'w',newline='',encoding='utf-8') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(["S.No","Link"])
        for i , link in enumerate(tags,start=1):
            href=link.get("href")
            if href:
                writer.writerow([i,href]) """





    #Beautiful Soup
    
    """ print(soup.h1.string) """
    # use methods like find , find_all etc 


    #comments
    comments=soup.find_all(string=lambda text: isinstance(text,Comment))
    for c in comments:
        print(c)
