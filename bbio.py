import Adafruit_BBIO.GPIO as GPIO

class BBIO(object):
  _object_count = 0
  
  def __init__(self):
    self.__class__._object_count += 1
    
  def __del__(self):
    self.__class__._object_count -= 1
    if self.__class__._object_count == 0:
      GPIO.cleanup()

class OutputPin(BBIO):
  def __init__(self, pin):
    BBIO.__init__()
    GPIO.setup(pin, GPIO.OUT)
    self.state = 0
    self.set_low()
  
  def set_high(self):
    GPIO.output(pin, GPIO.HIGH)
    self.state = 1
  
  def set_low(self):
    GPIO.output(pin, GPIO.LOW)
    self.state = 0
  
  def get_state(self):
    return state

class InputPin(BBIO):
  def __init__(self, pin):
    BBIO.__init__()
    GPIO.setup(pin, GPIO.IN)
  
  def input(self):
    return GPIO.input(pin)
  