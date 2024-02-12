import unittest 
import CompteBancaire

compte = CompteBancaire.__init__()

def depot_Test():
    assert compte.depot(50) == True

def retrait_Test():
    assert compte.depot(50) == True

def get_solde_Test(self):
    assert compte.depot(50) == True


if __name__ == '__main__':
    
    depot_Test()
    retrait_Test()
    get_solde_Test()