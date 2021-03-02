from flask_server import app
from time import sleep

from threading import Thread
import requests
from multiprocessing import Process


# app.run()


th_server = Thread(target=app.run)
th_server.start()
# th_server.join()
print('flask server starting')
sleep(1)


# r = requests.get('http://127.0.0.1:5000/')
# print(r.text)

def get_request(process_name):
  for i in range(10):
    r = requests.get('http://127.0.0.1:5000/')
    s = f'process_name - {process_name}; step = {i} ;  response = {r.text}'
    print(s)


# client0 = Thread(target=get_request, args=(0,))
# client0.start()

# client1 = Thread(target=get_request, args=(1,))
# client1.start()

# client2 = Thread(target=get_request, args=(2,))
# client2.start()

# client3 = Thread(target=get_request, args=(3,))
# client3.start()

# client4 = Thread(target=get_request, args=(4,))
# client4.start()

threads_lst = []

for j in range(10):
    client_x = Thread(target=get_request, args=(j,))
    client_x.start()
    threads_lst.append(client_x)


for th in threads_lst:
    th.join()

print('last command')
r = requests.get('http://127.0.0.1:5000/shutdown')
print(r.text)
