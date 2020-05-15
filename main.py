from plyer import notification 
import pip._vendor.requests as requests
from bs4 import BeautifulSoup
from time import sleep



def getData(url):
    r=requests.get(url)
    return r.text

def notifyMe(title, message):
    notification.notify(
        title=title, 
        message= message,
        app_icon= "E:\Websites\Python Projects\Covid-19 Notification System\icon.ico",
        timeout=15
    )

if __name__ == "__main__":

    while (True):
       myHtmlData= getData("https://www.mohfw.gov.in/")
       notifyMe("Covid-19 Updates", "Notification working")
       soup = BeautifulSoup(myHtmlData, 'html.parser')
       myDataStr=""
       #print(soup.prettify)
       for tr in soup.find_all('tbody')[0].find_all('tr'):
            #print(tr.getText())
            myDataStr+=tr.getText()
    
       myDataStr=myDataStr[1:]
       states=["Bihar","Delhi","West Bengal"]
       itemList=myDataStr.split("\n\n")
        #print(itemList)
       for item in itemList[0:33]:
            dataList=item.split("\n")
            print(dataList)
            if dataList[1] in states:
                nTitle="Cases of Covid-19"
                nText="State : "+dataList[1]+"\nTotal Confirmed cases* : "+dataList[2]+"\n Cured/Discharged/Migrated : "+dataList[3]+"\n Deaths : "+dataList[4]
                notifyMe(nTitle, nText)
                sleep(2)
       sleep(3600)
