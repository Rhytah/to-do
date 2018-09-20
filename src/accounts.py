accounts = []#key is user, valu is pswd
user={}


def add_account(self,name,password):

    self.name= input("Please enter your name: ")
    self.password= input("Please enter secret word: ")
    accounts.append(name)
    accounts.append(password)
    user={name:password}
    user.update({accounts:[]})
    print (accounts)
    

def login(self,name,password):
    self.name= name
    self.password= password
    if name == self.name and password==self.password:
        print (True)
            
