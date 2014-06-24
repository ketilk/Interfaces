import logging

class DS18B20(object):
    def __init__(self, id):
        self.file_name = '/sys/bus/w1/devices/' + id + '/w1_slave'
        self.logger = logging.getLogger(__name__)

    def getTemperature(self):
        try:
            f = open(self.file_name, 'r')
        except IOError:
            self.logger.error('error opening sensor file.')
            return -1
        try:
            raw = f.read()
        except IOError:
            self.logger.error('error reading from sensor.')
            return -1
        try:
            f.close()
        except IOError:
            self.logger.error('error closing sensor file.')
            return -1
        return float(raw.split("t=")[-1])/1000


