import unittest


class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def depot(self, montant):
        if montant > 0:
            self.solde += montant
            return True
        return False

    def retrait(self, montant):
        if montant > 0 and self.solde - montant >= 0:
            self.solde -= montant
            return True
        return False

    def get_solde(self):
        return self.solde


class TestCompteBancaire(unittest.TestCase):
    def setUp(self):
        self.cb = CompteBancaire()

    def test_depot(self):
        self.assertTrue(self.cb.depot(10), "Le dépôt de 10 euros devraît être réussi")
        self.assertEqual(self.cb.get_solde(), 10, "Le solde devraît être à 10 euros")
        self.assertFalse(
            self.cb.depot(-10), "Le dépôt de -10 euros ne devraît pas être possible"
        )
        self.assertEqual(
            self.cb.get_solde(), 10, "Le solde devraît être encore à 10 euros"
        )

    def test_retrait(self):
        self.cb.depot(20)
        self.assertTrue(
            self.cb.retrait(10), "Le retrait de 10 euros devraît être réussi"
        )
        self.assertEqual(
            self.cb.get_solde(), 10, "Le solde devraît être à 10 euros après retrait"
        )
        self.assertFalse(
            self.cb.retrait(20),
            "Le retrait de 20 euros ne devraît pas être possible avec 10 euros de solde",
        )
        self.assertEqual(
            self.cb.get_solde(),
            10,
            "Le solde devraît être encore à 10 euros après tentative de retrait",
        )

    def test_solde_initial(self):
        self.assertEqual(self.cb.get_solde(), 0, "Le solde initial devraît être zéro")
        self.cb.depot(100)
        self.assertEqual(
            self.cb.get_solde(), 100, "Le solde devraît être 100 euros après dépôt"
        )


if __name__ == "__main__":
    unittest.main()
