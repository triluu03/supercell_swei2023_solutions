import sys
import json

import threading


class User:
    '''
    The class User is used to store the information of each user 
    '''
    def __init__(self, name: str):
        self.name = name
        self.timestamp = 0
        self.values = {}
    

class MyThread(threading.Thread):
    """
    Class Thread to handle the file
    """
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.file = file
        
    def run(self):
        while True:
            threadLock.acquire()
            line = self.file.readline()
            threadLock.release()

            if line == '':
                break 

            input_value = json.loads(line)

            user = input_value["user"]
            timestamp = input_value["timestamp"]
            values = input_value["values"]

            if user not in users:
                users[user] = User(user)
            
            user: User = users[user]
            if timestamp > user.timestamp and bool(values):
                user.values.update(values)


def get_users_state(users):
    '''
    Print the users state in JSON format. 
    '''
    output = {}
    for name in users:
        user = users[name]
        output[name] = user.values
    return output

def main():
    '''
    The main function to handle the input requests file
    '''

    # Dictionary (Hash Map) to store the information of the users
    global users
    users = {}

    # Thread Lock 
    global threadLock
    threadLock = threading.Lock()

    filename = sys.argv[2]
    with open(f"./tests/ex2/{filename}") as file:
        # Creating Threads
        thread1 = MyThread(file)
        thread2 = MyThread(file)
        thread3 = MyThread(file)
        # thread4 = MyThread(file)
        # thread5 = MyThread(file)
        
        # Starting each thread
        thread1.start()
        thread2.start()
        thread3.start()
        # thread4.start()
        # thread5.start()

        # Join each thread to the main thread
        thread1.join()
        thread2.join()
        thread3.join()
        # thread4.join()
        # thread5.join()

    print(get_users_state(users))


if __name__ == '__main__':
    main()




