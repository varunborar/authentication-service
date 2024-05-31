import uuid


class User:

    def __init__(
            self,
            firstName,
            lastName,
            email,
            password,
            userid=None
    ):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        if not userid:
            self._uid = str(uuid.uuid4())
        else:
            self._uid = userid

    def getUser(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "userid": self._uid
        }

    @property
    def uid(self):
        return self._uid
