from random import randint

def thing():
    print(f"hello world {randint(100000, 999999)}")

count = 0
target = randint(10, 100)
while True:
    thing()
    if count == target:
        with open("modify_running_file_test2.py", "w+") as f:
            f.write("print(\"Hello world!\")")  

        count += 1