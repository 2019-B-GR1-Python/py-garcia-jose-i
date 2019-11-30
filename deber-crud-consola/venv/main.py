import curses
import os.path
from curses import wrapper
from curses.textpad import Textbox, rectangle

MENU_Y_POSITION = 7
MENU_X_POSITION = 3
CANCEL_FLAG = 0
EXIT_MENU = 0
CLOSE_PROGRAM = 0


def main(stdscr):
    # Black background in each option
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.curs_set(0)
    home_main(stdscr)
    stdscr.refresh()


def home_main(window):
    menu_elements = ["Ingresar Empresa", "Buscar", "Salir"]
    selected_element = 0
    global CANCEL_FLAG
    switch = HomeSwitch()

    home_screen(window, menu_elements, selected_element)

    while CLOSE_PROGRAM != 1:
        if CANCEL_FLAG == 1:
            CANCEL_FLAG = 0

        key = window.getch()

        if key == curses.KEY_UP and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_DOWN and selected_element < len(menu_elements) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch.switch(selected_element, window)

        home_screen(window, menu_elements, selected_element)


def home_screen(window, menu_elements, selected_element):
    y_pos = 0
    window.clear()
    window.addstr(0, 0, banner_to_string("banner.txt"))

    for position, element in enumerate(menu_elements):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + y_pos, MENU_X_POSITION, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(MENU_Y_POSITION + y_pos, MENU_X_POSITION, element)
        y_pos = y_pos + 1

    window.refresh()


class HomeSwitch(object):
    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Register Company
    def fun_0(self, window):
        register_company_main(window)

    # Search option
    def fun_1(self, window):
        search_options_main(window)

    # Quit
    def fun_2(self, window):
        global CLOSE_PROGRAM
        CLOSE_PROGRAM = 1


def register_company_main(window):
    global EXIT_MENU
    global CANCEL_FLAG
    text_box_focus = 1
    buttons = ["Ingresar", "Regresar"]
    selected_element = 0
    company_name_message = register_company_screen(window, buttons, selected_element, "", text_box_focus)
    text_box_focus = 0

    while EXIT_MENU != 1:
        if CANCEL_FLAG == 1:
            break

        key = window.getch()

        if key == curses.KEY_LEFT and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_UP:
            text_box_focus = 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch = RegisterCompanySwitch(company_name_message[:len(company_name_message) - 1])
            switch.switch(selected_element)

        company_name_message = register_company_screen(window, buttons, selected_element, company_name_message,
                                                       text_box_focus)
        text_box_focus = 0

    EXIT_MENU = 0


def register_company_screen(window, buttons, selected_element, company_name="", text_box_focus=0):
    num_lines = 1
    num_columns = 64
    x_pos = 0

    window.clear()
    window.addstr(0, 0, banner_to_string("create-option.txt"))
    window.addstr(MENU_Y_POSITION, MENU_X_POSITION, "Nombre de la Empresa")

    for position, element, in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    edit_win = curses.newwin(num_lines, num_columns, MENU_Y_POSITION + 2, MENU_X_POSITION)
    rectangle(window, MENU_Y_POSITION + 1, MENU_X_POSITION - 1, MENU_Y_POSITION + 3, num_columns + 3)

    window.refresh()

    edit_win.addstr(0, 0, company_name)
    edit_win.refresh()

    box = Textbox(edit_win)

    if text_box_focus == 1:
        curses.curs_set(1)
        box.edit()
        company_name = box.gather()
        curses.curs_set(0)

    return company_name


class RegisterCompanySwitch(object):
    def __init__(self, company_name):
        self.company_name = company_name

    def switch(self, i):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option()

    # Register Company
    def fun_0(self):
        create_company(self.company_name + "\n")
        global EXIT_MENU
        EXIT_MENU = 1

    # Quit
    def fun_1(self):
        global EXIT_MENU
        EXIT_MENU = 1


