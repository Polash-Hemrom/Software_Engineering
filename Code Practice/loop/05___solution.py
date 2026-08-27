# 5. Find the First Non-Repeated Character


character = 'Repeat'

for char in character:
    if character.count(char) == 1:
        print(char)