user_a_interests = {"Python", "Data Science", "Machine Learning", "Web Development", "Databases"}
user_b_interests = {"Python", "Web Development", "Graphic Design", "UI/UX","Java" ,"Databases"}
print(f"User A Interests: {user_a_interests}")
print(f"User B Interests: {user_b_interests}\n")
common_interests = user_a_interests.intersection(user_b_interests)
print("Common interests:", common_interests)
print("-" *20)
suggestions_for_a = user_b_interests.difference(user_a_interests)
print("Suggestions for User A (from User B's list):", suggestions_for_a)
print("-" * 20)