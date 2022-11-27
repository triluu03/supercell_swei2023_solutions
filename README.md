# Supercell Software Engineer Summer Intern 2023

This repository is used to return solutions to the intern application exercises. 

Here are some explanations about the ideas!

## Exercise 1
#### The class ``User`` is used to store information about each individual user and support some operations:
- Store ``name``
- Store ``friends``
- Store ``timestamp``, which stores the last time that user updates the state.
- Support make friends and delete friends.

#### The ``Main`` class is used for the main solution to exercise 1. 
- The class attribute ``self.users``, which is a hash map (dictionary in Python), is used to store information about the users in the network. 
- The method ``handle_requests`` is used to handle each request from the input file. It divides and handle each "type" of requests separately. 

## Exercise 2
#### In this exercise, I used the module: ``threading`` from Python to create multiple threads. 
#### The class ``User`` is used nearly the same way as exercise 1. 
- In this exercise, the class ``User`` just stores the necessary information about each user (since there are only update requests).
#### The class ``MyThread``, which is a subclass of ``Thread`` from ``threading`` module, is used to create each thread.
- The attribute ``file`` of the class is used to pass the input file object to the class.
- The method ``run`` is used to process each line of the input file. 
  - In this case, there is a lock: ``threadLock``, the command ``threadLock.acquire()`` will lock this thread 
  and other threads will not run before the command ``threadLock.release()`` releases the lock. 
  - The lock is used to make sure that all the threads will handle different requests from each other. 
  - The lock will be released right after a line is read from the input file. Therefore, the "handling part" runs parallel with other threads. 

#### The function ``main`` is used for the main solution to exercise 2.
- The global variable ``users`` is used to store the information about the users in the network.
- The global variable ``threadLock`` is used for ``threading.Lock()`` as mentioned above.
- Currently, I declare 3 threads (I commented out 2 other threads, but they all run perfectly when put into use).
  - Each thread is declared using the ``MyThread`` class above.
  - Each thread is started using the method ``threading.Thread.start()``.
  - And the method ``threading.Thread.join()`` is called to make sure the parallel threads do run into any errors. 
