import os
from subprocess import call

class Mode(object):
  read = 1
  write = 2
  
  pass

class GPIOError(exception):
  pass

class GPOI(object):
  mode = Mode()
  high = 1
  low = 0
  P8_3 = "38" #GPIO1_6
  P8_4 = "39" #GPIO1_7
  P8_5 = "34" #GPIO1_2
  P8_6 = "35" #GPIO1_3
  P8_11 = "45" #GPIO1_13
  P8_12 = "44" #GPIO1_12
  P8_14 = "26" #GPIO0_26
  P8_15 = "47" #GPIO1_15
  P8_16 = "46" #GPIO1_14
  
  def __init__(self, pin, mode):
    self.mode = mode
    self.pin_path = "/sys/class/gpio/gpio" + pin
    self.pin_direction_path = self.pin_path + "/direction"
    self.pin_value_path = self.pin_path + "/value"
    
    if not os.path.isdir(self.pin_path):
      call("echo " + pin + " > /sys/class/gpio/export")
      
    if mode == GPIO.mode.read:
      call("echo in > " + self.pin_direction_path)
    elif mode == GPIO.mode.write:
      call("echo low > " + self.pin_direction_path)
    else:
      raise GPIOError():
  
  def read(self):
    return 0
  
  def set_level(self, level):
    if self.mode == GPIO.read:
      raise GPIOError()
    elif level == GPIO.high:
      call("echo high > " + self.pin_value_path)
    elif level == GPIO.low:
      call("echo low > " + self.pin_value_path)
    else:
      raise GPIOError()
      