import re


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError as e:
            return str(e)
        except IndexError as e:
            return str(e)

    return inner


def validate_phone(phone):
    if not re.match(r"^\+?\d{10,}$", phone):
        raise ValueError("Invalid phone number. Please enter a valid phone number.")
    return True


@input_error
def add_contact(contacts, name, phone):
    if validate_phone(phone):
        contacts[name] = phone
        return "Contact added."


@input_error
def change_contact(contacts, name, new_phone):
    if not validate_phone(new_phone):
        raise ValueError("Invalid phone number. Please enter a valid phone number.")
    elif name not in contacts:
        raise KeyError("Contact not found.")
    else:
        contacts[name] = new_phone
        return "Contact updated."


@input_error
def remove_contact(contacts, name):
    if name not in contacts:
        raise KeyError("Contact not found.")
    else:
        contacts.pop(name)
        return "Contact deleted."


@input_error
def show_phone(contacts, name):
    if name not in contacts:
        raise KeyError("Contact not found.")
    return contacts[name]


@input_error
def show_all(contacts):
    if len(contacts) == 0:
        raise ValueError("No contacts found.")
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# Show available commands.
def show_info():
    info_message = (
        "Available commands:\n"
        "add [name] [phone] - Add a new contact with a valid phone number.\n"
        "change [name] [new phone] - Change an existing contact's phone number.\n"
        "phone [name] - Display a contact's phone number.\n"
        "all - Show all saved contacts and their phone numbers.\n"
        "exit or close - Close the program.\n"
        "hello - Greeting from the assistant.\n"
        "info - Show available commands."
    )
    return info_message


# Interprets user commands.
@input_error
def main():
    contacts = {}
    while True:
        try:
            command = input("Enter a command: ").strip().lower()
            if len(command) == 0:
                continue
            if command in ["exit", "close"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "info":
                print(show_info())
            else:
                parts = command.split()
                cmd = parts[0]
                if cmd == "add":
                    if len(parts) < 3:
                        raise IndexError("Add command requires name and phone number.")
                    name, phone = parts[1], parts[2]
                    print(add_contact(contacts, name, phone))
                elif cmd == "change":
                    if len(parts) < 3:
                        raise IndexError(
                            "Change command requires name and new phone number."
                        )
                    name, new_phone = parts[1], parts[2]
                    print(change_contact(contacts, name, new_phone))
                elif cmd == "remove":
                    if len(parts) < 2:
                        raise IndexError("Remove command requires a name.")
                    name = parts[1]
                    print(remove_contact(contacts, name))
                elif cmd == "phone":
                    if len(parts) < 2:
                        raise IndexError("Phone command requires a name.")
                    name = parts[1]
                    print(show_phone(contacts, name))
                elif cmd == "all":
                    print(show_all(contacts))
                else:
                    raise ValueError("Invalid command.")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
