#TODO: write script
class CompressedGene:
	def __init__(self, gene: str) -> None:
		self._compress(gene)

	def _compress(self, gene: str) -> None:

        # TODO: remove
		printy = ""  # holds a string representation of the bit string

		self.bit_string: int = 1	# start bit string with sentinel

        # loop through the characters in the gene string
		for nucleotide in gene.upper():
			self.bit_string <<= 2    # shift left two bit_string
			if nucleotide == "A":    # change last two bits to 00
				self.bit_string |= 0b00
				printy += "00"
			elif nucleotide == "C":    # change last two bits to 01
				self.bit_string |= 0b01
				printy += "01"
			elif nucleotide == "G":    # change last two bits to 10
				self.bit_string |= 0b10
				printy += "10"
			elif nucleotide == "T":    # change last two bits to 10
				self.bit_string |= 0b11
				printy += "11"
			else:
                # raise a value error if any characters becides A, C, G, or T are found
				raise ValueError("Invalid Nucleotide:{}".format(nucleotide))


        # print out some info for debugging TODO: remove
		print("gene sequence")
		print(gene)
		print()
		print("bit string gene representation:")
		print(printy)
		print()

		

	# TODO: write decompression method
	def decompress(self) -> None:
		print("decompression method run")
	
        
if __name__ == "__main__":
	# create gene sequence
	# gene = "bitch"  # this should raise a value error
	gene = "atcgtcgtagatcgctagccgcgcgcgcatagctagcttctagactgatcagcatacg"

	# compress gene sequence
	test: CompressedGene = CompressedGene(gene)

	# decompress gene sequence
	decompressed_gene: str = test.decompress()
