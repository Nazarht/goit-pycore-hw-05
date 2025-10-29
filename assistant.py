import readline
from collections import defaultdict
from functools import wraps

def input_error(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid value"
        except IndexError:
            return "Not enough arguments"
        except KeyError:
            return "Contact not found"
        except TypeError:
            return "Invalid type"
        except Exception:
            return "Internal server error"
        
    return wrapper

def parse_input(input_string: str) -> tuple[str, list[str]]:
    command, *args = input_string.split()
    return command, args

def handle_hello(_: list[str], __: defaultdict[str, str]) -> None:
    return "How can I help you?"

@input_error
def handle_add(args: list[str], contacts: defaultdict[str, str]) -> str:
    contact_name = args[0]
    contact_phone_number = args[1]
    contacts[contact_name] = contact_phone_number
    return f"Contact {contact_name} added successfully"

@input_error
def handle_change(args: list[str], contacts: defaultdict[str, str]) -> str:
    contact_name = args[0]
    contact_phone_number = args[1]
    if contact_name not in contacts:
        raise KeyError()
    
    contacts[contact_name] = contact_phone_number
    return f"Contact {contact_name} updated successfully"

@input_error
def handle_phone(args: list[str], contacts: defaultdict[str, str]) -> str:
    if len(args) < 1:
        return "Please provide a contact name"
    contact_name = args[0]
    return f"Contact {contact_name} phone number is {contacts.get(contact_name)}"

@input_error
def handle_all(_: list[str], contacts: defaultdict[str, str]) -> str:
    result: list[str] = []
    
    for contact_name, contact_phone_number in contacts.items():
        result.append(f"{contact_name} - {contact_phone_number}")
    
    if not result:
        return "No contacts found"
    
    return "\n".join(result)

handlers: dict[str, callable] = {
    "hello": handle_hello,
    "add": handle_add,
    "change": handle_change,
    "phone": handle_phone,
    "all": handle_all,
}

def main():
    contacts: defaultdict[str, str] = defaultdict(lambda: 'not found')

    while True:
        try:
            user_input = input("Enter a command: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        if not user_input.strip():
            continue

        command, args = parse_input(user_input)
        command = command.lower()

        if command in ("exit", "close"):
            print("Good bye!")
            break

        handler = handlers.get(command, None)
        if handler is None:
            print("Invalid command")
            continue

        result = handler(args, contacts)
        print(result)

if __name__ == "__main__":
    main()