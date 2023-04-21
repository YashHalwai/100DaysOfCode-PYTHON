# MultiProcessing in Python | Python Tutorial - Day #98

# https://www.youtube.com/watch?v=zGe-9LfnAaA&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=98


"""Multiprocessing refers to the ability of a system to support more than one processor at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates these threads to the processors improving performance of the system."""

# import multiprocessing
# import requests

import concurrent.futures
import requests


def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"



# def downloadFile(url, name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     open(f"({name}.jpg", "wb").write(response.content)
#     print(f"Finishing Downloading {name}")

# url = ["https://picsum.photos/200/300"]
# pros = []

# for i in range(5): 
#     # downloadFile(url,i)
#     p = multiprocessing.Process(target=downloadFile,args=[url,i])
#     p.start()
#     pros.append()
    
# for p in pros:
#     p.join()    



with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)