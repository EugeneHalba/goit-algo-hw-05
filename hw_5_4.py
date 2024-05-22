def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
# create decorator
def input_error (func):
    def inner(*args,**kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return "Enter the argument for the command"
        
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added." 

            # START MY CODE

# change existing contact
@input_error
def change_contact(args, contacts, phone):
    name = args [0]
    if name in contacts:
        contacts[name] = phone
        name.format(phone)
        return "Contact updated."
    else:
        return "Contact does not find"
# show contact by name
@input_error
def show_contact (args, contacts):
    name = args [0]
    if name in contacts:
        return contacts[name]
    else:
        return "contact does not exist"
# show all contacts
@input_error
def show_all (args, contacts): 
    all_name = []
    for name in contacts:
        all_name.append(contacts)
    return all_name
                #END MY CODE
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
                
                # START MY CODE

    # show contact by name
        elif command == "phone":
            print (show_contact(args,contacts))
    # show all contacts
        elif command == "all":
            print (show_all(args,contacts))
    # change existing contact  
        elif command == "change":
            print (change_contact(args, contacts))

                # END MY CODE
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
