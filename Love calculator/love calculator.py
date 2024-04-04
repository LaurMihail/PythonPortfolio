print("The Love Calculator is calculating your score...")
name1 = input("What is your name: ")
name2 = input("What is their name: ")
combined_name = name1 + name2
lower_names = combined_name.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, the relationship is beautiful and fascinating, but sometimes it can be tumultuous or unpredictable.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, your harmony is a symphony of souls entwined. In your union, stars dance and constellations shine.")
else:
    print(f"Your score is {score}. Your compatibility seems to be missing entirely. You should try again.")
