import os
import sys
import time
import base64
import threading
from colorama import Fore, Style, init

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def progress_loader(duration=5):
    clear_terminal()
    print(Fore.CYAN + Style.BRIGHT + "Loading, please wait...\n")
    length = 40
    interval = duration / length

    for i in range(length + 1):
        bar = '█' * i + '-' * (length - i)
        percent = (i / length) * 100
        print(f"\r[{Fore.GREEN}{bar}{Fore.RESET}] {percent:6.2f}%", end='', flush=True)
        time.sleep(interval)
    print("\n")

def animated_banner(duration=5):
    banner_text = [
        "██████╗ ██╗   ██╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗",
        "██╔══██╗██║   ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝",
        "██████╔╝██║   ██║█████╗  ██║     ██║   ██║██████╔╝█████╗  ",
        "██╔═══╝ ██║   ██║██╔══╝  ██║     ██║   ██║██╔═══╝ ██╔══╝  ",
        "██║     ╚██████╔╝███████╗╚██████╗╚██████╔╝██║     ███████╗",
        "╚═╝      ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝",
        "",
        "       Simple Python Obfuscator Tool by SHAYAN",
        "           Telegram Channel: @EroHack0"
    ]
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
    end_time = time.time() + duration

    while time.time() < end_time:
        for color in colors:
            if time.time() > end_time:
                break
            clear_terminal()
            for line in banner_text:
                print(color + Style.BRIGHT + line)
            time.sleep(0.25)

    # نمایش نهایی بنر ثابت
    clear_terminal()
    for line in banner_text:
        print(Fore.CYAN + Style.BRIGHT + line)
    print()

def show_help():
    clear_terminal()
    print(Fore.CYAN + Style.BRIGHT + """
Simple Python Obfuscator Tool

Usage:
  python obfuscator.py [options]

Options:
  -h          Show this help message and exit

Description:
  This tool obfuscates your Python scripts by encoding the source code in base64,
  wrapping it in an exec() call. This hides your source code to some extent.

How to use:
  Run without arguments, then provide input and output file paths interactively.

Author: SHAYAN
Telegram Channel: @EroHack0
    """)
    sys.exit()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        show_help()

    progress_loader(duration=5)
    animated_banner(duration=5)

    input_path = input(Fore.YELLOW + "Enter the exact path of the Python file to obfuscate > ").strip()
    output_path = input(Fore.GREEN + "Enter the output file name (e.g., obfuscated.py) > ").strip()
    if not output_path.endswith(".py"):
        output_path += ".py"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            code = f.read()
    except Exception as e:
        print(Fore.RED + f"Error reading input file: {e}")
        return

    encoded = base64.b64encode(code.encode("utf-8")).decode("utf-8")
    wrapper = f"""# Auto-generated obfuscated file
import base64
exec(base64.b64decode('{encoded}').decode('utf-8'))
"""

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(wrapper)
    except Exception as e:
        print(Fore.RED + f"Error writing output file: {e}")
        return

    print(Fore.GREEN + f"\nObfuscation successful! Output saved to: {output_path}")

if __name__ == "__main__":
    main()
