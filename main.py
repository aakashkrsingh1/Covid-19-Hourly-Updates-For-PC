from plyer import notification 

def notifyMe(title, message):
    notification.notify(
        title=title, 
        message= message,
        app_icon= "E:\Websites\Python Projects\Covid-19 Notification System\icon.ico",
        timeout=5
    )

if __name__ == "__main__":
    notifyMe("Covid-19 Updates", "Notification working")

