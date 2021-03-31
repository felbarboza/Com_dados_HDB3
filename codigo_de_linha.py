import bitarray
import matplotlib.pyplot as plt
import numpy as np


def string_to_bits(message):

  res = ''.join(format(ord(i), '08b') for i in message) 

  return res

string = string_to_bits('abc')
strOutput = []
pulse=-1
num_zeros=0
conta_pulsos=0
soma_sinais=0

for pos, bit in enumerate(string):
  if(bit=='1'):
    pulse = pulse*-1
    if(pulse==-1):
      strOutput.append('-')
      soma_sinais-=1
    else:
      strOutput.append('+')
      soma_sinais+=1
    conta_pulsos+=1
    num_zeros=0

  else:
    num_zeros+=1
    if(num_zeros==4):
      # if(soma_sinais==0):
      #   strOutput.append('V')
      #   soma_sinais+=pulse
      # else:
      #   strOutput[pos-3]='B'
      #   strOutput.append('V')
      #   soma_sinais+=2*pulse
      # num_zeros=0

      if(conta_pulsos%2==0):
        if(pulse==-1):
          strOutput[pos-3]='B'
          strOutput.append('V')
          pulse=1
        else:
          strOutput.append('V')
      else:
        if(pulse==-1):
          strOutput.append('V')
        else:
          strOutput[pos-3]='B'
          strOutput.append('V')
          pulse=-1
      conta_pulsos=0  
      num_zeros=0
    else:
      strOutput.append(0)


print("codificado",strOutput)
