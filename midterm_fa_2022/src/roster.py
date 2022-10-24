"""Implements Team Roster Operations"""

import json
from datetime import date



class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        """Initialize Roster object"""
        self._initialize_roster_dictionary()

        pass

    def new_roster(self):
        """Initialize new dictionary to store inventory data."""
        if (self.dictionary != None) and (bool(self.dictionary)):
            user_input = input("Save current inventory? (y/n): ")
            match user_input.lower():
                case 'y':
                    self.save_roster()
                    self._initialize_roster_dictionary()
                case 'n':
                    self._initialize_roster_dictionary()
                case _:
                    self._initialize_roster_dictionary()
        else:
            self._initialize_roster_dictionary()


    def _get_file_path(self):
        """Get flle path from user."""
        f_path = input("Please enter path and filename: ")
        return f_path

    def _initialize_roster_dictionary(self):
        if __debug__:
            print("Initializing Roster List...")
        self.dictionary = {}
        self.dictionary['type'] = 'Roster List'
        self.dictionary['date'] = date.today().isoformat()
        self.dictionary['items'] = []
        if __debug__:
            print("New Roster List Initialized")


