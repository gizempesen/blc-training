import os , sys
import time

#current file path
path = os.getcwd()
print(path)

# list
list = os.listdir(path)
print(list)

#path size
pathsize = os.path.getsize(path)
print(pathsize)

#time

modified_time = os.path.getmtime(path)
now = time.time()
print(modified_time)
print(now)

def main():
    if pathsize < 2000000 and modified_time > now - (45 * 60 * 1000): 
      print(list)
main() 
