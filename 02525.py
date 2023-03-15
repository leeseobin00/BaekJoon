hour, minute = input().split()
cook = int(input())

hour = int(hour)
minute = int(minute)

result_hour = hour + int((minute + cook) / 60)
result_minute = (minute + cook) % 60

if result_hour > 23:
    result_hour -= 24

print(str(result_hour) + " " + str(result_minute))
