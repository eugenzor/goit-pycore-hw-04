import sys
from pathlib import Path

from colorama import Fore, Style, init

DIR_ICON = "📁"
FILE_ICON = "📄"


def red(text: str) -> str:
    return f"{Fore.RED}{text}{Style.RESET_ALL}"


def green(text: str) -> str:
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"


def blue(text: str) -> str:
    return f"{Fore.BLUE}{text}{Style.RESET_ALL}"


def build_directory_tree(directory: Path, prefix: str = "") -> str:
    """Рекурсивно побудувати рядок зі структурою директорії з кольоровим розрізненням."""
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower()),
        )
    except PermissionError:
        return f"{prefix}{red('[немає доступу]')}\n"

    lines: list[str] = []
    total = len(entries)
    for index, entry in enumerate(entries):
        connector = "└── " if index == total - 1 else "├── "
        if entry.is_dir():
            lines.append(f"{prefix}{connector}{DIR_ICON} {blue(entry.name + '/')}")
            extension = "    " if index == total - 1 else "│   "
            subtree = build_directory_tree(entry, prefix + extension)
            if subtree:
                lines.append(subtree.rstrip("\n"))
        else:
            lines.append(f"{prefix}{connector}{FILE_ICON} {green(entry.name)}")

    return "\n".join(lines)


def render_tree(target: Path) -> str:
    """Сформувати повний рядок виводу для коректної директорії."""
    header = f"{DIR_ICON} {blue(f'{target.resolve()}/')}"
    body = build_directory_tree(target)
    return f"{header}\n{body}" if body else header


def usage_message(program_name: str) -> str:
    return f"Використання: python {program_name} <шлях_до_директорії>"


def path_error_message(target: Path) -> str:
    if not target.exists():
        return red(f"Помилка: шлях '{target}' не існує.")
    return red(f"Помилка: '{target}' не є директорією.")


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(usage_message(Path(sys.argv[0]).name))
        return

    target = Path(sys.argv[1])

    if not target.exists() or not target.is_dir():
        print(path_error_message(target))
        return

    print(render_tree(target))


if __name__ == "__main__":
    main()
