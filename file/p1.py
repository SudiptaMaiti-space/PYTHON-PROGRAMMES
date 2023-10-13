f = open("demofile.txt", "r")
print(f.read())
print("---------------------------")
f.seek(0)
print(f.readline())
print(f.readline())
print("---------------------------")
f.seek(0)
print(f.read(5))
print("---------------------------")
f.seek(0)
for x in f:
 print(x)
print("---------------------------")
print("---------------------------")
f.close()


f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

words=0
with open("demofile.txt","r") as f:
    for line in f:
        w=line.split()
        words+=len(w)
max_len=len(max(w,key=len))
print(words)


"""
import os
if os.path.exists("demofile.txt"):
 os.remove("demofile.txt")
else:
 print("The file does not exist")  """
