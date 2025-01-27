from unit_tests.EmailValidation import is_valid_email
from unit_tests.rectangle import Rectangle
from unit_tests.CompteBancaire import CompteBancaire
import pytest

# Email
def test_email_should_be_valid():
    # Arrange
    email = "tests@tests.com"
    # Act
    result = is_valid_email(email)
    # Assert
    assert result == True

def test_email_should_not_be_valid():
    # Arrange
    email_without_at = "totototo.com"
    email_without_dot = "tests@totocom"
    # Act
    result1 = is_valid_email(email_without_at)
    result2 = is_valid_email(email_without_dot)
    # Assert
    assert result1 == False
    assert result2 == False # not working, should fix

# Rectangle
def test_rectangle_area_should_work():
    # Arrange
    height = 10
    width = 5
    # Act
    rect = Rectangle(width, height)
    result = rect.area()
    # Assert
    assert result == 50
# Rectangle
def test_rectangle_area_should_not_work():
    # Arrange
    height = 10
    width = 6
    # Act
    rect = Rectangle(width, height)
    result = rect.area()
    # Assert
    assert result != 50

def test_compte_bancaire_initial_solde_should_be_zero():
    # Arrange
    # Act
    compte = CompteBancaire()
    result = compte.get_solde()
    # Assert
    assert result == 0

def test_compte_bancaire_depot_should_work():
    # Arrange
    compte = CompteBancaire()
    # Act
    compte.depot(100)
    result = compte.get_solde()
    # Assert
    assert result == 100

def test_compte_bancaire_depot_should_not_work():
    # Arrange
    compte = CompteBancaire()
    # Act
    compte.depot(-100)
    result = compte.get_solde()
    # Assert
    assert result == 0

def test_compte_bancaire_retrait_should_work():
    # Arrange
    compte = CompteBancaire()
    compte.depot(100)
    # Act
    compte.retrait(50)
    result = compte.get_solde()
    # Assert
    assert result == 50

def test_compte_bancaire_retrait_should_not_work():
    # Arrange
    compte = CompteBancaire()
    compte.depot(100)
    # Act
    compte.retrait(150)
    result = compte.get_solde()
    # Assert
    assert result == 100

def test_compte_bancaire_depot_should_return_error():
    # Arrange
    compte = CompteBancaire()
    # Act and Assert
    with pytest.raises(TypeError):
        compte.depot("test")
