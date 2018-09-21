user={"Rhy":"tah"}#key is user, valu is pswd
accounts = [] #list of users



def add_account(name,password):
    print("USER SIGNUP")

    name= str(input("Please enter your name: "))
    password= str(input("Please enter secret word: "))
    user=dict()

    if name and password not in user:
        user['name']=name
        user['password']=password
        accounts.append(user)
        print("Account created")
        print(accounts)
    

  

def login(name,password):
    print("USER LOGIN")
    name= str(input("Username: "))
    password= str(input("Secret: "))
    if name in user and user[name]==password:
        return True
    return False
            
