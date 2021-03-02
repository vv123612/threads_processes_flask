import requests
from multiprocessing import Process

r = requests.get('http://127.0.0.1:5000/')
print(r.text)

def get_request(process_name):
  for i in range(10):
    r = requests.get('http://127.0.0.1:5000/')
    print(f'process_name - {process_name}; step = {i} ;  response = {r.text}')

# clients_lst = []
# for j in range(5):
#   clients_lst.append(Process(target=get_request, args=(j,)))

# for j in range(len(clients_lst)):
#   clients_lst[j].start()


# Process(target=get_request, args=(0,)).start()
# Process(target=get_request, args=(1,)).start()
# Process(target=get_request, args=(2,)).start()
# Process(target=get_request, args=(3,)).start()
# Process(target=get_request, args=(4,)).start()

# client0 = Process(target=get_request, args=(0,))
# client0.start()

# client1 = Process(target=get_request, args=(1,))
# client1.start()

# client2 = Process(target=get_request, args=(2,))
# client2.start()

# client3 = Process(target=get_request, args=(3,))
# client3.start()

# client4 = Process(target=get_request, args=(4,))
# client4.start()

def foo():
    print(1)

# client_x = Process(target=foo)
# client_x.start()
