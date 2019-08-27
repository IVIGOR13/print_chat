#
# Author: Igor Ivanov
# 2019
#
import time
import os
from termcolor import colored
import colorama

colorama.init()

class print_chat:

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def close(self, clr=False):
        self.MESSAGES.clear()
        self.senders.clear()
        self.skips.clear()
        print('\x1b[A\r', end='')
        if clr:
            self._clear_screen()


    def up_on_rows(self, number):
        print('\r' + ' ' * os.get_terminal_size().columns + '\r', end='')
        print(('\x1b[A\r' + ' ' * os.get_terminal_size().columns + '\r') * number, end='')


    def up_on_message(self, number):
        n = self.__get_lines(number)
        self.up_on_rows(n)


    def up_on_occupied_rows(self, len_str):
        lines = ((len_str-1) // os.get_terminal_size().columns) + 1
        self.up_on_rows(lines)


    def down_on_rows(self, number):
        print('\r' + ' ' * os.get_terminal_size().columns + '\r', end='')
        print(('\n\r' + ' ' * os.get_terminal_size().columns + '\r') * number, end='')


    def get_num_messages(self):
        return(len(self.MESSAGES))


    def get_messages_from(self, sender):
        out = []
        for i in self.MESSAGES:
            if i['sender'] == sender:
                out.append(i)
        return out


    def get_messages(self):
        return self.MESSAGES


    def get_senders(self):
        return self.senders


    def get_skips(self):
        return self.skips


    def set_colors(self, colors):
        found = False
        for color in colors:
            for i in range(len(self.senders)):
                if self.senders[i]['sender'] == color[0]:
                    self.senders[i]['color'] = color[1]
                    found = True

            if not found:
                if len(color) == 1:
                    self.senders.append({'id': self.id_sender, 'sender': color[0], 'color': 'grey'})
                else:
                    self.senders.append({'id': self.id_sender, 'sender': color[0], 'color': color[1]})
                self.id_sender += 1


    def get_time(self):
        return time.strftime("%H:%M", time.gmtime())


    def __get_lines(self, number):
        lines = 0
        for i in range(number):

            m = self.MESSAGES[(len(self.MESSAGES)-1) - i]
            l = (len(m['sender']) + len(m['message']) + self.len_frame)

            s = 0
            for j in self.skips[(len(self.skips)-1) - i]:
                j = str(j)
                if isinstance(j, str):
                    for k in j.split('\n'):
                        s += ((len(k)-1) // os.get_terminal_size().columns) + 1
                else:
                    s += ((len(j)-1) // os.get_terminal_size().columns) + 1

            lines += (((l-1) // os.get_terminal_size().columns) + 1) + s

        return lines


    def __print_mess(self, sender, text, time):
        if self.is_time:
            print('[{}] '.format(time), end='')

        for i in self.senders:
            if not i['sender'] == sender:
                c0, c1 = 'white', 'grey'
            else:
                c = i['color']
                if c == 'grey':
                    c0, c1 = 'white', 'grey'
                else:
                    c0, c1 = 'grey', c
                break

        print(colored('[' + sender + ']', c0, ('on_' + c1)) + ': ', end='')
        print(text, end='\n')

        if self.is_save_file:
            dt = time.strftime("%d.%m %H:%M", time.gmtime())
            str = ''
            try:
                file = open(self.file_name, 'r')
                str = file.read()
                file.close()
                file = open(self.file_name, 'w')
            except IOError:
                file = open(self.file_name, 'w')

            file.write(str + '[' + dt + '] [' + sender + ']' + ': ' + text + '\n')


    def add_skip(self, text):
        lines = ((len(str(text))-1) // os.get_terminal_size().columns) + 1

        if not self.skips:
            self.skips.append([text])
        else:
            if not self.skips[len(self.skips)-1]:
                self.skips[len(self.skips)-1].append(text)
            else:
                self.skips[len(self.skips)-1].append(text)
        print(text)


    def remove_skip(self, number):
        if number > 0 and number <= len(self.skips):
            n = len(self.skips) - number
            self.up_on_message(number)
            self.skips[n].clear()
            if number == len(self.skips):
                self._load(number-1)
            else:
                self._load(number)


    def edit_skip(self, number, text):
        if number > 0 and number <= len(self.skips):
            n = len(self.skips) - number
            self.up_on_message(number)
            self.skips[n] = [text]
            if number == len(self.skips):
                self._load(number-1)
            else:
                self._load(number)


    def load_in_skip(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            i = number
            for m in self.MESSAGES[len(self.MESSAGES)-number:len(self.MESSAGES)]:
                self.add_skip(self.MESSAGES[len(self.MESSAGES)-i]['message'])
                i -= 1


    def print_skip(self, number):
        if number > 0 and number <= len(self.skips):
            if len(self.skips[number]) != 0:
                for i in self.skips[number]:
                    print(i)


    def reload(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            self.up_on_message(number)
            self._load(number)


    def _load(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            i = len(self.skips) - number
            for m in self.MESSAGES[len(self.MESSAGES)-number:len(self.MESSAGES)]:
                self.__print_mess(m['sender'], m['message'], m['time'])
                self.print_skip(i)
                i += 1


    def remove(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            self.up_on_message(number)
            self._load(number-1)

            self.MESSAGES.pop(len(self.MESSAGES) - number)
            self.skips.pop(len(self.skips) - number)


    def edit(self, number, text):
        if number > 0 and number <= len(self.MESSAGES):
            n = len(self.MESSAGES) - number
            self.up_on_message(number)
            self.MESSAGES[n].update({'message': text})
            self._load(number)


    def add_message(self, sender, text):
        text = " ".join(str(text).split())

        if text != '':

            if not self.skips:
                self.skips.append([])

            time = self.get_time()
            self.MESSAGES.append({'id': self.id_message, 'sender': sender, 'message': text, 'time': time})
            self.id_message += 1
            self.__print_mess(sender, text, time)

            self.skips.append([])

            return self.id_message-1


    def __init__(self, clr=True, file_name='', time=False):

        self.MESSAGES = []
        self.senders = []
        self.skips = []

        self.id_message = 0
        self.id_sender = 0

        self.is_time = time
        if self.is_time:
            self.len_frame = 12
        else:
            self.len_frame = 4

        self.file_name = file_name
        if file_name != '':
            self.is_save_file = True
        else:
            self.is_save_file = False

        if clr:
            self._clear_screen()
