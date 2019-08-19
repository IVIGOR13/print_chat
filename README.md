# print_chat
Small print tool for implementing chat in the terminal.

## Usage example
```python
from print_chat import print_chat

pc = print_chat()

sender = 'Charls'
pc.set_colors([('Charls', 'green')])

while True:
    post = str(input('> '))

    if post == 'exit':
        break
    else:
        pc.up_on_occupied_rows(len(post) + len(sender) + 2)
        pc.add_message('Charls', post)

pc.close()
```

## Important
### Numbering starts at 1, at the end of the message list

## Create object
default:
```python
pc = print_chat(clr=True, file_name='')
```
* clr - clear or not screen before output
* file_name - the name of the message history file, if not specified, the file is not created

## Method list
* .add_message(sender, text)
* .reload(number)
* .load(number)
* .remove(number)
* .edit(number, text)
* .add_skip(text) 
* .edit_skip(number, text)
* .close(clr)                       - closes the dialog, with or without screen clearing
* .set_colors(colors)               - takes a list [[sender, color],..]
   colors list:
     * grey
     * red
     * green
     * yellow
     * blue
     * magenta
     * cyan
     * white
* .get_num_messages()               - returns the number of messages
* .get_messages(start, end)         - returns a slice of messages
* .get_messages()
* .up_on_occupied_rows(len_str)
* .up_on_message(number)
* .up_on_rows(number)
* .get_senders()                    - returns a list of dictionaries
* .get_skips()

## Installation
Repository cloning
```
$ git clone https://github.com/IVIGOR13/print_chat.git
```
Tuning
```
$ pip install termcolor
$ pip install colorama
```
