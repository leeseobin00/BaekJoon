hour, minute = input().split()

hour = int(hour)
minute = int(minute)

result_hour = hour
result_minute = minute - 45

if result_minute < 0:
    result_hour -= 1
    result_minute += 60

if result_hour < 0:
    result_hour += 24

print(str(result_hour) + " " + str(result_minute))