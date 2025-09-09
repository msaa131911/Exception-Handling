try:
    f = open("studen.txt", "r")
    print(f.read(5))
    print(f.tell())
    f.seek(0)
    print(f.tell())
    f.close()
except FileNotFoundError:
    print("it is not exiest")