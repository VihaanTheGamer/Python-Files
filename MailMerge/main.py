#file = open("./input/names.txt")
#file_contents = file.readlines()
#print(file_contents)
#file.close()

with open("./input/names.txt") as file:
    names = file.readlines()

for name in names:
    name = name.strip()
    with open("./input/example_output.txt") as letter:
        letter_contents = letter.read()
        output_contents = letter_contents.replace("[name]", name )
    with open(f"./output/letter_to_{name}.txt", "w") as mail:
         mail.write(output_contents)
         
        
