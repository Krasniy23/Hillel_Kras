import time

def time_count(func):
    def counter():
        for i in range(1, 4):
            print(i)
            time.sleep(i)
        func()
    return counter()

@time_count
def time_is_now():
    print("Now " + time.strftime("%H:%M:%S"))
