import sys
from pathlib import Path
from colorama import Fore, Style, just_fix_windows_console

def print_directory_tree(directory: Path, prefix: str = ""):
    try:
        items = list(directory.iterdir())
    except PermissionError:
        print(f"{prefix}{Fore.RED}Permission denied{Style.RESET_ALL}")
        return
    except OSError as e:
        print(f"{prefix}{Fore.RED}Cannot read directory: {e}{Style.RESET_ALL}")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1

        connector = "┗━━ " if is_last else "┣━━ "
        extension = "    " if is_last else "┃   "

        if item.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")

            # Recursive traversal of the subdirectory
            if not item.is_symlink():
                print_directory_tree(item, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


def main():
    just_fix_windows_console()

    if len(sys.argv) != 2:
        print(f"Usage: python {Path(sys.argv[0]).name} <directory_path>")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Path does not exist: {path}{Style.RESET_ALL}")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Path is not a directory: {path}{Style.RESET_ALL}")
        return

    print(f"{Fore.BLUE}📦 {path}{Style.RESET_ALL}")
    print_directory_tree(path)


if __name__ == "__main__":
    main()