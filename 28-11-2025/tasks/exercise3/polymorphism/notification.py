class Notification:
    def send(self, message):
        print("sending notification:",message)
class EmailNotification(Notification):
    def send(self, message):
        print("send email to user:", message)
class SMSNotification(Notification):
    def send(self, message):
        print("send sms:", message)

n1=EmailNotification()
n1.send("your order is confirmed")
n2=SMSNotification()
n2.send("your otp is 4589")
