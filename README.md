# print_chat
Small print tool for implementing chat in the terminal.

![The Catcher in the Rye chat](https://github.com/IVIGOR13/print_chat/blob/master/screen_chat_in_the_rye.png)

## Usage example
```python
import print_chat as pc

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
# or for testing the main functionality:
```python
import print_chat as pc

pct = pc.print_chat(time=True)

s = 0 # sender iterator
senders = ['Charls', 'Max', 'Karl']
pct.set_colors([
        (senders[0], 'green'),
        (senders[1], 'red'),
        (senders[2], 'yellow')
    ])
pct.add_skip('-Test chat-\n-----------') # adding a header to the dialog

while True:
    post = str(input('> '))
    pct.up_on_occupied_rows(len(post) + len(senders[s]) + 2)
    command = post.split(' ')

    if post == 'exit':                  break
    elif command[0] == 'remove':        pct.remove(int(command[1]))
    elif command[0] == 'edit':          pct.edit(int(command[1]), ' '.join(command[2:]))
    elif command[0] == 'reload':        pct.reload(int(command[1]))
    elif command[0] == 'add_skip':      pct.add_skip(str(command[1]))
    elif command[0] == 'edit_skip':     pct.edit_skip(int(command[1]), ' '.join(command[2:]))
    elif command[0] == 'remove_skip':   pct.remove_skip(int(command[1]))
    elif command[0] == 'cs': s = (s+1) % len(senders) # change sender to next
    else:                               pct.add_message(senders[s], post)

pct.close()
```

## Important
### Numbering starts at 1, at the end of the message list

## Create object
default:
```python
pct = print_chat.print_chat(time=False)
```
* time - show message sending time

## Method list
* .add_message(sender, text)
* .reload(number)
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
