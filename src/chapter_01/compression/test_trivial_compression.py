# TODO: write pytests
import trivial_compression as tc
import pytest


def test_fails():
	# gene = "NotAGeneStringBitch"
	with pytest.raises(ValueError) as e_info:
		test: tc.CompressedGene = tc.CompressedGene("bitch")