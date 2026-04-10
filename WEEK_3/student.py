day1 = {101, 102, 105, 108, 110}
day2 = {102, 103, 105, 109, 111}
both_days = day1 & day2
print("Present on both days:", both_days)
either_day = day1 | day2
print("Total unique students present:", either_day)
absent_day2 = day1 - day2
print("Students present on Day 1 but absent on Day 2:", absent_day2)