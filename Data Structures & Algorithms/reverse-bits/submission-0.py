class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:]

        # Pad the binary string with leading zeros to ensure it's 32 bits long.
        # This is crucial for correctly reversing bits for numbers
        # that don't use all 32 bits (e.g., 1, which is '1' in binary).
        # Without padding, reversing '1' would still be '1', but for a 32-bit
        # reversal, it should become '100...000' (binary), which is 2**31.
        padded_binary_string = binary_string.zfill(32)

        # Reverse the padded binary string.
        reversed_binary_string = padded_binary_string[::-1]

        # Convert the reversed binary string back to an integer (base 2).
        reversed_integer = int(reversed_binary_string, 2)

        return reversed_integer