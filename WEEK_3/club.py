records = ["Arun:AI,ML,Robotics", "Bala:ML,IoT", "Chitra:AI,CyberSecurity", "Divya:Robotics,IoT,AI", "Ezhil:ML,CyberSecurity","Farah:AI,ML", "Ganesh:IoT,Robotics,AI", "Hari:ML"]

# 1, 2, 3, 4: Extract names, clubs, and mapping
all_names = set()
all_clubs = set()
student_club_map = {}

for record in records:
    name, club_string = record.split(":")
    club_list = club_string.split(",")
    club_set = set(club_list) # Removes duplicates automatically

    all_names.add(name)
    all_clubs.update(club_set)
    student_club_map[name] = club_set

print("Unique Students:", all_names)
print("Unique Clubs:", all_clubs)

# 5. Members of both AI and ML
ai_and_ml = []
for name in student_club_map:
    if {"AI", "ML"}.issubset(student_club_map[name]):
        ai_and_ml.append(name)
print("Both AI and ML:", ai_and_ml)

# 6. AI but not Robotics
ai_no_robotics = []
for name, clubs in student_club_map.items():
    if "AI" in clubs and "Robotics" not in clubs:
        ai_no_robotics.append(name)
print("AI but not Robotics:", ai_no_robotics)

# 7. Clubs that no student belongs to alone
clubs_never_alone = set()
for club in all_clubs:
    alone = False
    for clubs in student_club_map.values():
        if club in clubs and len(clubs) == 1:
            alone = True
    if not alone:
        clubs_never_alone.add(club)
print("Clubs never joined alone:", clubs_never_alone)

# 8. Intersection of clubs for students whose names start with a vowel
vowel_start_clubs = []
for name, clubs in student_club_map.items():
    if name[0].lower() in "aeiou":
        vowel_start_clubs.append(clubs)

if vowel_start_clubs:
    vowel_intersection = set.intersection(*vowel_start_clubs)
    print("Intersection (Vowel Start):", vowel_intersection)

# 9. Union of clubs for students whose names end with a consonant
consonant_union = set()
for name, clubs in student_club_map.items():
    if name[-1].lower() not in "aeiou":
        consonant_union.update(clubs)
print("Union (Consonant End):", consonant_union)

# 10. All characters used in all names
all_chars = set("".join(all_names).lower())
print("All name characters:", all_chars)

# 11. Characters that appear in every student name
every_name_chars = set(records[0].split(":")[0].lower())
for name in all_names:
    every_name_chars &= set(name.lower())
print("Common chars in all names:", every_name_chars)

# 12. Name character set is a subset of "Arun"
arun_set = set("arun")
subset_arun = []
for name in all_names:
    if set(name.lower()).issubset(arun_set):
        subset_arun.append(name)
print("Names subset of 'Arun':", subset_arun)

# 13. Duplicate club combinations
club_lists = list(student_club_map.values())
shared_memberships = 0
for i in range(len(club_lists)):
    for j in range(i + 1, len(club_lists)):
        if club_lists[i] == club_lists[j]:
            shared_memberships += 1
print("Count of identical club memberships shared:", shared_memberships)

# 14. Sort students: Clubs (desc), then Alphabetical (asc)
sorted_students = sorted(all_names, key=lambda x: (-len(student_club_map[x]), x))
print("Sorted students:", sorted_students)

# 15. Final filtered set
def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

hari_clubs = student_club_map["Hari"]
final_set = set()
for name, clubs in student_club_map.items():
    # Condition A: Prime length
    cond_a = is_prime(len(name))
        cond_b = any(c[0].lower() in "aeiou" for c in clubs)
        cond_c = clubs.isdisjoint(hari_clubs)

    if cond_a and cond_b and cond_c:
        final_set.add(name)
print("Final Filtered Students:", final_set)