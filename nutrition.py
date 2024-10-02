'''Nutrition tracking program'''

import ui
from view import View, MenuView, ListView


# Keeps the main loop of the program running while True
run_program = True

# Keeps track of the programs view state
previous_view = None
current_view = None


def main():
    '''Setting up views and runs main loop of the program'''

    ui.app_name = "Nutrition Tracker"

    global current_view
    current_view = setup_views()

    while run_program:
        ui.clear_terminal()
        ui.print_top_bar(current_view.title)
        ui.print_valid_commands(current_view.commands)
        ui.print_view_content(current_view.get_content())
        ui.print_feedback(*current_view.get_feedback())

        user_input = input(current_view.input_prompt)

        # The current_view gets to process user_input first
        result = current_view.process_input(user_input)

        # Now the main program gets to process the result of the 
        # view processing the user_input
        process_result(result)


def setup_views():
    '''Performing setup of essential views'''

    menu_options = [
        ListView("Ingredients", []),
        ListView("Meals", []),
        ListView("Weight", []),
        ListView("Journal", []),
        ListView("Statistics", [])
    ]

    return MenuView("Main Menu", menu_options)


def process_result(result):
    '''Processing results after the current view has processed user input'''

    if isinstance(result, View):
        if current_view == result:
            return
        switch_view(result)
        return

    match result:
        case None:
            pass
        case "quit":
            quit_program()
        case "back":
            if previous_view:
                switch_view(previous_view)
        case _:
            global current_view
            current_view.set_feedback("Something unexpected happened!", False)


def switch_view(new_view):
    '''Switching current_view to new one and updates previous_view'''

    global previous_view, current_view
    previous_view = current_view
    current_view = new_view


def quit_program():
    '''Setting run_program to False canceling the main loop of the program'''

    global run_program
    run_program = False


if __name__ == '__main__':
    main()
