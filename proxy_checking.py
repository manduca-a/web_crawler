import threading
import requests
import queue

q = queue.Queue()

valids = []

with open("proxies.txt", "r") as f:
    for line in f:
        q.put(line.strip())
        print(f"Added {line.strip()} to the queue.")

def worker():
    while not q.empty():
        proxy = q.get()
        try:
            response = requests.get("https://ipinfo.io", proxies={"http": proxy, "https": proxy})
            if response.status_code == 200:
                valids.append(proxy)
                print(f"{proxy}")
            else:
                print(f"{proxy} is not valid.")
        except Exception as e:
            continue
        q.task_done()

for _ in range(10):
    t = threading.Thread(target=worker)
    t.start()