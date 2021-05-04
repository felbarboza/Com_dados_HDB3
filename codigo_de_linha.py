import bitarray
import matplotlib.pyplot as plt
import numpy as np
from cryptography.fernet import Fernet

def crypt(message):
  asc=[ord(c) for c in message]
  result =[]
  for c in asc:
    result.append(c+111)
  result = ''.join(str(a) for a in result)
  return result

def decrypt(message):
  result = []
  for i in range(int(len(message)/3)):
    char = message[i*3:(i+1)*3]
    result.append(chr(int(char)-111))
  return ''.join(result)
    

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

  return ''.join(decoded)

if __name__ == "__main__": 
  message = 'the quick brówn fôx jumps ùver the lazy dog'
  encrypted = crypt(message)
  string_bit = string_to_bits(encrypted)
  hdb3_message = hdb3_coding(string_bit)

  decoded = decode(hdb3_message)
  message_encrypted = frombits(decoded)
  message_decryped = decrypt(message_encrypted)

  print (message, '\n')
  print(encrypted, '\n')
  print(string_bit, '\n')
  print (hdb3_message, '\n')
  print(decoded, '\n')
  print(message_encrypted, '\n')
  print(message_decryped, '\n')