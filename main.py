from plyer import notification 
import pip._vendor.requests as requests
from bs4 import BeautifulSoup


def getData(url):
    r=requests.get(url)
    return r.text

def notifyMe(title, message):
    notification.notify(
        title=title, 
        message= message,
        app_icon= "E:\Websites\Python Projects\Covid-19 Notification System\icon.ico",
        timeout=5
    )

if __name__ == "__main__":


    myHtmlData= getData("https://www.mohfw.gov.in/")
    notifyMe("Covid-19 Updates", "Notification working")
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    print(soup)
    

