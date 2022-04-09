#TODO: LINT BJTCH


#TODO: write script
class CompressedGene:
	def __init__(self, gene: str) -> None:
		self._compress(gene)

	def _compress(self, gene: str) -> None:
		# print(gene)
		printy = ""
		self.bit_string: int = 1	# sentinel
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
				raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
		print("bit string gene representation:")
		print(printy)

		

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
