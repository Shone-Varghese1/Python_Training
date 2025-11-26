class Mobile:
    def __init__(self,brand,model,storage):
        self.brand=brand
        self.model=model
        self.storage=storage
        self.allowed_storage=[128,256,512,1024]
    def display(self):
        print("brand ",self.brand)
        print("model ",self.model)
        print("storage ",self.storage,"GB")
    def increase_storage(self):
        index=-1
        if self.storage in self.allowed_storage:
            index=self.allowed_storage.index(self.storage)
        if index<len(self.allowed_storage)-1:
            self.storage=self.allowed_storage[index+1]
        else:
            print("maximum allowed storage")

m1=Mobile("Samsung","S24",128)
m1.display()
print()
m1.increase_storage()
m1.display()