# print_chat
Small print tool for implementing chat in the terminal.

![The Catcher in the Rye chat](https://github.com/IVIGOR13/print_chat/blob/master/screen_chat_in_the_rye.png)

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
# or for testing the main functionality:
```python
from print_chat import print_chat

pc = print_chat(time=True)

s = 0 # sender iterator
senders = ['Charls', 'Max', 'Karl']
pc.set_colors([
        (senders[0], 'green'),
        (senders[1], 'red'),
        (senders[2], 'yellow')
    ])
pc.add_skip('-Test chat-\n-----------') # adding a header to the dialog

while True:
    post = str(input('> '))
    pc.up_on_occupied_rows(len(post) + len(senders[s]) + 2)
    command = post.split(' ')

    if post == 'exit':                  break
    elif command[0] == 'remove':        pc.remove(int(command[1]))
    elif command[0] == 'edit':          pc.edit(int(command[1]), ' '.join(command[2:]))
    elif command[0] == 'reload':        pc.reload(int(command[1]))
    elif command[0] == 'load':          pc.load_in_skip(int(command[1]))
    elif command[0] == 'add_skip':      pc.add_skip(str(command[1]))
    elif command[0] == 'edit_skip':     pc.edit_skip(int(command[1]), ' '.join(command[2:]))
    elif command[0] == 'remove_skip':   pc.remove_skip(int(command[1]))
    elif command[0] == 'cs': s = (s+1) % len(senders) # change sender to next
    else:                               pc.add_message(senders[s], post)

pc.close()
```

## Important
### Numbering starts at 1, at the end of the message list

## Create object
default:
```python
pc = print_chat(file_name='', time=False)
```
* file_name - the name of the message history file, if not specified, the file is not created
* time - show message sending time

## Method list
* .add_message(sender, text)
* .reload(number)
* .load(number)
* .remove(number)
* .edit(number, text)
* .add_skip(text) 
* .edit_skip(number, text)
* .remove_skip(number)
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
* .get_messages()
* .get_messages_from(sender)
* .up_on_occupied_rows(len_str)
* .up_on_message(number)
* .up_on_rows(number)
* .clear_row()
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
