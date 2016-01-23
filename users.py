import pickle
import os


class Users(object):
    def __init__(self):
        self.filename = 'pocket_users.p'
        self.available = os.path.exists(self.filename)
        self.users = {}
        return

    def add_user(self, name, access_code):
        name = name.lower()
        self.load_users()
        if name in self.users:
            raise IOError('User\'s name is already in use \n'
                          'Use "modify_user" function to make changes')
        else:
            self.users[name] = access_code
            fileHandle = open(self.filename, 'wb')
            users = self.users
            pickle.dump(users, fileHandle)
            self.available = True
        return 'Added User --> {0} with Code --> {1}'.format(name, access_code)

    def delete_user(self, name):
        name = name.lower()
        self.load_users()
        if name in self.users:
            if name == 'larry':
                return 'Can\'t delete this root user, Larry'
            self.users.pop(name)
            if self.users:
                fileHandle = open(self.filename, 'wb')
                users = self.users
                pickle.dump(users, fileHandle)
            else:
                os.remove(self.filename)
                self.available = False
        else:
            raise IOError('User\'s name does not exists!')
        return 'Deleted User --> {0}'.format(name)

    def get_token(self, name):
        name = name.lower()
        self.load_users()
        if name in self.users:
            return self.users[name]
        else:
            raise IOError('User\'s name does not exists, Add name')
        return

    def load_users(self,alone=False):
        if self.users:
            pass
        else:
            if self.available:
                fileHandle = open(self.filename, 'rb')
                self.users = pickle.load(fileHandle)
        if alone:
            print(self.users)
        return

if __name__ == '__main__':
    people = Users()
    people.add_user('larry', 'c7112800-b3c5-4c53-04f0-4e126b')
