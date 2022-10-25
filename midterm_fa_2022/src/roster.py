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

    def load_roster(self):
        """Load roster from file."""
        if __debug__:
            print('load_roster() method called...')
        try:
            file_path = self._get_file_path()
            with open(file_path, 'r', encoding='UTF-8') as f:
                self.dictionary = json.loads(f.read())
        except OSError:
            print('Problem loading file. Please try again.')


    def save_roster(self):
        """Save roster to file."""
        if __debug__:
            print('save_roster() method called...')
        if self.dictionary != None:
            file_path = self._get_file_path()
            with open(file_path, 'w', encoding='UTF-8') as f:
                f.write(json.dumps(self.dictionary))

    def add_members(self, player_name, age):
        assert self.dictionary != None
        self.dictionary['team_roster'].append({'name': player_name, 'age': int(age)})




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
        self.dictionary['team_roster'] = []
        if __debug__:
            print("New Roster List Initialized")


