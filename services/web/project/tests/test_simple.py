from project.utilslocal import eightqueen


def test_area():
	output = eightqueen.eightqueen(8)
	assert len(output.solutions) == 92
 