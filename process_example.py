# from threading import Thread
from multiprocessing import Process
from time import sleep

def func():
    for i in range(5):
        print(f"from child process: {i}")
        sleep(0.5)


pr = Process(target=func)
pr.start()

for i in range(5):
    print(f"from main process: {i}")
    sleep(1)