def search_options_main(window):
    global EXIT_MENU
    global CANCEL_FLAG
    menu_elements = ["Empresa", "Producto", "Regresar"]
    selected_element = 0
    switch = SearchOptionSwitch()
    search_options_screen(window, selected_element, menu_elements)

    while EXIT_MENU != 1:
        if CANCEL_FLAG == 1:
            break

        key = window.getch()

        if key == curses.KEY_UP and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_DOWN and selected_element < len(menu_elements) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch.switch(selected_element, window)

        search_options_screen(window, selected_element, menu_elements)

    EXIT_MENU = 0


def search_options_screen(window, selected_element, menu_elements):
    y_pos = 0
    window.clear()
    window.addstr(0, 0, banner_to_string("search-option.txt"))

    for position, element in enumerate(menu_elements):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + y_pos, MENU_X_POSITION, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(MENU_Y_POSITION + y_pos, MENU_X_POSITION, element)
        y_pos = y_pos + 1

    window.refresh()


class SearchOptionSwitch(object):
    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Search Company Option
    def fun_0(self, window):
        search_company_main(window)

    # Search Product option
    def fun_1(self, window):
        search_product_main(window)

    # Return
    def fun_2(self, window):
        global EXIT_MENU
        EXIT_MENU = 1


def search_company_main(window):
    global EXIT_MENU
    global CANCEL_FLAG
    text_box_focus = 1
    buttons = ["Buscar", "Regresar", "Cancelar"]
    selected_element = 0
    company_name_message = search_company_screen(window, buttons, selected_element, "", text_box_focus)
    text_box_focus = 0

    while EXIT_MENU != 1:
        CANCEL_FLAG = 0
        key = window.getch()

        if key == curses.KEY_LEFT and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_UP:
            text_box_focus = 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch = SearchCompanySwitch(company_name_message[:len(company_name_message) - 1])
            switch.switch(selected_element, window)

        company_name_message = search_company_screen(window, buttons, selected_element, company_name_message,
                                                     text_box_focus)
        text_box_focus = 0

    EXIT_MENU = 0


def search_company_screen(window, buttons, selected_element, company_name="", text_box_focus=0):
    num_lines = 1
    num_columns = 64
    x_pos = 0

    window.clear()
    window.addstr(0, 0, banner_to_string("search-option.txt"))
    window.addstr(MENU_Y_POSITION, MENU_X_POSITION, "Nombre de la Empresa")

    for position, element, in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    edit_win = curses.newwin(num_lines, num_columns, MENU_Y_POSITION + 2, MENU_X_POSITION)
    rectangle(window, MENU_Y_POSITION + 1, MENU_X_POSITION - 1, MENU_Y_POSITION + 3, num_columns + 3)

    window.refresh()

    edit_win.addstr(0, 0, company_name)
    edit_win.refresh()

    box = Textbox(edit_win)

    if text_box_focus == 1:
        curses.curs_set(1)
        box.edit()
        company_name = box.gather()
        curses.curs_set(0)

    return company_name


class SearchCompanySwitch(object):
    def __init__(self, company_name):
        self.company_name = company_name

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Search Company
    def fun_0(self, window):
        company = search_element(".index", self.company_name)
        if company:
            search_company_results_main(window, company[1].strip())
        else:
            search_company_results_main(window, "No se encontró companía")

    # Return
    def fun_1(self, window):
        global EXIT_MENU
        EXIT_MENU = 1

    # Cancel
    def fun_2(self, window):
        global CANCEL_FLAG
        global EXIT_MENU
        CANCEL_FLAG = 1
        EXIT_MENU = 1


def search_product_main(window):
    global EXIT_MENU
    global CANCEL_FLAG
    text_box_focus = 1
    buttons = ["Buscar", "Regresar", "Cancelar"]
    selected_element = 0
    product_name = search_product_screen(window, buttons, selected_element, "", text_box_focus)
    text_box_focus = 0

    while EXIT_MENU != 1:

        CANCEL_FLAG = 0

        key = window.getch()

        if key == curses.KEY_LEFT and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_UP:
            text_box_focus = 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch = SearchProductSwitch(product_name)
            switch.switch(selected_element, window)

        product_name = search_product_screen(window, buttons, selected_element, product_name,
                                             text_box_focus)
        text_box_focus = 0

    EXIT_MENU = 0


