#!/usr/bin/env python3
"""Program called console.py that contains the entry point of the command
interpreter.
"""
import cmd
import os
from models.base_model import BaseModel
from models import storage

# TODO: refactor delete, create, update, print in storage


class HBNBCommand(cmd.Cmd):
    """Class to manage the console and all the commands built to the project"""
    prompt = '(hbnb)'
    valid_classes = ['BaseModel', 'User', 'Amenity', 'Review', 'State', 'City',
                     'Place']

    ERROR_CLASS_NAME = '** class name missing **'
    ERROR_CLASS = "** class doesn't exist **"
    ERROR_ID = "** instance id missing **"
    ERROR_ID_NOT_FOUND = "** no instance found **"
    ERROR_ATTR = "** attribute name missing **"
    ERROR_ATTR_VALUE = "** value missing **"

    def cmd_cls_args_split(self, command, class_name):
        """Auxiliary function to update the command-line interpreter. This
        function manages and reorders the input of the console to allow the
        functions to work with a formatted command line.
        """
        if command.find("(") != -1:
            attr_name = ''
            value = ''

            args_split = command.split('(')
            command = args_split[0]
            args_split[1] = args_split[1].replace(')', '')
            args_split[1] = args_split[1].replace('"', '')
            args = args_split[1].split(',')
            id_number = args[0].strip(" ")
            if len(args) > 1:
                attr_name = args[1].strip(" ")
            if len(args) > 2:
                value = args[2].strip(" ")
            return '{} {} {} {} "{}"'.format(command, class_name, id_number,
                                             attr_name, value)

        elif class_name in HBNBCommand.valid_classes:
            return "{} {}".format(command, class_name)

    def onecmd(self, line: str) -> bool:
        """Updating the command line interpreter to allow this usage:
        <class name>.<command>() or <class name>.<command>("args")
        """
        line_split = line.split(".")
        # Class.command
        if len(line_split) > 1:
            class_name = line_split[0]
            command = line_split[1].replace('()', '')
            # parameters
            line = self.cmd_cls_args_split(command, class_name)

        return super().onecmd(line)

    def validate_len_args(self, arg):
        """Validates if the command receives the class_name argument"""
        if len(arg) == 0:
            print(HBNBCommand.ERROR_CLASS_NAME)
            return False
        return True

    def validate_class_name(self, arg):
        """Validates if the class_name argument is a valid class"""
        args = arg.split(' ')
        class_name = args[0]
        if class_name not in HBNBCommand.valid_classes:
            print(HBNBCommand.ERROR_CLASS)
            return False
        return class_name

    def validate_id(self, arg):
        """Validates if the command receives an id_number argument """
        args = arg.split(' ')
        if len(args) < 2:
            print(HBNBCommand.ERROR_ID)
            return False
        id_number = args[1]
        return id_number

    def validate_attr(self, arg):
        """Validates if the command receives an attribute argument"""
        args = arg.split(' ')
        if len(args) < 3:
            print(HBNBCommand.ERROR_ATTR)
            return False
        attribute = args[2]
        return attribute

    def validate_attr_value(self, arg):
        """Validates if attribute value exists"""
        args = arg.split(' ')
        if len(args) < 4:
            print(HBNBCommand.ERROR_ATTR_VALUE)
            return False
        attr_value = args[3]
        return attr_value

    def do_EOF(self, arg):
        """ Quits with new line <end of file>
        Usage: Ctrl + d """
        print()
        return True

    def emptyline(self):
        """ None """
        pass

    def do_quit(self, arg):
        """ Quits the console
        Usage: quit """
        return True

    def do_create(self, arg):
        """ Creates new elements
        Usage: create <class_name> or <class_name>.create()
        """
        if not self.validate_len_args(arg):
            return

        class_name = self.validate_class_name(arg)
        if not class_name:
            return

        storage.create(class_name)

    def do_show(self, arg):
        """ Shows an element by id_number
        Usage: show <class_name> <id> or <class_name>.show("<id>")
        """
        if not self.validate_len_args(arg):
            return

        class_name = self.validate_class_name(arg)
        if not class_name:
            return

        id_number = self.validate_id(arg)
        if not id_number:
            return
        objects = storage.all()
        key = "{}.{}".format(class_name, id_number)
        try:
            print(objects[key])
        except:
            print(HBNBCommand.ERROR_ID_NOT_FOUND)

    def do_destroy(self, arg):
        """ Deletes elements in storage
        Usage: destroy <class_name> <id> or <class_name>.destroy("<id>")
        """
        if not self.validate_len_args(arg):
            return

        class_name = self.validate_class_name(arg)
        if not class_name:
            return

        id_number = self.validate_id(arg)
        if not id_number:
            return

        objects = storage.all()
        key = "{}.{}".format(class_name, id_number)

        try:
            del objects[key]
            storage.save()
        except:
            print(HBNBCommand.ERROR_ID_NOT_FOUND)

    def do_all(self, arg):
        """ Prints all elements in storage by class name
         Usage: all or all <class_name> or <class_name>.all()
        """
        class_name = None
        if len(arg) > 0:
            class_name = self.validate_class_name(arg)
            if not class_name:
                return
            # filter data
        storage.print(class_name)

    def do_update(self, arg):
        """ Updates info in storage
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        or <class_name>.update("<id>", "<attribute_name>", "<attribute_value>")
        """
        if not self.validate_len_args(arg):
            return
        class_name = self.validate_class_name(arg)
        if not class_name:
            return
        id_number = self.validate_id(arg)
        if not id_number:
            return

        attribute = self.validate_attr(arg)
        if not attribute:
            return
        attr_value = self.validate_attr_value(arg)
        if not attr_value:
            return
        try:
            objects = storage.all()
            key = "{}.{}".format(class_name, id_number)
            obj = objects[key]
        except:
            print(HBNBCommand.ERROR_ID_NOT_FOUND)
            return

        # obj[attribute] = attr_value
        attr_value = attr_value.strip('"')

        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except:
                pass

        setattr(obj, attribute, attr_value)
        obj.save()

    def do_clear(self, _):
        """Clears the terminal
        Usage: clear
        """
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    def do_count(self, arg):
        """ Retrieves the number of instances of a specific class
        Usage: <class_name>.count()
        """
        if not self.validate_len_args(arg):
            return
        class_name = self.validate_class_name(arg)
        if not class_name:
            return

        class_list = storage.filter_by_class(class_name)
        print(len(class_list))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
