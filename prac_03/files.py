# 1. Write user's name to a file using open and close
name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()

# 2. Read the name from the file and print greeting using open and close
name_file = open("name.txt", "r")
name_from_file = name_file.read().strip()
name_file.close()
print(f"Hi {name_from_file}!")

# 3. Read first two numbers from numbers.txt, add them, print result using with
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline().strip())
    second_number = int(numbers_file.readline().strip())
    print(first_number + second_number)  # Should print 59

# 4. Print total for all numbers in numbers.txt using with and for line in file
total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line.strip())

print(total)  # Should print sum of all numbers
