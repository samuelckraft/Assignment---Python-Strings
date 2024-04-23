#Task 1
def help_desk_bot(user):
    words = user.split()
    return_message = []
    for word in words:
        if word == 'help':
            return_message.append("Help has been requested")
        elif word == 'issue':
            return_message.append("Sorry for this problem, we will have someone reach out to resolve this shortly")
        elif word == 'contact' and 'support':
            return_message.append("Support has been contacted")
        else:
            continue
    
    for message in return_message:
        return message

while True:
    user_input = input("Is there anything I can help with? ").lower()

    helper = help_desk_bot(user_input)
    print(helper)

    continue_input = input("Can I help with anything else? (yes/no) ").lower()
    if continue_input != 'yes':
        break


#Task 2
def help_desk_bot(user):
    words = user.split()
    return_message = []
    for word in words:
        if word == 'help':
            return_message.append("Help has been requested")
        elif word == 'issue':
            return_message.append("Sorry for this problem, we will have someone reach out to resolve this shortly")
        elif word == 'contact' and 'support':
            return_message.append("Support has been contacted")
        else:
            continue
    
    for message in return_message:
        return message

while True:
    user_input = input("Is there anything I can help with? ").lower()

    helper = help_desk_bot(user_input)
    print(helper)

    issue_message = []
    if 'issue' in user_input:
        qualifying_input = input("Where are you experiencing issues? (login, performance, error messages) ").lower()
        if qualifying_input == 'login':
            issue_message.append("- login")
        elif qualifying_input == 'performance':
            issue_message.append("- performance")
        elif qualifying_input == 'error messages':
            issue_message.append("- error messages")
        else:
            print("I'm sorry that input is not valid please try again")

    if len(issue_message) > 0:
        for issue in issue_message:
            print(f"User is experiencing problems with: {issue}")

    continue_input = input("Can I help with anything else? (yes/no) ").lower()
    if continue_input != 'yes':
        break