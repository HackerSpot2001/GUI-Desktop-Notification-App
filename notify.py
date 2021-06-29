#!/usr/bin/python3
import notify2 
import time

notify2.init("Health Notifier...")
notification_object = notify2.Notification(None)
notification_object.set_urgency(notify2.URGENCY_CRITICAL)
# notification_object.set_timeout(5000)

while True:
    notification_object.update("Break Time.....","Go and Fresh-up yuor face and eyes..")
    notification_object.show()
    time.sleep(5)  
    notification_object.close()
    time.sleep(1200)  
