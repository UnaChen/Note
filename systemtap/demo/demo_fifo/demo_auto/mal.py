import os
f = os.open("new", os.O_CREAT)
os.close(f)

os.remove("new")

