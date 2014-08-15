import Adafruit_BBIO.GPIO as GPIO

class BBIO(object):
  _object_count = 0
  
  def __init__(self, pin):
    self.__class__._object_count += 1
    self.pin = pin
    
  def __del__(self):
    self.__class__._object_count -= 1
    if self.__class__._object_count == 0:
      GPIO.cleanup()

class OutputPin(BBIO):
  def __init__(self, pin):
    BBIO.__init__(self, pin)
    GPIO.setup(self.pin, GPIO.OUT)
    self.state = 0
  
  def set_high(self):
    GPIO.output(self.pin, GPIO.HIGH)
    self.state = 1
  
  def set_low(self):
    GPIO.output(self.pin, GPIO.LOW)
    self.state = 0
  
  def get_state(self):
    return state

class InputPin(BBIO):
  def __init__(self, pin):
    BBIO.__init__()
    GPIO.setup(self.pin, GPIO.IN)
  
  def input(self):
    return GPIO.input(self.pin)
  