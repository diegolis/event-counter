import json
QUIT_STRING = "Quit"

class Values:

    def __init__(self, config):
        self.val = {}
        self.config = config
        for item, value in self.config.items():
            self.val[value] = 0

    def increase(self, key):
        self.val[key] += 1

    def get(self, key):
        return self.val[key]

    def show(self):
        print "VALORES"
        for item, value in self.config.items():
            if item != QUIT_STRING:
                print value, ":", self.val[value]


f = open("config.json", "r")
config = json.loads(f.read())

values = Values(config)

import curses
stdscr = curses.initscr()

while values.get(config[QUIT_STRING]) == 0:
    print ("INSTRUCCIONES:")
    for item, value in config.items():
        print value, "=", item

    print
    values.show()


    c = stdscr.getch()
    a = chr(c)
    print 'You entered', a

    try:
        values.increase(a)
    except:
        print "OPCION INCORRECTA"


curses.endwin()

values.show()
