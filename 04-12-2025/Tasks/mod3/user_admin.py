# 23. Create a User class and an Admin subclass that can delete a user (override methods).
class User:
    users=[]
    def __init__(self,username,password):

        self.username=username
        self.password=password
        self.users.append([username,password])

    def delete_user(self,username):
        pass
    def display_users(self):
        for user in self.users:
            print(user[0])
class Admin(User):
    def __init__(self,username,password,is_admin):
        super().__init__(username,password)
        self.is_admin=is_admin
    def delete_user(self,username):
        for user in self.users:
            if user[0]==username:
                self.users.remove(user)

a1=Admin("shone",1223,True)
a2=User(username="shine",password=123)
a3=User(username="shan",password=1234)
a2.display_users()
a1.delete_user("shan")
print("#"*50)
a2.display_users()

