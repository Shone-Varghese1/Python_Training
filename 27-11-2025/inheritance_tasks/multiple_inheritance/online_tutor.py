class ContentCreator:
    def __init__(self,no_of_followers):
        self.no_of_followers = no_of_followers
class Teacher:
    def __init__(self,years_of_experience):
        self.years_of_experience = years_of_experience
class OnlineTrainer(Teacher,ContentCreator):
    def __init__(self,years_of_experience,no_of_followers,platform):
        Teacher.__init__(self,years_of_experience)
        ContentCreator.__init__(self,no_of_followers)
        self.platform = platform

o1=OnlineTrainer(10,20000,"Teams")
print(o1.no_of_followers,o1.years_of_experience,o1.platform)