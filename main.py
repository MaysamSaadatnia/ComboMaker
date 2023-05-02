import random
import string
import sys
import time
from tqdm import tqdm
from termcolor import colored


def email_generator(keywords, domain):
    # Generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

    # Combine the keywords and username
    email = f"{keywords}-{username}@{domain}"

    return email

def password_generator(keywords):
    # Generate a random password
    password = ''.join(random.choice(keywords) for _ in range(12))

    return password

def email_generator_menu():
    while True:
        # Define the text art for the title
        title = colored("███╗░░░███╗░█████╗░██████╗░░█████╗░██╗███╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░\n"
                        "████╗░████║██╔══██╗╚════██╗██╔══██╗██║████╗░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░\n"
                        "██╔████╔██║███████║░█████╔╝██║░░██║██║██╔██╗██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░\n"
                        "██║╚██╔╝██║██╔══██║░╚═══██╗██║░░██║██║██║╚████║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░\n"
                        "██║░╚═╝░██║██║░░██║██████╔╝╚█████╔╝██║██║░╚███║  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗\n"
                        "╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝", "magenta")

        # Print the title
        print(title)

        # Print the menu options
        print(colored("Here are your options:", "cyan"))
        print(colored("1. Generate email and password pairs", "green"))
        print(colored("2. Quit", "green"))

        # Get the user's choice
        choice = input(colored("What would you like to do? ", "cyan"))

        if choice == '1':
            # Get the user's input
            keywords = input(colored("Enter the keywords separated by hyphens: ", "cyan"))
            domain = input(colored("Enter the domain name: ", "cyan"))
            password_keywords = input(colored("Enter the password keywords separated by hyphens: ", "cyan"))
            num_emails = int(input(colored("Enter the number of email and password pairs to generate: ", "cyan")))

            # Generate the email and password pairs
            print(colored("Generating email and password pairs...", "purple"))
            for i in tqdm(range(num_emails)):
                email = email_generator(keywords, domain)
                password = password_generator(password_keywords)
                print(f"{email}:{password}")

                # Pause before generating the next pair
                time.sleep(0.5)
            print(colored("Done!", "green"))

        elif choice == '2':
            sys.exit()
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == "__main__":
    email_generator_menu()