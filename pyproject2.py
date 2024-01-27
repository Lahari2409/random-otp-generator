#import modules
import math as m #for floor method
import random as r
#function to generate otp
def otpgen():
#declare a string variable
#which stores all aplha-numeric characters
  string="0123456789abcdefghijklmnopqrstuvwxyz"
  otp=""
  varlen=len(string)
  for i in range(6):
      otp+=string[m.floor(r.random()*varlen)]
  return otp
#mail function
print(otpgen())
