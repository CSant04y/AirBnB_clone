# AirBnB_clone
This Object-Oriented project uses concepts from the Python langauge to make a Copy of the AirBnb website.
## Console

### How to use in Interactive Mode

To use the console in interactive mode you must run the file by typing this into your command line.

#### Ex.
```
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```

### How to Use in Non-Interactive Mode

To run the Console in non-nteractive mode you just pipe the command that you want to use.

#### Ex.
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

## Commands and Info

| Command      | Use | Description    |
| :---        |    :-----------   |         :--- |
| `help`      |  `help <command>`       | This shows what a command is used for   |
| `all`   | `all` or `all <class>` |  This displays all the class instances |
| `create`   | `create <class>` | This creates a new class instance  |
| `destroy`   | `destroy <class> <id>` | This delets the class instance |
| `show`   | `<class> <id>` | This command prints instance of class    |
| `update`  | `<class> <id> <attr_name> <attr_val>` | This command updates class attr with value     |
| `quit`   | `quit` | This command Exits the console       |
| `EOF`   | `EOF` | This command Exits the console     |

### Ex. of commands
```
$ ./console.py 
(hbnb) all
[]
(hbnb) create User
f3a6929c-a046-4ae9-90e2-c5d8bde86e86
(hbnb) create City
1f3075d1-9c76-4877-9219-3d1602096df9
(hbnb) all
["[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'updated_at': datetime.datetime(2021, 2, 19, 19, 54, 56, 964160), 'created_at': datetime.datetime(2021, 2, 19, 19, 54, 56, 964160), 'id':
'1f3075d1-9c76-4877-9219-3d1602096df9'}", "[User] (f3a6929c-a046-4ae9-90e2-c5d8bde86e86) {'updated_at': datetime.datetime(2021, 2, 19, 19, 54, 48, 629362), 'created_at': datetime.datetime(2021, 
2, 19, 19, 54, 48, 629362), 'id': 'f3a6929c-a046-4ae9-90e2-c5d8bde86e86'}"]
(hbnb) all City
["[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'updated_at': datetime.datetime(2021, 2, 19, 19, 54, 56, 964160), 'created_at': datetime.datetime(2021, 2, 19, 19, 54, 56, 964160), 'id': 
'1f3075d1-9c76-4877-9219-3d1602096df9'}"]
(hbnb) show User f3a6929c-a046-4ae9-90e2-c5d8bde86e86
[User] (f3a6929c-a046-4ae9-90e2-c5d8bde86e86) {'updated_at': datetime.datetime(2021, 2, 19, 19, 54, 48, 629362), 'created_at': datetime.datetime(2021, 2, 19, 19, 54, 48, 629362), 'id': 
'f3a6929c-a046-4ae9-90e2-c5d8bde86e86'}
(hbnb) destroy User f3a6929c-a046-4ae9-90e2-c5d8bde86e86
(hbnb) all
["[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'updated_at': datetime.datetime(2021, 2, 19, 19, 54, 56, 964160), 'created_at': datetime.datetime(2021, 2, 19, 19, 54, 56, 964160), 'id': 
'1f3075d1-9c76-4877-9219-3d1602096df9'}"]
(hbnb) update City 1f3075d1-9c76-4877-9219-3d1602096df9 name "Los Angeles"
(hbnb) show City 1f3075d1-9c76-4877-9219-3d1602096df9
[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'id': '1f3075d1-9c76-4877-9219-3d1602096df9', 'updated_at': datetime.datetime(2021, 2, 19, 19, 57, 26, 348781), 'name': 'Los Angeles', 
'created_at': datetime.datetime(2021, 2, 19, 19, 54, 56, 964160)}
(hbnb) quit
$
``` 

## Contributers

`Ben Dosch and Carlos Esquivel`
