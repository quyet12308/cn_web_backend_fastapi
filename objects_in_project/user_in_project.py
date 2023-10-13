

class User_in_project:
    def __init__(self,username ,email ,password ,birthday ,avata_img ,createdTime ):
        self.username = username
        self.email = email
        self.password = password
        self.birthday = birthday
        self.avata_img = avata_img
        self.createdTime = createdTime

user1 = User_in_project(email="abc")

print(user1)
