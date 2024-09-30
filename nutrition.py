'''
Nutrition tracking program
'''

import os


terminal_length = os.get_terminal_size().columns
terminal_height = os.get_terminal_size().lines


def main():
    ''' Main function of the program'''

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

    try:
        selection = int(input("Enter a number: "))
    except ValueError:
        print("Not a number")
        return 0
    else:
        if selection not in range(1, menu_option_amount+1):
            print("Number not an option in the menu")
            return 0
        return selection


if __name__ == '__main__':
    main()
