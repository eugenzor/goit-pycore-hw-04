def parse_input(user_input: str) -> tuple[str, ...]:
    """Розібрати рядок вводу на команду та аргументи."""
    if not user_input.strip():
        return ("",)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command. Usage: add <name> <phone>"
    name, phone = args
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' to update the phone."
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command. Usage: change <name> <phone>"
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return "Invalid command. Usage: phone <name>"
    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "Contacts list is empty."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main() -> None:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "":
            print("Invalid command.")
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
