# RAF1

DISCLAIMER: RAF1 is a cipher that has not been verified to be secure by any means.
It should not be used for anything but learning purposes.

RAF1 (Random As F\*ck-1) was built for me, the creator, to learn about SP-networks.

To be fair, I have no idea if this even works. It's a work in progress.
A decryption method hasn't even been made yet. This might as well be a really shitty
hash function.

## Description

RAF-1 has a keysize of 512-bits. Why? Because I can.
RAF-1 has a blocksize of 512-bits. Why? Because I fucking can.
RAF-1 does 32 rounds of encryption. Why? Cause I said so.

### S-Box Creation

RAF-1 creates four S-Boxes of 512-bits each. The S-Box values are calculated
by taking four 128-bit chunks of the key, four 128-bit chunks of the IV,
and XORing each other. Each chunk of the key will XOR with every chunk of the IV.
The result is inserted into the respective S-Box.

To help visualize, let `k` be the key, and `j` be the IV:

k<sub>0</sub> XOR [j<sub>0</sub>, j<sub>1</sub>, j<sub>2</sub>, j<sub>3</sub>],

k<sub>1</sub> XOR [j<sub>0</sub>, j<sub>1</sub>, j<sub>2</sub>, j<sub>3</sub>]...

### Substitution

RAF-1 substitutes each byte in the S-Box by taking the most-significant bit and
the least-signigicant bit to determine which S-Box to use. It then takes the six
inner bits to determine which byte to substitute for.

To help visualize, `00110101` is our byte to substitute. We take the MSB and the LSB
to determine which S-Box to use. `01` == s<sub>1</sub>. Then we take the six inner
bits to determine which byte to substitute. `011010` == 26. Looking at a 2d array,
it would look like `sBoxes[1][26]`. That byte is added to the S-Box output and used
in further rounds.

### P-Box

RAF-1 should simply distribute each byte from the input S-Box to each output S-Box.
See the picture below for a graphic from Wikipedia.

![P-Box Implementation](https://upload.wikimedia.org/wikipedia/commons/c/c7/Link_between_S-Boxes.gif)

## Summary

This is the RAF-1 (Random As F\*ck-1) cipher. It's insecure, probably doesn't work,
and probably a big waste of my time, but it was fun to come up with.

The current build is not working cause I'm an idiot, FYI.
