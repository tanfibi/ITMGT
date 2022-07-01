def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.
    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.
    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale
    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".
    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

import math
def scytale_cipher(message, shift):
	chars = [c.upper() for c in message if c not in (' ',',','.','?','!',':',';',"'")]
	chunks = math.ceil(len(chars) / float(shift))
	inters, i, j = [], 1, 1

	while i <= chunks:
		inters.append(tuple(chars[j - 1:(j + shift) - 1]))
		i += 1
		j += shift

	cipher, k = [], 0
	while k < shift:
		l = 0
		while l < chunks:
			if k >= len(inters[l]):
				cipher.append('_')
			else:
				cipher.append(inters[l][k])
			l += 1
		k += 1

	return ''.join(cipher)

scytale_encrypt("ALGORITHMS_ARE_IMPORTANT",8)
#i guess it works but not really,, the numbers dont match up with the examples




def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.
    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.
    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"
    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def scytale_decipher(message, shift):
	chars = [c for c in message]
	chunks = int(math.ceil(len(chars) / float(shift)))
	inters, i, j = [], 1, 1

	while i <= shift:
		inters.append(tuple(chars[j - 1:(j + chunks) -1]))
		i += 1
		j += chunks

	plain, k = [], 0
	while k < chunks:
		l = 0
		while l < len(inters):
			plain.append(inters[l][k])
			l += 1
		k += 1

	return ''.join(plain)

scytale_decrypt("AMMLSPG_OOARRRTIEAT_NHIT", 8)