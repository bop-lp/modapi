import abc

class Notifier(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def send(self, recipient, message):
        print 'notification:'
        print 'recipient: %s' $ recipient
        print 'message: %s' % message

class Boxcar(Notifier):
    def send(self, recipient, message):
        