"""Represents Application user interface """

from home_inventory import HomeInventory
from subprocess import call
import os

class InventoryApp():

    def __init__(self):
        """IInitialize objects defined below"""
        #Constants
        self.NEW_INVENTORY = '1'
        self.LOAD_INVENTORY = '2'
        self.LIST_INVENTORY = '3'
        self.ADD_ITEMS = '4'
        self.SAVE_INVENTORY = '5'
        self.EXIT = '7'
        #fields
        self.menu_choice = 1
        self.keep_going = True
        self.home_inventory = HomeInventory()
        pass

    def clear_screen(self):
        _ = call('clear' if  os.name == 'posix' else 'cls')

    def display_menu(self):
        """This displays the menu"""
        print()
        print('\tHome Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. Load Inventory')
        print('\t\t3. List Inventory')
        print('\t\t4. Add Items')
        print('\t\t5. Save Inventory')
        print('\t\t7. Exit')
        print()

    def process_menu_choice(self):
        """This section processes menu choices and execute corresponding methods"""
        menu_choice = input('Select the menu item numeber: ')
        if __debug__:
            print(f'You entered: {self.menu_choice}')
        match menu_choice:
            case self.NEW_INVENTORY:
                self.new_inventory()
            case self.LOAD_INVENTORY:
                self.load_inventory()
            case self.LIST_INVENTORY:
                self.list_inventory()
            case self.ADD_ITEMS:
                self.add_items()
            case self.SAVE_INVENTORY:
                self.save_inventory()
            case self.EXIT:
                if __debug__:
                    print('Goodbey!')
                self.keep_going = False
                self.clear_screen
            case _:
                print('Invalid Menu Choice!\t Try again')

    def new_inventory(self):
        """This is to create new inventory"""
        if __debug__:
            print('new_inventory() method called...')
        self.home_inventory.new_inventory()

    def load_inventory(self):
        """This load inventory from file"""
        if __debug__:
            print('load_inventory() method called...')
        self.home_inventory.load_inventory()

    def list_inventory(self):
        """This list inventory"""
        if __debug__:
            print('list_inventory() method called...')
        self.clear_screen()
        self.home_inventory.list_inventory()
        input('Press any key to continue...')
        self.clear_screen()

    def save_inventory(self):
        """This is to save inventory to file"""
        self.home_inventory.save_inventory()

    def add_items(self):
        """This is to add items to inventory"""
        keep_going = 'y'
        while keep_going[0] == 'y':
            item_name = input('Item Name: ')
            item_count = input('Item Count: ')
            self.home_inventory.add_item(item_name, item_count)
            keep_going = input('Add another? (y/n): ')

    #Program prompt
    def start_program(self):
        """This section is to start the application"""
        #clear Screen
        self.clear_screen()
        while self.keep_going:
            self.display_menu()
            self.process_menu_choice()