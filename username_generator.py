"""
Username Generator Script

This script generates random usernames composed of lowercase letters and digits.
You can customize the length of the username and the number of usernames to generate
using command-line arguments.

Usage:
    python username_generator.py --length 8 --number 3

If no parameters are provided, it will generate 1 username with 5 characters.
"""

import random
import argparse

def generate_username(length=5):
    """
    Generate a random username with the specified length.

    Parameters:
        length (int): The desired length of the username (default is 5).

    Returns:
        str: A randomly generated username consisting of lowercase letters and digits.
    """
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    """
    Parse command-line arguments and generate usernames.
    """
    parser = argparse.ArgumentParser(description="Random Username Generator")
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=5,
        help="Length of each username (default: 5)"
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Number of usernames to generate (default: 1)"
    )
    args = parser.parse_args()

    for _ in range(args.number):
        print(generate_username(args.length))

if __name__ == "__main__":
    main()
