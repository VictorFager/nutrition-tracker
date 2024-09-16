'''
Nutrition tracking program
'''

import os


terminal_length = os.get_terminal_size().columns
terminal_height = os.get_terminal_size().lines

# LOOP
# print top bar
# print menu and cursor
# wait for input


def main():
    menu_selection = 1

    start_menu_options = ["Add", "Print", "Delete", "Quit"]

    while menu_selection != 4:
        print_top_bar()
        print_menu(start_menu_options, menu_selection)
        menu_selection = input_menu_selection(len(start_menu_options))


def print_top_bar():
    os.system('clear')
    print("=" * terminal_length)
    print(f"{"Nutrition Tracker".center(terminal_length)}")
    print("=" * terminal_length)
    print("\n")


def print_menu(menu_options, cursor_pos, menu_title="MENU"):
    print(f"{menu_title}\n")
    for nr, item in enumerate(menu_options, 1):
        print(f"{"*" if nr == cursor_pos else " "} {nr}. {item}")
    print()


def input_menu_selection(menu_option_amount):
    # MORE WORK IS NEEDED
    # kanske testa en try except?
    selection = int(input("Enter a number: "))
    return selection


if __name__ == '__main__':
    main()
