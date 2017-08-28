from duck import Duck
from flying import FlyWithWings, FlyNoWay
from quacking import Quack


class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__(FlyWithWings(), Quack())

    @staticmethod
    def display():
        print 'I\'m a Mallard Duck'


class ModelDuck(Duck):
    def __init__(self):
        super(ModelDuck, self).__init__(FlyNoWay(), Quack())

    @staticmethod
    def display():
        print 'I\'m a model duck'


if __name__ == '__main__':
    MallardDuck.display()
    mallard = MallardDuck()
    mallard.perform_fly()
    mallard.perform_quack()

    ModelDuck.display()
    model = ModelDuck()
    model.perform_fly()
    model.perform_quack()
