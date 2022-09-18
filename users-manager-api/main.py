from util.userDAO import UserDAO
from util.entities.user import User
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == "__main__":
    userDAO = UserDAO()
    
    # Insert User
    #user1 = User("Steve","Rogers",28,"capamerica@test.com","999999999")
    user1 = User("Bruce","Banner",30,"hulk@test.com","919191919")
    userDAO.insertUser(user1)
    
    # List all users
    users = userDAO.listUsers()
    i = 1
    for user in users:
        print("--------------------------user % s--------------------------" % (i))
        print(user.showInfo())
        i+=1
    
    # List a specific user
    user = userDAO.listUser("2")
    print(user.showInfo())
    
    # Delete an user
    userDAO.deleteUser("3")
    
    # Update an user
    userTest = User("Thor","Odinson",1000,"thor@test.com","912913914")
    userDAO.editUser(userTest, "4")