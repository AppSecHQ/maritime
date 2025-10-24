#!/usr/bin/env python3
"""
Maritime Demo Application
A simple hello world application with external dependencies
"""

import requests
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init()

def main():
    """Main application entry point"""
    print(f"{Fore.CYAN}=" * 50)
    print(f"{Fore.GREEN}Hello World from Maritime Demo!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}=" * 50)

    # Display current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.YELLOW}Current time: {current_time}{Style.RESET_ALL}")

    # Make a simple API call to demonstrate requests library
    try:
        print(f"\n{Fore.BLUE}Fetching a fun fact...{Style.RESET_ALL}")
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en", timeout=5)
        if response.status_code == 200:
            fact = response.json().get("text", "No fact available")
            print(f"{Fore.MAGENTA}Fun fact: {fact}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Could not fetch fun fact: {e}{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}Application completed successfully!{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
