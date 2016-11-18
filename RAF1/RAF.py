class RAF:
    BLOCKSIZE = 64
    NUM_ROUNDS = 32
    NUM_SBOXES = 4

    def __init__(self, iv, key):
        self.iv = iv
        self.key = key
        self._getSBoxes()

    def encrypt(self, message):
        ciphertext = self._XOR(self.key, message)
        for round_num in range(self.NUM_ROUNDS-1):
            sOut = self._doSub(ciphertext)
            pOut = self._doPerm(sOut)
            ciphertext = self._XOR(self.key, pOut)
        sOut = self._doSub(ciphertext)
        ciphertext = self._XOR(self.key, sOut)
        return ciphertext

    def _doSub(self, ciphertext):
        sOut = ''
        for byte in ciphertext:
            sBox_idx, sBoxSub_idx = self._getSubIndices(byte)
            sOut += self.sBoxes[sBox_idx][sBoxSub_idx]
        return sOut

    def _doPerm(self, sOut):
        pBoxes = [[None]*self.BLOCKSIZE]*self.NUM_SBOXES
        for idx, sByte in enumerate(sOut):
            pBoxes[idx%4][idx/4] = sByte
        pOut = ''
        for pBox in pBoxes:
            for pByte in pBox:
                pOut += pByte
        return pOut

    def _getSBoxes(self):
        # Four SBoxes; 64-bytes each
        sBoxes = []
        chunk_size = self.BLOCKSIZE / self.NUM_SBOXES

        for idx in range(self.NUM_SBOXES):
            sBoxData = ''
            key_data = self.key[chunk_size*idx:chunk_size*(idx+1)]
            for idx2 in range(self.NUM_SBOXES):
                iv_data = self.iv[chunk_size*idx2:chunk_size*(idx2+1)]
                sBoxData += self._XOR(key_data, iv_data)
            sBoxes.append(list(sBoxData))
        self.sBoxes = sBoxes

    def _getSubIndices(self, byte):
        box_index = '{}{}'.format(
            str(((ord(byte) >> 7) & 1)),
            str(((ord(byte) >> 0) & 1))
        )

        sub_index = ''
        for bit_pos in range(6,0,-1):
            sub_index += str(((ord(byte) >> bit_pos) & 1))
        return (int(box_index, 2), int(sub_index, 2))

    def _XOR(self, d1, d2):
        data = ''
        for idx in range(len(d1)):
            data += chr(ord(d1[idx]) ^ ord(d2[idx]))
        return data
