import requests as req
import time 
from seleniumwire import webdriver
import cfscrape  #anti cloudflare hack




def get_cookies(browser):
    cookies = {}
    selenium_cookies = browser.get_cookies()
    for cookie in selenium_cookies:
        cookies[cookie['name']] = cookie['value']
    return cookies

def getTime():
    return round(time.time()*1000)

driver = webdriver.Chrome()

driver.get("https://www.invokergame.com/")
session = cfscrape.create_scraper(req.session())



input("Press Enter after save request.")
for x in driver.requests:
    if(x.url.split("/")[2] =="www.invokergame.com"):
        print(x.url)
    if(x.url.split("/")[2] =="www.invokergame.com" and x.url.split("/")[3] == "a" and x.url.split("/")[4].split("?")[0] != "ajax.ashx"):
        exampleReq = x
        break



session.headers.update(exampleReq.headers)
print(exampleReq.url)
print(exampleReq.headers)
print(driver.get_cookies())
print(session.headers)
print(session.cookies)
print(getTime())

timik = getTime()
finallUrl = exampleReq.url.split("?")[0] + "?a=1&b=Classic&c=0&d=" + str(timik) +"&e=" + str(timik) +"&f=41&g=10&h=0&H0=M&H1=Z&H2=T&H3=A&H4=G&H5=Z&H6=Q&H7=P&H8=O&H9=R"
response = session.get(finallUrl, cookies=get_cookies(driver))
print(finallUrl)
print(response.text)
print(response.content)
print(response.status_code)
input()

