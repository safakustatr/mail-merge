with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

stripped_name_list = []
for name in name_list:
    stripped_name_list.append(name.strip())

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

for name in stripped_name_list:
    temp = letter.replace("[name]",name)
    f = open(f"Output/ReadyToSend/letter_for_{name}.txt", "w")
    f.write(temp)