def search_product_screen(window, buttons, selected_element, product_name="", text_box_focus=0):
    num_lines = 1
    num_columns = 64
    x_pos = 0

    window.clear()
    window.addstr(0, 0, banner_to_string("search-option.txt"))
    window.addstr(MENU_Y_POSITION, MENU_X_POSITION, "Nombre del producto")

    for position, element, in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    edit_win = curses.newwin(num_lines, num_columns, MENU_Y_POSITION + 2, MENU_X_POSITION)
    rectangle(window, MENU_Y_POSITION + 1, MENU_X_POSITION - 1, MENU_Y_POSITION + 3, num_columns + 3)

    window.refresh()

    edit_win.addstr(0, 0, product_name)
    edit_win.refresh()

    box = Textbox(edit_win)

    if text_box_focus == 1:
        curses.curs_set(1)
        box.edit()
        product_name = box.gather()
        curses.curs_set(0)

    return product_name


class SearchProductSwitch(object):
    def __init__(self, product_name):
        self.product_name = product_name

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Search Product
    def fun_0(self, window):
        result = search_product(self.product_name)
        if result:
            search_product_results_main(window, result[0], result[1][0])
        else:
            search_product_results_main(window, "", "No se encontró producto")

    # Return
    def fun_1(self, window):
        global EXIT_MENU
        EXIT_MENU = 1

    # Cancel
    def fun_2(self, window):
        global CANCEL_FLAG
        global EXIT_MENU
        CANCEL_FLAG = 1
        EXIT_MENU = 1


def search_company_results_main(window, company):
    global EXIT_MENU
    global CANCEL_FLAG
    buttons = ["Ver", "Editar", "Eliminar", "Regresar", "Cancelar"]
    selected_element = 0
    search_company_results_screen(window, selected_element, buttons, company)

    while EXIT_MENU != 1:
        if CANCEL_FLAG == 1:
            break

        key = window.getch()

        if key == curses.KEY_LEFT and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch = SearchCompanyResultsSwitch(company)
            switch.switch(selected_element, window)

        search_company_results_screen(window, selected_element, buttons, company)

    EXIT_MENU = 0


def search_company_results_screen(window, selected_element, buttons, company):
    x_pos = 0
    num_columns = 64
    window.clear()
    window.addstr(0, 0, banner_to_string("search-option.txt"))
    window.addstr(MENU_Y_POSITION, MENU_X_POSITION, "Nombre de la Empresa")
    window.addstr(MENU_Y_POSITION + 2, MENU_X_POSITION, company)
    for position, element in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    rectangle(window, MENU_Y_POSITION + 1, MENU_X_POSITION - 1, MENU_Y_POSITION + 3, num_columns + 3)

    window.refresh()


class SearchCompanyResultsSwitch(object):
    def __init__(self, company_name):
        self.company_name = company_name

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # View products of the Company
    def fun_0(self, window):
        company_details_main(window, self.company_name)

    # Edit Company
    def fun_1(self, window):
        company_name_edit_main(window, self.company_name)

    # Delete Company
    def fun_2(self, window):
        delete_company(self.company_name)
        global EXIT_MENU
        EXIT_MENU = 1

    # Return
    def fun_3(self, window):
        global EXIT_MENU
        EXIT_MENU = 1

    # Cancel
    def fun_4(self, window):
        global CANCEL_FLAG
        global EXIT_MENU
        CANCEL_FLAG = 1
        EXIT_MENU = 1


