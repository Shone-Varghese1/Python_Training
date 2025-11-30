
class Camera:
    def take_photo(self):
        return "Photo taken."

class Phone:
    def make_call(self):
        return "Calling..."

class SmartPhone(Camera, Phone):
    def use_apps(self):
        return "Using apps on smartphone."


sp = SmartPhone()
print(sp.take_photo())
print(sp.make_call())
