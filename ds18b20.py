import logging

class DS18B20Exception(Exception):
  pass

class DS18B20(object):
    def __init__(self, id):
        self.file_name = '/sys/bus/w1/devices/' + id + '/w1_slave'
        self.logger = logging.getLogger(__name__)

    def getTemperature(self):
        try:
            f = open(self.file_name, 'r')
        except IOError:
            raise DS18B20Exception()
        try:
            raw = f.read()
        except IOError:
            raise DS18B20Exception()
        try:
            f.close()
        except IOError:
            raise DS18B20Exception()
        return float(raw.split("t=")[-1])/1000


