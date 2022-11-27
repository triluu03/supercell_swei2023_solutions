import sys 
import json

class User:
    '''
    The class User is used to store the information of each user 
    and support some operations regarding each user, such as:
    making friends, deleting friends, storing friends information, etc.
    '''
    def __init__(self, name: str):
        self.name = name
        self.friends = set()
        self.friends_names = set()
        self.timestamp = 0
    
    def make_friends(self, friend: str):
        if friend not in self.friends:
            self.friends.add(friend)

    def del_friends(self, friend: str):
        if friend in self.friends:
            self.friends.remove(friend)
    
    

class Main:
    def __init__(self):
        self.users = {}

    def handle_request(self, input_value: dict):
        '''
        Method used to handle each request from the input
        '''
        type = input_value['type']
        #----- Handle making new friends -----
        if type == 'make_friends':
            user1 = input_value['user1']
            user2 = input_value['user2']
            if user1 not in self.users:
                self.users[user1] = User(user1)
            if user2 not in self.users:
                self.users[user2] = User(user2)
            
            user1: User = self.users[user1]
            user2: User = self.users[user2]

            if (user1 not in user2.friends) and (user2 not in user1.friends):
                user2.friends.add(user1)
                user2.friends_names.add(user1.name)

                user1.friends.add(user2)
                user1.friends_names.add(user2.name)
            else:
                raise LookupError('Both users seem to be friends already!')

        #----- Handle deleting friends -----
        elif type == 'del_friends':
            user1 = input_value['user1']
            user2 = input_value['user2']
            if user1 not in self.users or user2 not in self.users:
                raise KeyError(f"One of two users: {user1} or {user2} does not exist!")
            
            user1: User = self.users[user1]
            user2: User = self.users[user2]

            user1.friends.remove(user2)
            user1.friends_names.remove(user2.name)

            user2.friends.remove(user1)
            user2.friends_names.remove(user1.name)

        #----- Handle updating (broadcasting) ----- 
        elif type == 'update':
            user = input_value['user']
            timestamp = input_value['timestamp']
            values = input_value['values']

            if user not in self.users:
                self.users[user] = User(user)
            
            output = {}
            user: User = self.users[user]


            if timestamp > user.timestamp and bool(values):
                user.timestamp = timestamp
                if bool(user.friends):
                    output['broadcast'] = list(user.friends_names)
                else:
                    return 
                output['user'] = user.name
                output['timestamp'] = timestamp
                output['values'] = values
                sys.stdout.write(str(output) + '\n')
            else:
                return

        # ---- When Type is not in the set of operations ------
        else:
            raise TypeError(f"{type} is not correct!")

    def main(self):
        '''
        Main function (method) for the solution
        '''
        filename = sys.argv[2]
        with open(f"./tests/ex1/{filename}") as file:
            for line in file:
                input_value = json.loads(line)
                self.handle_request(input_value=input_value)
        





if __name__ == '__main__':
    solution = Main()
    solution.main()


