#Task 1
def name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        problem_name = ('first name' if len(first_name) < 2 else 'last name')
        return f"Error, {problem_name} is too short"
    else:
        return f"Welcome {first_name} {last_name}"

while True:
    first_name_input = input("Please input your first name: ")
    last_name_input = input("Please enter your last name: ")

    length_validator = name_length(first_name_input, last_name_input)
    print(length_validator)

    continue_input = input("Is there another name you'd like to enter: (yes/no) ").lower()
    if continue_input != 'yes':
        break

#Task 2
def password_checker(password):
    problems = []
    number_count = 0
    upper_count = 0
    lower_count = 0

    if len(password) < 8:
        problems.append(f"- {8 - len(password)} characters")
    
    for char in password:
        if char.isupper():
            upper_count += 1
            
    if upper_count < 1:
        problems.append("- uppercase letter")


    for char in password:
        if char.islower():
            lower_count += 1
            
    if lower_count < 1:
        problems.append("- lowercase letter")


    for char in password:
        if char.isdigit():
            number_count += 1
            
    if number_count < 1:
        problems.append("- number")

    if problems:
        print("Missing: ")
        for problem in problems:
            print(problem)

        return "Please fix these errors and try again"
    else:
        return "Password meets all criteria"



while True:
    password_input = input("Input password to be checked: ")

    password_check = password_checker(password_input)

    print(password_check)

    continue_input = input("Would you like to check another password? (yes/no) ").lower()
    if continue_input != 'yes':
        break


#Task 3
def email_formatter(username, web_address):
    return username + "@" + web_address

while True:
    username_input = input("Enter your email username: ")
    web_address_input = input("Enter your web address in .com format (e.g. gmail.com, yahoo.com, comcast.net): ")

    email_formatting = email_formatter(username_input, web_address_input)
    print(email_formatting)
    
    continue_input = input("Would you like to format another email? (yes/no) ").lower()

    if continue_input != 'yes':
        break