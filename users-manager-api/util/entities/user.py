class User():
    def __init__(self, firstName: str, lastName: str, age: int, email: str, phone: str):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.phone = phone
        
    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, firstName):
        self.firstName = firstName
        
    def getLastName(self):
        return self.lastName
    
    def setLastName(self, lastName):
        self.lastName = lastName
        
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
        
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
        
    def getPhone(self):
        return self.phone
    
    def setPhone(self, phone):
        self.phone = phone
        
    def showInfo(self):
        info = 'firstName: ' + self.firstName + '\nlastName: ' + self.lastName + '\nage: ' + str(self.age) + '\nemail: ' + self.email + '\nphone: ' + self.phone
        return info