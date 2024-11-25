import hashlib
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(strip=False)

# Define the green bold string
context = f"{Style.BRIGHT}{Fore.GREEN}Press Return to Continue or type 'exit' to quit{Style.RESET_ALL}"

def get_sha256_hash(input_text):
    hash_function = hashlib.sha256()
    hash_function.update(input_text.encode('utf-8'))
    return hash_function.hexdigest()

def main():
    print("SHA-256 Hash Generator")
    text = input("Enter text to hash: ")
    pancake = get_sha256_hash(text)
    print(f"{pancake}")

    # Write the hash to a file
    with open("/Users/mbymax/Documents/code/avf/out/texthash", "a") as f:
        f.write(f"{pancake}\n")

    # Show the message and wait for the user to press Enter or exit
    while True:
        print()  # Adds a newline for spacing
        user_input = input(context).strip().lower()
        if user_input == "exit":
            print(f"{Fore.YELLOW}Exiting... Goodbye!{Style.RESET_ALL}")
            return  # Exits the main function
        elif user_input == "":
            print(f"{Fore.BLUE}Continuing...{Style.RESET_ALL}")
            return  # Continue or allow another run
        else:
            print(f"{Fore.RED}Invalid input. Press Return to continue or type 'exit' to quit.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()