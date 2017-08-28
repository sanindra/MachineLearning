class Subject(object):

    def register_observer(self, o):
        # type: (object) -> object
        raise NotImplementedError()

    def remove_observer(self, o):
        raise NotImplementedError()

    def notify_observers(self):
        raise NotImplementedError()


class Observer(object):
    def update(self, temp, humidity, pressure):
        raise NotImplementedError()


class DisplayElement(object):
    def display(self):
        raise NotImplementedError()