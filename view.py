class View:

    def __init__(self, title):
        self.title = title
        self.input_prompt = "=> "
        self.commands = {}

    def get_content(self):
        return [self.title]

    def get_commands(self):
        return self.commands.keys()

    def process_command(self):
        pass

    def process_selection(self):
        pass


class MenuView(View):

    def __init__(self, title, menu_options):
        super().__init__(title)
        self.input_prompt = "Enter a number or command: "
        self.menu_options = menu_options

    def get_content(self):
        return [option.title for option in self.menu_options]

    def get_valid_range(self):
        return range(1, len(self.menu_options) + 1)


class ListView(View):

    def __init__(self, title, item_list):
        super().__init__(title)
        self.item_list = item_list

    def get_content(self):
        return self.item_list


class EditView(View):

    def __init__(self, title):
        super().__init__(title)
