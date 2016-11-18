

def GetSBoxes(iv):
    iv = list(iv)
    sboxes = []
    # Four SBoxes with 16 bytes each
    while len(iv) > 0:
        sboxes.append(iv[:16])
        iv = iv[16:]
    return sboxes

def doSub(ciphertext, sBoxes):
    sIn = []
    while len(ciphertext) > 0:
        sIn.append(ciphertext[:16])
        ciphertext = ciphertext[16:]
    sOut = ''
    for idx, sBoxIn in enumerate(sIn):
        for sByte in sBoxIn:
            sOut += sBoxes[idx][int(bin(ord(sByte))[-4:], 2)]
    return sOut

def doPBox(sOut, stringify=False):
    pOut = [[None]*16] * 4
    for idx, sByte in enumerate(sOut):
        pOut[idx%4][idx/4] = sByte
    stringy = ''
    for out in pOut:
        for char in out:
            stringy += char
    return stringy

def XOR(key, plaintext):
    data = ''
    for idx, char in enumerate(key):
        data += chr(ord(plaintext[idx]) ^ ord(char))
    return data

def encrypt(key, message, iv):
    sBoxes = GetSBoxes(iv)
    ciphertext = XOR(key, message)
    for i in range(31):
        sOut = doSub(ciphertext, sBoxes)
        pOut = doPBox(sOut)
        ciphertext = XOR(key, pOut)
    sOut = doSub(ciphertext, sBoxes)
    ciphertext = XOR(key, sOut)
    return ciphertext
