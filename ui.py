import os


TERMINAL_LENGTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines

app_name = "Hello World"
feedback = ""


def clear_terminal():

    os.system('clear')


def print_top_bar(page_title):

    print("=" * TERMINAL_LENGTH)
    print(f"{app_name.upper().center(TERMINAL_LENGTH)}")
    print(f"{("-" * len(app_name)).center(TERMINAL_LENGTH)}")
    print(f"{page_title.center(TERMINAL_LENGTH)}")
    print("=" * TERMINAL_LENGTH)
    print("\n")


def print_view_content(view_content):

    for nr, item in enumerate(view_content, 1):
        print(f"{nr}. {item}")

    print()


def print_feedback():
    print(feedback)
