from digital_machine import *
from digital_machine.templates import simple
from digital_machine.templates import templates as t

class workshop(simple.SimpleClassTemplate):
  def model_0_1(self,instance):
    print(instance.device_key)
    
  pass
