__author__ = 'laxdjole'

class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.table = self.getTable(username,password)
        print("%s %s" % (self.username,self.password))

    def getTable(self,username,password):
        #access database and check for user, try except if user or not, recommend creating account ect
        mocktable = {
                        'Bleach':{'title'   :'Bleach',
                                  'lastread': 20, },

                        'Naruto':{'title'   : 'Naruto',
                                  'lastread': 10, },

                        'GTO'   :{'title'   : 'GTO',
                                  'lastread': 15 }        }
        return mocktable




# if __name__ == "__main__":
#     marko = Users(username="marko",password="polo")