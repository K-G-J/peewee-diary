#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import os
import sys

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


def clear():
    # clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
    """Show the menu"""
    # initialize the choice variable
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            # value is a function, __doc__ is the docstring for that function
            print(f'{key}) {value.__doc__}')
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            # call function from menu dictionary
            menu[choice]()


def add_entry():
    """Add an entry."""
    print('Enter your entry. Press ctrl+d when finished.')
    # use stdin the capture everything the user writes
    data = sys.stdin.read().strip()

    if data:
        if input('Save enter? [Y/n]').lower() != 'n':
            Entry.create(content=data)
            print('Saved successfully!')


def view_entries(search_query=None):
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        # filter entries for search query is passed in
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(f'{timestamp}\n{"=" * len(timestamp)}\n{entry.content}\n\n\n{"=" * len(timestamp)}\nn) next entry\nd) delete entry\nq) return to main menu')

        next_action = input('Action: [N/d/q]  ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
            print('Entry deleted!')


def search_entries():
    """Search entries for a string."""
    view_entries(input('Search query:  '))


def delete_entry(entry):
    """Delete an entry."""
    if input('Are you sure? [y/N]').lower() == 'y':
        entry.delete_instance()


menu = OrderedDict([
    # add dictionary items as a tuple
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
