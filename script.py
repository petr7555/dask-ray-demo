import socket
import time
from collections import Counter

import ray

ray.init()

print(f'''This cluster consists of
    {len(ray.nodes())} nodes in total
    {ray.cluster_resources()['CPU']} CPU resources in total
''')


@ray.remote
def f() -> str:
    time.sleep(0.001)
    # Return IP address.
    return socket.gethostbyname(socket.gethostname())


object_ids = [f.remote() for _ in range(10000)]
ip_addresses = ray.get(object_ids)

print('Tasks executed')
for ip_address, num_tasks in Counter(ip_addresses).items():
    print(f'    {num_tasks} tasks on {ip_address}')
