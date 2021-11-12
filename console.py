#!/usr/bin/python3
"""
This module contains a class that defines
a console for testing the file storage and classes
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines a command interpreter
    """

    prompt = "(hbnb)"

    def do_quit(self, *arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, *arg):
        """EXIT command to exit the program at the EOF"""
        return True

    def emptyline(self):
        """empty line + ENTER doesn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
