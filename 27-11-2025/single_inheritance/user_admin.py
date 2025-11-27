class User:
    def __init__(self,name,mail):
        self.name = name
        self.mail = mail
class Admin(User):
    def __init__(self,name,mail,is_admin):
        super().__init__(name,mail)
        self.is_admin = is_admin
u1=Admin("Shone","mail@mail.com",True)
print(u1.name)
print(u1.mail)
print(u1.is_admin)