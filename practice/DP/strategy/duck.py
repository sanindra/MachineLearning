
class Duck(object):

    def __init__(self, fb, qb):
        self.fb = fb
        self.qb = qb

    def perform_fly(self):
        self.fb.fly()

    def perform_quack(self):
        self.qb.quack()


class Flying(object):
    def fly(self):
        raise NotImplementedError


class Quacking(object):
    def quack(self):
        raise NotImplementedError
