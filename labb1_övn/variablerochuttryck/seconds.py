sekunder = int(input("How many seconds?:"))
minutes = (sekunder - ((sekunder // 3600) * 3600)) // 60
hours =  sekunder // 3600
seconds =(sekunder - ((sekunder // 3600) * 3600)) - (((sekunder - ((sekunder // 3600) * 3600)) // 60)*60)

print(sekunder, "seconds are", hours, "hours,", minutes, "minutes and", seconds, "seconds")