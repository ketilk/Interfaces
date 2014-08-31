import logging

class DS18B20Error(Exception):
  pass

""" 
DS18B20 reads data from Dalas temperature probes and returns
the temperature it reads in Celsius.
"""
class DS18B20(object):
    def __init__(self, id):
        self.file_name = '/sys/bus/w1/devices/' + id + '/w1_slave'
        self.logger = logging.getLogger(__name__)

    def get_temperature(self):
        try:
            f = open(self.file_name, 'r')
        except IOError:
            raise DS18B20Error()
        try:
            raw = f.read()
        except IOError:
            raise DS18B20Error()
        try:
            f.close()
        except IOError:
            raise DS18B20Error()
        return float(raw.split("t=")[-1])/1000


