#!/usr/bin/python3
"""[This is the Console]
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """[This si the console that handles commands]

    Args:
        cmd ([type]): [description]
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

    
if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
