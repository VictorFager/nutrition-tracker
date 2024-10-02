'''Module for printing the UI to the terminal'''

import os


# Constants containing the size of the terminal
TERMINAL_LENGTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines

# Used as top title in the top bar of the UI
app_name = "Hello World"


def clear_terminal():
    '''Clearing the terminal before updating the UI'''

    os.system('clear')


def print_top_bar(page_title):
    '''Printing the top bar of the UI'''

    print("=" * TERMINAL_LENGTH)
    print(f"{app_name.upper().center(TERMINAL_LENGTH)}")
    print(f"{("-" * len(app_name)).center(TERMINAL_LENGTH)}")
    print(f"{page_title.center(TERMINAL_LENGTH)}")
    print("=" * TERMINAL_LENGTH)


def print_valid_commands(commands):
    '''Printing commands that can be used in the current context'''

    output = "commands:"
    for command in commands:
        output += " " + command + ","
    print(output[:-1])
    print("\n")


def print_view_content(view_content):
    '''Printing main content of the view displayed'''

    for line in view_content:
        print(line)
    print()


def print_feedback(feedback, is_positive):
    '''Print feedback to the user based on previous input'''

    # Add functionality for positive (green) or negative (red) feedback
    print(feedback)
