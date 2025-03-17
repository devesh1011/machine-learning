import threading


def hello_world():
    for i in range(10):
        print("one")


def bye_world():
    for i in range(10):
        print("two")


t1 = threading.Thread(target=hello_world)
t2 = threading.Thread(target=bye_world)

t1.start()
t1.join()

t2.start()
