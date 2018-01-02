import os
import time
f = os.open("new", os.O_CREAT)
os.close(f)
os.remove("new")
time.sleep(20)
