'''Module containing classes for different views in the program'''


class View:
    '''Base class for views '''

    def __init__(self, title):
        # Representing a page title
        self.title = title
        # Feedback based on most recent user_input
        self._feedback = ""
        # Tells if feedback is positive or negative
        self._positive_feedback = True
        # Used as prompt to tell the user what to input
        self.input_prompt = "=> "
        # Commands that can be used in this view
        self.commands = ["quit", "back"]

    def set_feedback(self, message, is_positive):
        '''Setter for feedback attributes'''
        self._feedback = message
        self._positive_feedback = is_positive

    def get_feedback(self):
        '''Getter for feedback attributes'''
        return (self._feedback, self._positive_feedback)

    def get_content(self):
        '''Returning a list with strings that make up the views content'''
        return [self.title]

    def process_input(self, user_input):
        '''Processing the user input

        Make changes based on user_input and return a result (None, a View or
        a string representing a command) for the main program to process
        '''
        if user_input not in self.commands:
            self.set_feedback("INVALID COMMAND - Command not found", False)
            return None
        return user_input


class MenuView(View):
    '''Subclass of View representing a menu'''

    def __init__(self, title, menu_options):
        super().__init__(title)
        self.input_prompt = "Enter a number or command: "
        self.commands = ["quit"]
        # A list containing other Views which make up the menu options
        self.menu_options = menu_options

    def get_content(self):
        '''Returning a list with strings that make up the views content

        The content is a list of numbered menu options based on the view titles
        '''
        content = []
        for nr, option in enumerate(self.menu_options, 1):
            content.append(f"{nr}. {option.title}")
        return content

    def get_valid_range(self):
        '''Returns a range only containing the numbers of the menu options'''
        return range(1, len(self.menu_options) + 1)

    def process_input(self, user_input):
        '''Processing the user input

        Make changes based on user_input and return a result (None, a View or
        a string representing a command) for the main program to process
        '''

        # This view has no commands requiring more than one argument
        if len(user_input.split()) >= 2:
            self.set_feedback("INVALID COMMAND - Too many arguments", False)
            return None

        # This view needs exactly one argument
        if not user_input:
            self.set_feedback("INVALID INPUT - No input", False)
            return None

        # All valid commands for this view are handled by the main program
        # so we return them as the result
        if user_input in self.commands:
            return user_input

        # Checking if input is an integer argument
        try:
            selection = int(user_input)

        except ValueError:
            # If the argument cannot be converted to an integer then we know
            # it was an invalid command
            self.set_feedback("INVALID COMMAND - Command not found", False)
            return None
        else:
            if selection not in self.get_valid_range():
                self.set_feedback("INVALID INPUT - Selection out of range",
                                  False)
                return None

            # Returning a View for the main program to switch to
            return self.menu_options[selection - 1]


class ListView(View):
    '''Subclass of View representing a list of content

    The view has functionality for searching the list, adding new items,
    editing items, deleting items, navigating up and down the list using pages,
    and showing parts of the list using categories
    '''

    def __init__(self, title, item_list):
        super().__init__(title)
        # List of items making up the content for the view
        self.item_list = item_list

    def get_content(self):
        '''Returning a list with strings that make up the views content

        The content is a list of numbered list items
        '''
        return self.item_list


class EditView(View):
    '''Subclass of View representing an item that can be edited

    The view has functionality for adding information to fields in order when
    adding a new item, selecting fields to edit, jumping to the next or
    previous field, and canceling or okaying the editing of the item
    '''

    def __init__(self, title):
        super().__init__(title)
