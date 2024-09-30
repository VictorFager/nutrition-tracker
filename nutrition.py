'''
Nutrition tracking program
'''

import ui
from view import MenuView, ListView

run_program = True


def main():
    ''' Main function of the program'''

    ui.app_name = "Nutrition Tracker"

    ingredients_view = ListView("Ingredients", [])
    meals_view = ListView("Meals", [])
    weight_view = ListView("Weight", [])
    journal_view = ListView("Journal", [])
    statistics_view = ListView("Statistics", [])

    menu_options = [
        ingredients_view,
        meals_view,
        weight_view,
        journal_view,
        statistics_view
    ]

    main_menu_view = MenuView("Main Menu", menu_options)
    current_view = main_menu_view

    while run_program:
        ui.clear_terminal()
        ui.print_top_bar(current_view.title)

        content = current_view.get_content()
        ui.print_view_content(content)

        ui.print_feedback()
        # prompt = "Enter a number or command: "
        # input_range = range(len(content) + 1, 1)
        # commands = current_view.commands
        process_input(current_view)


def process_input(view):

    user_input = input(view.input_prompt).split()

    if (len(user_input) == 1):

        if user_input[0] in view.get_commands():
            # view.process_command(user_input[0])
            return
        elif user_input[0] == "quit":
            quit_program()
            return

        try:
            result = int(user_input[0])

        except ValueError:
            ui.feedback = "Input not valid"
        else:
            if result not in view.get_valid_range():
                ui.feedback = "Number selected out of range"

            # view.process_selection(result)


def quit_program():
    global run_program
    run_program = False


if __name__ == '__main__':
    main()
