from sys import argv

script, user_name, age = argv
prompt = 'Enter Here >  '
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)
print(f"How old were you when you moved to {lives}, {user_name}?")
moved = (int(age)-int(input(prompt)))
print(f"Oh, so you moved there {moved} years ago.")

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
