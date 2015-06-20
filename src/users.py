__author__ = 'laxdjole'

class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        print("%s %s" % (self.name,self.password))
    def getTable(self):
        pass




if __name__ == "__main__":
    marko = Users(name="marko",password="polo")