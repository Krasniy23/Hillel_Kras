from datetime import datetime

count_down = 3
while (count_down):
    print(count_down)
    count_down -= 1
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
print("Time is now:", time)
