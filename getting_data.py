import requests
from bs4 import BeautifulSoup, Comment
import os
import csv


response = requests.get("https://www.flipkart.com/search?q=mobiles+under+10000+rupees&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+10000+rupees%7CMobiles&requestId=df637841-dfe8-44a3-b94e-e0dfdac8415f&as-searchtext=mobiles%20under%2010000%20rupees")
responsedata = response.content




  # prints response status (e.g., <Response [200]>)

if response.status_code == 200:
    
    soup = BeautifulSoup(responsedata, "html.parser")
    box=soup.find_all("div",class_="DOjaWF gdgoEp")
    print(box)





    
    """ data = soup.prettify()
    count = 1
    img_data=soup.find_all('img')
    for i in img_data:
        print(f"{i.get('src')}\n")

else:
    print("Failed to fetch page. Status code:", response.status_code)

 """

    """ response=requests.get("http://www.instagram.com/sindhuri03/?_pwa=1")
    responsedata=response.content

    print(response)

    if response.status_code==200:
        soup=BeautifulSoup(response,"html.parser")
        
        
        data=soup.prettify()
        count=1 """
    
    
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
    """ comments=soup.find_all(string=lambda text: isinstance(text,Comment))
    for c in comments:
        print(c) """


#Finding elemenmts