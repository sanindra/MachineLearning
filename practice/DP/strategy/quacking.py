from duck import Quacking


class Quack(Quacking):
    def quack(self):
        print 'Quack!!'


class MuteQuack(Quacking):
    def quack(self):
        print '<<silence>>'


class Squeak(Quacking):
    def quack(self):
        print 'Squeak'
