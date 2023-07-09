import pytest
from BracketBalance import balance


@pytest.mark.parametrize(
    "obj, expected", [
        ('(((([{}]))))', 'Сбалансированно'),
        ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
        ('{{[()]}}', 'Сбалансированно'),
        ('}{}', 'Несбалансированно'),
        ('{{[(])]}}', 'Несбалансированно'),
        ('[[{())}]', 'Несбалансированно')
    ]
)
def test_balance_brackets(obj, expected):
    res = balance(obj)
    assert res == expected


