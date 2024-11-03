import unittest
import skip


runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(skip.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runST)