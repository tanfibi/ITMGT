def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

#The code that initially worked but broke

def caesar_cipher(message, shift): 
    cipherText = ""
    for ch in message:
        if ch.isalpha():
            if ord(ch) >= 65 and ord(ch)<=90:
                shift_ = shift % 26
                result = chr(ord(ch) + shift_) #i think the issue is here bc it not wrap
                if (ord(result) > 90 and ord(result) < 122):
                    result = chr(ord(result) - 26)
                    finalLetter = chr(result)
                    cipherText += finalLetter
        
            elif (ord(ch) >= 97  and ord(ch)<=122):
                shift_ = shift % 26
                result = chr(ord(ch) + shift_)
                if ord(result) > 122:
                    result = chr(ord(result) - 26)
                    finalLetter = chr(result)
                    cipherText += finalLetter
    
    return cipherText

caesar_cipher("aaa", 12)

#"aaa",27 = bbb which is correct, but "zzz", 27 gives {{{ which is wrong...
# (z, 1) works to wrap back to give "a", but (Z,1) doesnt wrap around ,. gives "[" instead



def caesar_cipher(message, shift): 
  cipherText = ""
  for ch in message:
    if ch.isalpha() >= 65 and ord(ch)<=90:
      result = ord(ch) + shift 
      if result > ord('Z'):
        result -= 26
      finalLetter = chr(result)
      cipherText += finalLetter

    if ch.isalpha() : #OTHER CONDITION DOES HERE
      result = ord(ch) + shift 
      if result > ord('z'):
        result -= 26
      finalLetter = chr(result)
      cipherText += finalLetter
  
  return cipherText

caesar("hello", 3)

def caesar_cipher(message, shift): 
    cipherText = ""
    for ch in message:
        if ch.isalpha():
            if ord(ch) >= 65 and ord(ch)<=90:
                shift_ = shift % 26
                result = chr(ord(ch) + shift_) #i think the issue is here bc it not wrap
                if (ord(result) > 90 and ord(result) < 122):
                    result = chr(ord(result) - 26)
                    finalLetter = chr(result)
                    cipherText += finalLetter
        
            elif (ord(letter) >= 97  and ord(letter)<=122):
                shift_ = shift % 26
                result = chr(ord(letter) + shift_)
                if ord(result) > 122:
                    result = chr(ord(result) - 26)
                    finalLetter = chr(result)
                    cipherText += finalLetter
    
    return cipherText

    caesar("ZZZ", 1)
#https://www.ictdemy.com/python/basics/strings-in-python-working-with-single-characters


