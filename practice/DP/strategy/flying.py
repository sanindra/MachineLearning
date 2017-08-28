from duck import Flying


class FlyWithWings(Flying):
    def fly(self):
        print 'I\'m flying'


class FlyNoWay(Flying):
    def fly(self):
        print 'I can\'t fly'


class FlyRocketPowered(Flying):
    def fly(self):
        print 'I\'m flying with a rocket'
