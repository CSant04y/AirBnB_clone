#!/usr/bin/python3
"""[This is the Console]
"""
import datetime
import cmd
from models import dict_of_classes, storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        """[Create command makes new instance of class and prints uuid]"""
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
            """[Destroy command to delete an object]
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
        """[All command to print all instances of a class or all instances]
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
        """[Update command based off class name and id]
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

            elif len(args) < 4 or not args[3].startswith('"'):
                print("** value missing **")
                return

            else:
                str_concat = args[3]
                if not args[3].endswith('"'):
                    for i in range(4, len(args)):
                        str_concat += " " + args[i]

                        if args[i].endswith('"'):
                            break
                if not str_concat.endswith('"'):
                    print("** value missing **")
                    return

                str_concat = str_concat.split('"')

                obj = attr_objs[key]
                if args[2] in obj.__dict__:
                    val_type = type(getattr(obj, args[2]))
                    setattr(obj, args[2], val_type(str_concat[1]))
                else:
                    setattr(obj, args[2], str_concat[1])
                obj.updated_at = datetime.datetime.now()
                storage.save()
                return

        print("** no instance found **")

        def count(self, cls_cmd):
            """This gets the count of instances of a class"""
            count = 0
            attr_objs = storage.objects

            for key in attrs_objs:
                class_id = key.split(".")
                if class_id[0] == cls_cmd:
                    count += 1
            print(count)

        def default(self, line):
            """This is the Defualt if the command if not found"""
            class_parsed = line.split('.')
            print(class_parsed)
            if class_parsed[0] in dict_of_classes:
                cmd_mod = class_parsed[1].split('(')
                print(cmd_mod)
                cmd_args = cmd_mod[1].split(')')

                if cmd_mod[0] is "count":
                    self.count(class_parsed[0])

                elif cmd_mod[0] is "all":
                    self.do_all(class_parsed[0])

                elif cmd_mod[0] is "show":
                    show_line = class_parsed[0] + " " + cmd_args[0]
                    self.do_show(show_line)

                elif cmd_mod[0] is "destroy":
                    destroy_line = class_parsed[0] + " " + cmd_args[0]
                    self.do_destroy(destroy_line)

                elif cmd_mod[0] is "update":
                    if False:
                        pass
                    elif (cmd_args[0].find(',') and
                          cmd_args[0].find(',', 38)):
                        comma_1 = cmd_args[0].find(',')
                        comma_2 = cmd_args[0].find(',', comma_1 + 1)
                        update_line = class_parsed[0] + " "
                        + cmd_args[0][:comma_1]
                        + cmd_args[0][comma_1 + 1:comma_2]
                        + cmd_args[0][comma_2 + 1:]

                    self.do_update(update_line)

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
