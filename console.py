#!/usr/bin/python3
"""
This module contains a class that defines
a console for testing the file storage and classes
"""
from models import storage
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

    def do_create(self, arg):
        """Creates a class instance from class name supplied"""

        dict = storage.dict()
        if not arg:
            print("** class name missing **")
            return
        elif arg not in dict:
            print("** class doesn't exist **")
            return
        else:
            instance = dict[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""

        dict = storage.dict()
        all_objects = storage.all()
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in dict:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = "{}.{}".format(args[0], args[1])
                for key, value in all_objects.items():
                    if key == obj_id:
                        print(all_objects[key])
                        return
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""

        dict = storage.dict()
        all_objects = storage.all()
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in dict:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = "{}.{}".format(args[0], args[1])
                for key, value in all_objects.items():
                    if key == obj_id:
                        del all_objects[key]
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all."""

        dict = storage.dict()
        all_objects = storage.all()
        list_all = []
        if not arg:
            for key, value in all_objects.items():
                list_all.append(value.__str__())
        else:
            args = arg.split()
            if args[0] not in dict:
                print("** class doesn't exist **")
                return
            else:
                for key, value in all_objects.items():
                    if args[0] == value.__class__.__name__:
                        list_all.append(value.__str__())
        print(list_all)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute.
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""

        dict = storage.dict()
        all_objects = storage.all()
        if not arg:
            print("** class name missing **")
            return
        else:
            args = arg.split()
            if args[0] not in dict:
                print("** class doesn't exist **")
            elif not args[1]:
                print("** class name missing **")
            elif args[0] + "." + args[1] not in all_objects.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj_id = "{}.{}".format(args[0], args[1])
                for key, value in all_objects.items():
                    if key == obj_id:
                        attr_value = args[3]
                        if args[2] in value.__dict__:
                            attr_type = type(value.__dict__[args[2]])
                            print("---")
                            attr_value = attr_type(args[3])
                            print(attr_value)
                        setattr(value, args[2], attr_value)
                        value.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
