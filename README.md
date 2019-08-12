# print_chat
Small print tool for implementing chat in the terminal.

## Usage example
```python
from print_chat import print_chat

pc = print_chat()

pc.set_colors([('Charls', 'green')])

while True:
    post = str(input('> '))

    if post == 'exit':
        break
    else:
        print('\x1b[A', end='')  # print carriage lift
        pc.add_message('Charls', post)

pc.close()
```

## Important
### Worth explaining: numbering starts at 1, at the end of the message list

## Method list
* .add_message(sender, text)
* .reload(number)
* .load(number)
* .remove(number)
* .edit(number, text)
* .set_colors(colors)        - takes a list [[sender, color],..]
   colors list:
     * grey
     * red
     * green
     * yellow
     * blue
     * magenta
     * cyan
     * white
* .get_num_messages()         - returns the number of messages
* .get_messages(start, end)   - returns a slice of messages

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