def search_product_results_main(window, company, product):
    global EXIT_MENU
    global CANCEL_FLAG
    buttons = ["Editar", "Eliminar", "Regresar", "Cancelar"]
    selected_element = 0
    search_product_results_screen(window, selected_element, buttons, product)

    while EXIT_MENU != 1:
        if CANCEL_FLAG == 1:
            break

        key = window.getch()

        if key == curses.KEY_LEFT and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch = SearchProductResultsSwitch(company, product)
            switch.switch(selected_element, window)

        search_product_results_screen(window, selected_element, buttons, product)

    EXIT_MENU = 0


def search_product_results_screen(window, selected_element, buttons, product):
    x_pos = 0
    num_columns = 64
    window.clear()
    window.addstr(0, 0, banner_to_string("search-option.txt"))
    window.addstr(MENU_Y_POSITION, MENU_X_POSITION, "Nombre del producto")
    window.addstr(MENU_Y_POSITION + 2, MENU_X_POSITION, product)

    for position, element in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + 9, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            pass
            window.addstr(MENU_Y_POSITION + 9, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    rectangle(window, MENU_Y_POSITION + 1, MENU_X_POSITION - 1, MENU_Y_POSITION + 3, num_columns + 3)

    window.refresh()


class SearchProductResultsSwitch(object):
    def __init__(self, company_name, product):
        self.company_name = company_name
        self.product = product

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Edit Product
    def fun_0(self, window):
        edit_product_main(window, self.company_name, self.product)

    # Delete Product
    def fun_1(self, window):
        delete_product(self.company_name, self.product)
        global EXIT_MENU
        EXIT_MENU = 1

    # Return
    def fun_2(self, window):
        global EXIT_MENU
        EXIT_MENU = 1

    # Cancel
    def fun_3(self):
        global CANCEL_FLAG
        global EXIT_MENU
        CANCEL_FLAG = 1
        EXIT_MENU = 1


def company_details_main(window, company):
    global EXIT_MENU
    global CANCEL_FLAG
    buttons = ["Nuevo producto", "Regresar"]
    selected_element = 0
    products_list = read_file(company)
    company_details_screen(window, selected_element, buttons, company, products_list)

    while EXIT_MENU != 1:
        if CANCEL_FLAG == 1:
            break

        key = window.getch()

        if key == curses.KEY_LEFT and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch = CompanyDetailsSwitch(company)
            switch.switch(selected_element, window)

        products_list = read_file(company)
        company_details_screen(window, selected_element, buttons, company, products_list)

    EXIT_MENU = 0


def company_details_screen(window, selected_element, buttons, company_name, products_list):
    screen_size = window.getmaxyx()
    y_pos = 0
    x_pos = 0
    title_y_pos = 2
    title_x_pos = 3
    window.clear()
    window.addstr(title_y_pos, title_x_pos, company_name)

    for position, element in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(screen_size[0] - 2, title_x_pos + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(screen_size[0] - 2, title_x_pos + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    y_pos = 0

    for product in products_list:
        product = product.split(",")
        product = [f'{product_attribute} ' for product_attribute in product]
        window.addstr(title_y_pos + 3 + y_pos, title_x_pos, " ".join(product))
        y_pos = y_pos + 1

    rectangle(window, title_y_pos + 2, MENU_X_POSITION - 1, screen_size[0] - 3, screen_size[1] - 2)

    window.refresh()


class CompanyDetailsSwitch(object):
    def __init__(self, message):
        self.message = message

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Register Product
    def fun_0(self, window):
        register_product_main(window, self.message)

    # Return
    def fun_1(self, window):
        global EXIT_MENU
        EXIT_MENU = 1


def company_name_edit_main(window, company):
    global EXIT_MENU
    global CANCEL_FLAG
    text_box_focus = 1
    buttons = ["Editar", "Regresar"]
    selected_element = 0
    company_name_message = company_name_edit_screen(window, buttons, selected_element, company, "", text_box_focus)
    text_box_focus = 0

    while EXIT_MENU != 1:
        if CANCEL_FLAG == 1:
            break

        key = window.getch()

        if key == curses.KEY_LEFT and selected_element > 0:
            selected_element = selected_element - 1
        elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
            selected_element = selected_element + 1
        elif key == curses.KEY_UP:
            text_box_focus = 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            switch = CompanyNameEditSwitch(company, company_name_message)
            switch.switch(selected_element, window)

        company_name_message = company_name_edit_screen(window, buttons, selected_element, company,
                                                        company_name_message, text_box_focus)
        text_box_focus = 0

    EXIT_MENU = 0


def company_name_edit_screen(window, buttons, selected_element, company_title, company_name="", text_box_focus=0):
    num_lines = 1
    num_columns = 64
    x_pos = 0

    window.clear()
    window.addstr(0, 0, banner_to_string("edit-option.txt"))
    window.addstr(MENU_Y_POSITION, MENU_X_POSITION, company_title)

    for position, element, in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(MENU_Y_POSITION + 4, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    edit_win = curses.newwin(num_lines, num_columns, MENU_Y_POSITION + 2, MENU_X_POSITION)
    rectangle(window, MENU_Y_POSITION + 1, MENU_X_POSITION - 1, MENU_Y_POSITION + 3, num_columns + 3)

    window.refresh()

    edit_win.addstr(0, 0, company_name)
    edit_win.refresh()

    box = Textbox(edit_win)

    if text_box_focus == 1:
        curses.curs_set(1)
        box.edit()
        company_name = box.gather()
        company_name = company_name[:len(company_name) - 1]

        curses.curs_set(0)

    return company_name


class CompanyNameEditSwitch(object):
    def __init__(self, company_name, new_company_name):
        self.company_name = company_name
        self.new_company_name = new_company_name

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Edit Name
    def fun_0(self, window):
        edit_company(self.company_name, self.new_company_name)
        global EXIT_MENU
        global  CANCEL_FLAG
        EXIT_MENU = 1
        CANCEL_FLAG = 1

    # Return
    def fun_1(self, window):
        global EXIT_MENU
        EXIT_MENU = 1


def register_product_main(window, company):
    global EXIT_MENU
    global CANCEL_FLAG
    text_box_focus = 0
    text_box_values = ["", "", "", ""]
    buttons = ["Ingresar", "Regresar"]
    selected_element = 0
    register_product_screen(window, text_box_values, buttons, selected_element)

    while EXIT_MENU != 1:

        key = window.getch()

        if key == curses.KEY_UP and text_box_focus > 0:
            text_box_focus = text_box_focus - 1

        elif key == curses.KEY_DOWN and text_box_focus < 3:
            text_box_focus = text_box_focus + 1

        elif key == curses.KEY_DOWN and text_box_focus == 3:
            text_box_focus = text_box_focus + 1
            while True:
                if EXIT_MENU == 1:
                    break

                key = window.getch()

                if key == curses.KEY_LEFT and selected_element > 0:
                    selected_element = selected_element - 1
                elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
                    selected_element = selected_element + 1
                elif key == curses.KEY_UP:
                    text_box_focus = text_box_focus - 1
                    break
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    switch = RegisterProductSwitch(company, text_box_values)
                    switch.switch(selected_element, window)

                text_box_values = register_product_screen(window, text_box_values, buttons, selected_element,
                                                          text_box_focus)

        text_box_values = register_product_screen(window, text_box_values, buttons, selected_element, text_box_focus)

    EXIT_MENU = 0


def register_product_screen(window, text_box_values, buttons, selected_element, text_box_focus=0):
    x_pos = 2
    textbox_x_pos = x_pos + 10
    num_lines = 1
    num_columns = 64

    name_y_pos = 7
    year_y_pos = 10
    price_y_pos = 13
    weight_y_pos = 16

    window.clear()
    window.addstr(0, 0, banner_to_string("create-option.txt"))

    for position, element, in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(weight_y_pos + 2, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(weight_y_pos + 2, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    window.addstr(name_y_pos, 2, "Nombre:")
    window.addstr(year_y_pos, 2, "Año")
    window.addstr(price_y_pos, 2, "Precio")
    window.addstr(weight_y_pos, 2, "Peso")

    edit_win_name = curses.newwin(num_lines, num_columns, name_y_pos, textbox_x_pos)
    edit_win_year = curses.newwin(num_lines, num_columns, year_y_pos, textbox_x_pos)
    edit_win_price = curses.newwin(num_lines, num_columns, price_y_pos, textbox_x_pos)
    edit_win_weight = curses.newwin(num_lines, num_columns, weight_y_pos, textbox_x_pos)

    rectangle(window, name_y_pos - 1, textbox_x_pos - 1, name_y_pos + num_lines, textbox_x_pos + num_columns + 1)
    rectangle(window, year_y_pos - 1, textbox_x_pos - 1, year_y_pos + num_lines, textbox_x_pos + num_columns + 1)
    rectangle(window, price_y_pos - 1, textbox_x_pos - 1, price_y_pos + num_lines, textbox_x_pos + num_columns + 1)
    rectangle(window, weight_y_pos - 1, textbox_x_pos - 1, weight_y_pos + num_lines, textbox_x_pos + num_columns + 1)

    window.refresh()

    edit_win_name.addstr(0, 0, text_box_values[0])
    edit_win_year.addstr(0, 0, text_box_values[1])
    edit_win_price.addstr(0, 0, text_box_values[2])
    edit_win_weight.addstr(0, 0, text_box_values[3])

    edit_win_name.refresh()
    edit_win_year.refresh()
    edit_win_price.refresh()
    edit_win_weight.refresh()

    box_name = Textbox(edit_win_name)
    box_year = Textbox(edit_win_year)
    box_price = Textbox(edit_win_price)
    box_weight = Textbox(edit_win_weight)

    if text_box_focus == 0:
        box_name.edit()
        text_box_values[0] = box_name.gather()
        text_box_values[0] = text_box_values[0][:len(text_box_values[0]) - 1]

    elif text_box_focus == 1:
        box_year.edit()
        text_box_values[1] = box_year.gather()
        text_box_values[1] = text_box_values[1][:len(text_box_values[1]) - 1]

    elif text_box_focus == 2:
        box_price.edit()
        text_box_values[2] = box_price.gather()
        text_box_values[2] = text_box_values[2][:len(text_box_values[2]) - 1]

    elif text_box_focus == 3:
        box_weight.edit()
        text_box_values[3] = box_weight.gather()
        text_box_values[3] = text_box_values[3][:len(text_box_values[3]) - 1]

    window.refresh()

    return text_box_values


class RegisterProductSwitch(object):
    def __init__(self, company_name, product_attributes_list):
        self.company_name = company_name
        self.product_attributes_list = product_attributes_list

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Register Product
    def fun_0(self, window):
        product = ",".join(self.product_attributes_list) + "\n"
        create_product(product, self.company_name)
        global EXIT_MENU
        EXIT_MENU = 1

    # Return
    def fun_1(self, window):
        global EXIT_MENU
        EXIT_MENU = 1


def edit_product_main(window, company, product_name):
    global EXIT_MENU
    global CANCEL_FLAG
    text_box_focus = 0
    text_box_values = ["", "", "", ""]
    buttons = ["Ingresar", "Regresar"]
    selected_element = 0
    edit_product_screen(window, text_box_values, buttons, selected_element)

    while EXIT_MENU != 1:

        key = window.getch()

        if key == curses.KEY_UP and text_box_focus > 0:
            text_box_focus = text_box_focus - 1

        elif key == curses.KEY_DOWN and text_box_focus < 3:
            text_box_focus = text_box_focus + 1

        elif key == curses.KEY_DOWN and text_box_focus == 3:
            text_box_focus = text_box_focus + 1
            while True:
                if EXIT_MENU == 1:
                    break

                key = window.getch()

                if key == curses.KEY_LEFT and selected_element > 0:
                    selected_element = selected_element - 1
                elif key == curses.KEY_RIGHT and selected_element < len(buttons) - 1:
                    selected_element = selected_element + 1
                elif key == curses.KEY_UP:
                    text_box_focus = text_box_focus - 1
                    break
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    switch = EditProductSwitch(company, product_name, text_box_values)
                    switch.switch(selected_element, window)

                text_box_values = edit_product_screen(window, text_box_values, buttons, selected_element,
                                                      text_box_focus)

        text_box_values = edit_product_screen(window, text_box_values, buttons, selected_element, text_box_focus)

    EXIT_MENU = 0


def edit_product_screen(window, text_box_values, buttons, selected_element, text_box_focus=0):
    x_pos = 2
    textbox_x_pos = x_pos + 10
    num_lines = 1
    num_columns = 64

    name_y_pos = 7
    year_y_pos = 10
    price_y_pos = 13
    weight_y_pos = 16

    window.clear()
    window.addstr(0, 0, banner_to_string("edit-option.txt"))

    for position, element, in enumerate(buttons):
        if position == selected_element:
            window.attron(curses.color_pair(1))
            window.addstr(weight_y_pos + 2, MENU_X_POSITION + x_pos, element)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(weight_y_pos + 2, MENU_X_POSITION + x_pos, element)
        x_pos = x_pos + len(buttons[position]) + 2

    window.addstr(name_y_pos, 2, "Nombre:")
    window.addstr(year_y_pos, 2, "Año")
    window.addstr(price_y_pos, 2, "Precio")
    window.addstr(weight_y_pos, 2, "Peso")

    edit_win_name = curses.newwin(num_lines, num_columns, name_y_pos, textbox_x_pos)
    edit_win_year = curses.newwin(num_lines, num_columns, year_y_pos, textbox_x_pos)
    edit_win_price = curses.newwin(num_lines, num_columns, price_y_pos, textbox_x_pos)
    edit_win_weight = curses.newwin(num_lines, num_columns, weight_y_pos, textbox_x_pos)

    rectangle(window, name_y_pos - 1, textbox_x_pos - 1, name_y_pos + num_lines, textbox_x_pos + num_columns + 1)
    rectangle(window, year_y_pos - 1, textbox_x_pos - 1, year_y_pos + num_lines, textbox_x_pos + num_columns + 1)
    rectangle(window, price_y_pos - 1, textbox_x_pos - 1, price_y_pos + num_lines, textbox_x_pos + num_columns + 1)
    rectangle(window, weight_y_pos - 1, textbox_x_pos - 1, weight_y_pos + num_lines, textbox_x_pos + num_columns + 1)

    window.refresh()

    edit_win_name.addstr(0, 0, text_box_values[0])
    edit_win_year.addstr(0, 0, text_box_values[1])
    edit_win_price.addstr(0, 0, text_box_values[2])
    edit_win_weight.addstr(0, 0, text_box_values[3])

    edit_win_name.refresh()
    edit_win_year.refresh()
    edit_win_price.refresh()
    edit_win_weight.refresh()

    box_name = Textbox(edit_win_name)
    box_year = Textbox(edit_win_year)
    box_price = Textbox(edit_win_price)
    box_weight = Textbox(edit_win_weight)

    if text_box_focus == 0:
        box_name.edit()
        text_box_values[0] = box_name.gather()
        text_box_values[0] = text_box_values[0][:len(text_box_values[0]) - 1]

    elif text_box_focus == 1:
        box_year.edit()
        text_box_values[1] = box_year.gather()
        text_box_values[1] = text_box_values[1][:len(text_box_values[1]) - 1]

    elif text_box_focus == 2:
        box_price.edit()
        text_box_values[2] = box_price.gather()
        text_box_values[2] = text_box_values[2][:len(text_box_values[2]) - 1]

    elif text_box_focus == 3:
        box_weight.edit()
        text_box_values[3] = box_weight.gather()
        text_box_values[3] = text_box_values[3][:len(text_box_values[3]) - 1]

    window.refresh()

    return text_box_values


class EditProductSwitch(object):
    def __init__(self, company_name, product_name, product_attributes):
        self.company_name = company_name
        self.product_name = product_name
        self.product_attributes = product_attributes

    def switch(self, i, window):
        option_name = "fun_" + str(i)
        option = getattr(self, option_name, lambda: 'Invalid')
        return option(window)

    # Edit Product
    def fun_0(self, window):
        edit_product(self.company_name, self.product_name, self.product_attributes)
        global EXIT_MENU
        global CANCEL_FLAG
        EXIT_MENU = 1
        CANCEL_FLAG = 1

    # Return
    def fun_1(self, window):
        global EXIT_MENU
        EXIT_MENU = 1


def banner_to_string(name_file):
    path = "./res/" + name_file
    banner_file = open(path, "r")
    return banner_file.read()


def write_company_file(name_file, products=[""]):
    path = "./companies/" + name_file
    company_file = open(path, "w+")
    company_file.writelines(products)
    company_file.close()


def read_company_file(name_file):
    file_exists = 0
    lines = None
    path = "./companies/" + name_file
    if os.path.isfile(path):
        company_file = open(path, "r")
        lines = company_file.readlines()
        file_exists = 1

    return file_exists, lines


def read_file(name_file):
    path = "./companies/" + name_file.strip()
    file = open(path, "r")
    lines = file.readlines()
    return lines


def write_file(name_file, lines=[]):
    path = "./companies/" + name_file.strip()
    file = open(path, "w")
    file.writelines(lines)
    file.close()


def append_file(name_file, lines):
    path = "./companies/" + name_file.strip()
    file = open(path, "a")
    file.write(lines)
    file.close()


def create_company(company_name):
    append_file(".index", company_name)
    write_file(company_name.strip())


def create_product(product, company_name):
    append_file(company_name, product)


def delete_company(company_name):
    success = False
    path = "./companies/" + company_name.strip()
    if os.path.isfile(path):
        os.system("rm " + path)
        success = True
        delete_element(window, ".index", company_name)

    return success


def delete_element(name_file, element):
    lines = read_file(name_file)
    results = search_element(name_file, element)
    if results:
        del lines[results[0]]
        write_file(name_file, lines)
        return True

    return False


def delete_product(company_name, product_name):
    product_attributes = search_product(product_name)
    product = ",".join(product_attributes[1])
    delete_element(company_name, product.strip())


def search_element(name_file, element):
    list_elements = read_file(name_file)
    list_elements_strip = [item.strip() for item in list_elements]
    try:
        return list_elements_strip.index(element), element
    except ValueError:
        pass

    return False


def search_product(product_name):
    list_companies = read_file(".index")

    for company in list_companies:
        products_list = read_file(company.strip())

        for product in products_list:
            product_attributes = product.split(",")
            if product_attributes[0] == product_name.strip():
                return company, product_attributes

    return False


def edit_company(company_name, new_company_name):
    edit_element(".index", company_name, new_company_name)
    company_name = company_name.replace(" ", "\\ ")
    new_company_name = new_company_name.replace(" ", "\\ ")
    os.system("mv ./companies/" + company_name + " ./companies/" + new_company_name)


def edit_element(name_file, element, new_element):
    lines = read_file(name_file)
    results = search_element(name_file, element)
    if results:
        del lines[results[0]]
        lines.insert(results[0], new_element)
        write_file(name_file, lines)
        return True

    return False


def edit_product(company_name, product_name, product):
    lines = read_file(company_name)
    product_attributes = search_product(product_name)
    if product_attributes:
        index = lines.index(",".join(product_attributes[1]))
        del lines[index]
        lines.insert(index, ",".join(product))
        write_file(company_name, lines)
        return True

    return False

wrapper(main)
