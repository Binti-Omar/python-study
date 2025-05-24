# Create a file called mydstask.py and attempt the below questions:
# my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
my_ds = [23, "Jane", 560, ["Lesson", "Maths", {"currency": "KES"}], 987, (76, "John")]
# 1. Print KES
print(my_ds[3][2]["currency"])  # Output: KES
# 2. Print 560
print(my_ds[2])  # Output: 560
# 3. Print Maths
print(my_ds[3][1])  # Output: Maths
# 4. In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"] = 90
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#      Hint: Strings can be reversed using [::]
my_ds[4] = int(str(my_ds[4])[::-1])  # Reverse 987 to 789
print(my_ds[4])  # Output: 789
# 6. Change the name “John” to “Jane” .
my_ds[5] = (my_ds[5][0], "Jane")  # Change "John" to "Jane"
print(my_ds[5])  # Output: (76, "Jane")
# You can research or discuss to find the solutions above.
#         https://realpython.com/quizzes/pybasics-tuples-lists-dicts/ 
