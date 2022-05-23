from time import sleep

x = 0
y = 1

print(x)
print(y)

while True:
    z = x + y
    x = y
    y = z

    print(y)

    sleep(0.5)
