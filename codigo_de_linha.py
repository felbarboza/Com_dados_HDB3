import bitarray
import matplotlib.pyplot as plt
import numpy as np
from cryptography.fernet import Fernet


def string_to_bits(message):

  res = ''.join(format(ord(i), '08b') for i in message) 

  return res

def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def hdb3_coding(string):
  strOutput = []
  pulse=1
  pulseV=1
  num_zeros=0
  for pos, bit in enumerate(string):
    if(bit=='1'):
      if(pulse==1):
        strOutput.append('+')
      else:
        strOutput.append('-')
      pulse*=-1
      num_zeros=0
    else:
      num_zeros+=1
      if(num_zeros==4):
        if(pulseV==1):
          strOutput.append('+')
          if(pulse==1):
            strOutput[pos-3]='+'
            pulse*=-1
        else:
          strOutput.append('-')
          if(pulse==-1):
            strOutput[pos-3]='-'
            pulse*=-1
        pulseV*=-1
        num_zeros=0
      else:
        strOutput.append('0')
  return strOutput

def decode(message):
  num_zeros=0
  decoded=[]
  ultimo_sinal=0
  for pos, bit in enumerate(message):
    if(bit=='0'):
      num_zeros+=1
      decoded.append('0')
    else:
      if(bit=='+'):
        decoded.append('1')
        if(ultimo_sinal==1 and num_zeros>=2):
          decoded[pos]='0'
          decoded[pos-3]='0'
          ultimo_sinal=0
          num_zeros=0
        elif(ultimo_sinal==1 and num_zeros==3):
          decoded[pos]='1'
        else:
          num_zeros=0  
        ultimo_sinal=1
      else:
        decoded.append('1')
        if(ultimo_sinal==0 and num_zeros==2):
          decoded[pos]='0'
          decoded[pos-3]='0'
          ultimo_sinal=1
          num_zeros=0
        elif(ultimo_sinal==0 and num_zeros==3):
          decoded[pos]='0'
        else:
          num_zeros=0
        ultimo_sinal=0

  return decoded

message = 'the quick brówn fôx jumps ùver the lazy dog'
string_bit = string_to_bits(message)
hdb3_message = hdb3_coding(string_bit)
decoded = decode(hdb3_message)
string_decoded = ''.join(decoded)
message_right = frombits(string_decoded)

print (message)
print(string_bit)
print (hdb3_message)
print(decoded)
print(string_decoded)
print(message_right)
