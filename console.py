#!/usr/bin/python3
"""[This is the Console]
"""
import datetime
import cmd
from models import dict_of_classes, storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """[This is the console that handles commands]

    Args:
        cmd: [Class for command line interpretation]
    """
    def emptyline(self):
        """[This handles an empty line]
        """
        pass

    def do_quit(self, line):
        """[This exits the console]
        """
        return True

    def do_EOF(self, line):
        """[EOF command to exit the console]
        """
        return True

    def do_create(self, line):
        """Create command makes new instance of class and prints uuid"""
        if not line or line is None:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in dict_of_classes:
            print("** class doesn't exist **")
            return

        cls = dict_of_classes[args[0]]
        """insert loop to go through key, value pair to put in a dictonary"""
        obj = cls()
        print(obj.id)
        storage.save()

    def do_show(self, line):
        """[show command prints the str representaiton of an object]
        """
        if not line or line is None:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in dict_of_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]

        attr_objs = storage.objects

        if key in attr_objs:
            class_id = key.split(".")
            print("[{}] ({}) {}".format(class_id[0],
                                        class_id[1],
                                        attr_objs[key].__dict__))
        else:
            print("** no instance found **")

    def do_destroy(self, line):
            """[destroy command to delete an object]
            """
            if not line or line is None:
                print("** class name missing **")
                return

            args = line.split()

            if args[0] not in dict_of_classes:
                print("** class doesn't exist **")
                return

            if len(args) < 2:
                print("** instance id missing **")
                return

            key = args[0] + "." + args[1]

            attr_objs = storage.objects

            if key in attr_objs:
                taco = attr_objs.pop(key)
                storage.save()

            else:
                print("** no instance found **")

    def do_all(self, line):
        """[all command to print all instances of a class or all instances]
        """
        list_return = []

        attr_objs = storage.objects

        if not line or line is None:
            for key in attr_objs:
                class_id = key.split(".")
                list_return.append("[{}] ({}) {}".format(class_id[0],
                                        class_id[1], attr_objs[key].__dict__))

            print(list_return)
            return

        args = line.split()

        if args[0] not in dict_of_classes:
            print("** class doesn't exist **")
            return

        for key in attr_objs:
            class_id = key.split(".")
            if class_id[0] == args[0]:
                list_return.append("[{}] ({}) {}".format(class_id[0],
                class_id[1], attr_objs[key].__dict__))

        print(list_return)

    def do_update(self, line):
        """[update command based off class name and id]
        """
        if not line or line is None:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in dict_of_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]

        attr_objs = storage.objects

        if key in attr_objs:
            if len(args) < 3:
                print("** attribute name missing **")
                return

            elif len(args) < 4:
                print("** value missing **")
                return

            else:
                obj = attr_objs[key]
                if args[2] in obj.__dict__:
                    val_type = type(getattr(obj, args[2]))
                    setattr(obj, args[2], val_type(args[3]))
                else:
                    setattr(obj, args[2], args[3])
                obj.updated_at = datetime.datetime.now()
                storage.save()
                return

        print("** no instance found **")


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
