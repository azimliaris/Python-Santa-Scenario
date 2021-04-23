class Reindeer:
    def __init__(self, name, injured, speed=None):
        self.speed = speed
        self.name = name.capitalize()
        self.checkName(name.upper())
        self.injured = injured.capitalize()
        self.checkInjured(injured.upper())

    def checkName(self, name):
        if name == 'DASHER':
            self.speed = 5
        elif name == 'DANCER':
            self.speed = 5
        elif name == 'PRANCER':
            self.speed = 5
        elif name == 'VIXEN':
            self.speed = 10
        elif name == 'COMET':
            self.speed = 10
        elif name == 'CUPID':
            self.speed = 15
        elif name == 'DONDER':
            self.speed = 20
        elif name == 'BLITZEN':
            self.speed = 30
        else:
            raise SyntaxError('There is no reindeer in this name')

    def checkInjured(self, injured):
        if injured == "YES":
            self.speed = 0
        elif injured == "NO":
            pass
        else:
            raise SyntaxError('INJURED HAS NO MEANNING')

    def __str__(self):
        if self.injured == "yes":
            return "noNAME: {}" \
                   "\ninjured: {}" \
                   "\nspeed: {}".format(
                self.name, self.injured, self.speed)
        else:
            return "Name: {}" \
                   "\ninjured: {}" \
                   "\nspeed: {}".format(
                self.name, self.injured, self.speed)
