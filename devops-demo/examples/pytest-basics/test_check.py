from main import check_machine


def test_check_machine():
    a = 1                              # Arrange
    b = 1
    result = check_machine(a, b)       # Act
    assert result == True              # Assert
