# TODO: write doc string

class CompressedGene:
    """Class to compress/decompress a gene string into and from a binary string."""
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """compress the gene string"""
        # TODO: remove
        self.bit_string: int = 1	# start bit string with sentinel

        # loop through the characters in the gene string
        for nucleotide in gene.upper():
            self.bit_string <<= 2    # shift left two bit_string
            if nucleotide == "A":    # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C":    # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":    # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":    # change last two bits to 10
                self.bit_string |= 0b11
            else:
                # raise a value error if any characters becides A, C, G, or T are found
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

	# TODO: write decompression method
    def decompress(self) -> str:
        """decompress the bit string"""
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # -1 to include sentinal
            bits: int = self.bit_string >> i & 0b11 # get just 2 relevant bits
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]  # returned reversed string using slicing

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGATAATACGGCCCGTATTATATAGGCGCGCGCTATATATATATATACACAATACATAGATAGAGAGGAGCGCGCGCTCTCTCACACACAGAAGAGAGAGAGAGCGCGTGTAGATTAGTAC" * 100
    original_size = getsizeof(original)
    compressed: CompressedGene = CompressedGene(original)
    compressed_size = getsizeof(compressed.bit_string)
    bool_same = original == compressed.decompress()
    print(f"original is {original_size} bytes")
    print(f"compressed is {compressed_size} bytes")
    print(f"original and decompressed are the same: {bool_same}")
