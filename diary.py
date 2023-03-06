#!/usr/bin/env python3

from collections import OrderedDict
import datetime
from peewee import *


db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    # initialize the choice variable
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            # value is a function, __doc__ is the docstring for that function
            print(f'{key}) {value.__doc__}')
        choice = input('Action: ').lower().strip()

        if choice in menu:
            # call function from menu dictionary
            menu[choice]()


def add_entry():
    """Add an entry."""


def view_entries():
    """View previous entries."""


def delete_entry():
    """Delete an entry."""


menu = OrderedDict([
    # add dictionary items as a tuple
    ('a', add_entry),
    ('v', view_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
