# print_chat  [![PyPI](https://img.shields.io/pypi/v/print_chat.svg)](https://pypi.org/project/print_chat/)
Small print tool for implementing chat in the terminal.

## Usage example
```python
from print_chat import print_chat as pc

pct = pc.print_chat()

sender = 'Charls'
pct.set_colors([('Charls', 'green')])

while True:
    post = str(input('> '))

    if post == 'exit':
        break
    else:
        pct.up_on_occupied_rows(len(post) + len(sender) + 2)
        pct.add_message('Charls', post)

pct.close()
```
### For testing the main functionality:
```python
from print_chat import print_chat as pc

pct = pc.print_chat(time=True)

s = 0 # sender iterator
senders = ['Charls', 'Max', 'Karl']
pct.set_colors([
        (senders[0], 'green'),
        (senders[1], 'red'),
        (senders[2], 'yellow')
    ])
pct.set_header('-Test chat-\n-----------') # adding a header to the dialog

while True:
    post = str(input('> '))
    pct.up_on_occupied_rows(len(post) + len(senders[s]) + 2)
    command = post.split(' ')

    if post == 'exit':                  break
    elif command[0] == 'remove':        pct.remove(int(command[1]))
    elif command[0] == 'edit':          pct.edit(int(command[1]), ' '.join(command[2:]))
    elif command[0] == 'reload':        pct.reload(int(command[1]))
    elif command[0] == 'add_skip':      pct.add_skip(int(command[1]), str(' '.join(command[2:])))
    elif command[0] == 'edit_skip':     pct.edit_skip(int(command[1]), ' '.join(command[2:]))
    elif command[0] == 'remove_skip':   pct.remove_skip(int(command[1]))
    elif command[0] == 'add_mark':      pct.add_mark(int(command[1]), str(command[2]))
    elif command[0] == 'edit_mark':     pct.edit_mark(int(command[1]), str(command[2]))
    elif command[0] == 'remove_mark':   pct.remove_mark(int(command[1]))
    elif post == 'cs':                  s = (s+1) % len(senders) # change sender to next
    else:                               pct.add_message(senders[s], post)

pct.close()

```

## Important
### Numbering starts at 1, at the end of the message list

This is not a bug this is a feature

## Create object
default:
```python
from print_chat import print_chat

pct = print_chat.print_chat(time=False)
```
* time - show message sending time

## Method list
* .add_message(sender, text, time='', skip=[], mark=[])
* .add_message_top(sender, text, time='', skip=[], mark=[], prnt=True)
* .reload(number)
* .remove(number)
* .edit(number, text)
* .add_skip(number, text) 
* .edit_skip(number, text)
* .remove_skip(number)
* .add_mark(number, text)
* .edit_mark(number, text)
* .remove_mark(number)
* .close(clr)                       - closes the dialog, with or without screen clearing
* .set_header(string)
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
* .get_messages()
* .get_messages_from(sender)
* .up_on_occupied_rows(len_str)
* .up_on_message(number)
* .up_on_rows(number)
* .clear_row()
* ._clear_screen()
* .get_senders()                    - returns a list of dictionaries

## Installation
```
$ pip install print_chat
```
### or
Repository cloning
```
$ git clone https://github.com/IVIGOR13/print_chat.git
```
Tuning
```
$ pip install termcolor
$ pip install colorama
```
