import time
from pyler import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Its time to drink water!!",
            message = "Water makes up approximately 70% of a human's body weight – but DON'T stop drinking water "
                      "to lose weight! Approximately 80% of your brain tissue is made of water ",
            app_icon = r"C:\Users\\rishi\OneDrive\Desktop\water\\drink-water.ico",
            timeout = 15

        )
        time.sleep(60*60)
