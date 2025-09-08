try:
   with open("file.txt", "r") as file:
       content = file.read()
except FileNotFoundError as f:
    print("File not found",f)
finally:
    print("This will always execute")