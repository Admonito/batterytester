import time
import psutil
import itertools
usage = input("What will you be using your Laptop for? ")
start = (input("Do you want to start the battery test? y/n "))
if start == "y":
    while True:
        for elapsedtime in (itertools.count(0,25)):
            battery = psutil.sensors_battery()
            percent = battery.percent
            slice = str(percent)
            timenow = time.strftime("%Y %B %d %H:%M:%S", time.localtime())
            cpupercent = str(psutil.cpu_percent())
            print("Time:" + " " + str(timenow) + " Usage:" + usage + " Elapsed seconds:" + str((elapsedtime)) + " CPU Percent:" + cpupercent + " Battery Percentage:" + slice[0:5] + "% " + "Charging:" + str(battery.power_plugged))
            file = open('testresult.txt','a')
            file.write("Time:" + " " + str(timenow) + " Usage:" + usage + " Elapsed seconds:" + str((elapsedtime)) + " CPU Percent:" + cpupercent + " Battery Percentage:" + slice[0:5] + "% " + "Charging:" + str(battery.power_plugged),)
            file.write('\n')
            time.sleep(25)
elif start == "n":
    print("Closing...")
else:
    print("I said that you need to type a y or a n, but you didnt type neither.")
