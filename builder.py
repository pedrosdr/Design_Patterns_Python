from abc import ABC, abstractmethod

class User:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []

    def __str__(self):
        text = f"User("
        text += f"firstname={self.firstname}, "
        text += f"lastname={self.lastname}, "
        text += f"age={self.age}, "
        text += f"phone_numbers={self.phone_numbers}, "
        text += f"phone_addresses={self.addresses}"
        text += f")"
        return text

class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):pass

    @abstractmethod
    def set_firstname(self, firstname): pass

    @abstractmethod
    def set_lastname(self, lastname): pass

    @abstractmethod
    def set_age(self, age): pass

    @abstractmethod
    def add_phone_number(self, phone_number): pass

    @abstractmethod
    def add_address(self, address): pass

class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def set_firstname(self, firstname):
        self._result.firstname = firstname
        return self

    def set_lastname(self, lastname):
        self._result.lastname = lastname
        return self

    def set_age(self, age):
        self._result.age = age
        return self

    def add_phone_number(self, phone_number):
        self._result.phone_numbers.append(phone_number)
        return self

    def add_address(self, address):
        self._result.addresses.append(address)
        return self

class UserDirector:
    def __init__(self, builder):
        self._builder: UserBuilder = builder

    def with_age(self, firstname, lastname, age):
        self._builder\
            .set_firstname(firstname)\
            .set_lastname(lastname)\
            .set_age(age)
        return self._builder.result
    
if __name__ == "__main__":
    ud = UserDirector(UserBuilder())
    print(ud.with_age("name", "asdf", 34))
