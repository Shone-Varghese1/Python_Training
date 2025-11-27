class NotificationDevice:
    def show_notification(self):
        print("Notification POP UP ******")
class HealthDevice():
    def monitor_heartrate(self):
        print("Heartrate is ###")
class SmartWatch(NotificationDevice,HealthDevice):
    def about_device(self):
        print("device details")


s1=SmartWatch()
s1.show_notification()
s1.monitor_heartrate()
s1.about_device()