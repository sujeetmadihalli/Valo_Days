curlevel = int(input("Enter your current level:"))
print("*******************************************************************")

val = curlevel
xd = val

xp = val
add = 0
for val in range(curlevel, 51, 1):
    xp = val + 2
    add = add + xp
totalxp = add * 1000

print("XP needed to complete the battlepass: " + str(totalxp) + " xp")

print()

perdaymatch = int(input("Enter the average number of matches you play per day:"))

matchxp = perdaymatch * 4500
dailyxp = 4000
perdayxp = matchxp + dailyxp
weeklyxp = 50000
day = 0
allxp = 0
while not (allxp >= totalxp):
    day = day + 1
    if (day % 7 == 0):
        allxp = allxp + weeklyxp + perdayxp
    else:
        allxp = allxp + perdayxp

print("The number of days needed to complete your battlepass with your current pace is averagely " + str(day) + " days")
print()
print()
