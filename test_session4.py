import pytest
import random
import string
import session4
import os
import inspect
import re
import math
from math import isclose
import decimal

number_1 = random.choice([-1,0,1])
number_2 = random.choice(list(set([-1,0,1])-set([number_1])))

README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    #readme_words = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_invalid_input_valueerror():
    with pytest.raises(ValueError):
        q = session4.Qualean(10)
    with pytest.raises(ValueError):
        q = session4.Qualean(-1.5)
    with pytest.raises(ValueError):
        q = session4.Qualean(5/3)

def test_invalid_input_valueerror_provides_relevant_message():
    with pytest.raises(ValueError, match=r".*[-1,0,1].*"):
        q = session4.Qualean(10)

def test_Qualean_repr():
    r = session4.Qualean(number_1)
    assert r.__repr__() == f'Qualean Number({r.number})', 'The representation of the Qualean object does not meet expectations'

def test_Qualean_str():
    r = session4.Qualean(number_1)
    assert r.__str__() == f'Qualean Number: {r.number}', 'The print of the Qualean object does not meet expectations'

def test_Qualean_comparison():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = session4.Qualean(number_2)  # this will be another random decimal number
    assert min(r1,r2) < max(r1,r2), "Wrong!! :) Object comparison is not as expected"  # using min, max function to be sure which one is smaller

def test_Qualean_comparison_with_non_Qualean():
    with pytest.raises(NotImplementedError) as e_info:
        r1 = session4.Qualean(number_1)   # Qualean object
        r2 = "Qualean"                  # String object
        r1 < r2

def test_Qualean_equality():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = r1  # storing the same object
    assert r2 == r1, "Wrong!! :) Object comparison is not as expected"  # using min, max function to be sure which one is smaller

def test_Qualean_invertsign():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = (-1)*r1.number  # storing the negative of object
    assert r1.__invertsign__() == r2, "Wrong!! :) Object comparison is not as expected"

def test_100_times_sum():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = decimal.Decimal(0)
    decimal.getcontext().prec = 12
    for i in range(100):
        r2 = r2 + r1.number
    assert 100*r1.number == r2 , "Wrong!! :) Object comparison is not as expected "
    
def test_1_Million_Qualean_mean_closeto_zero():
    r2 = decimal.Decimal(0)
    for i in range(1000000):
        r1 = session4.Qualean(random.choice([-1,0,1]))  # this will be a random decimal number
        r2 = r2 + r1.number
    r2 = r2/1000000
    assert isclose(decimal.Decimal(0), r2, rel_tol=0.01,abs_tol=0.01), "Wrong!! :) Object comparison is not as expected"

def test_Qualean_BOOL():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    assert r1.__bool__() == bool(r1), "Wrong!! :) Object comparison is not as expected"

def test_Qualean_AND():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = session4.Qualean(number_2)  # this will be a random decimal number
    assert (r1.__and__(r2)) == bool(r1 and r2), "Wrong!! :) Object comparison is not as expected"

def test_Qualean_OR():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = session4.Qualean(number_2)  # this will be a random decimal number
    assert (r1.__or__(r2)) == bool(r1 or r2), "Wrong!! :) Object comparison is not as expected"

def test_Qualean_AND_short_Circuit():
    r1 = session4.Qualean(0)  # this will be a 0 decimal number
    # r2 is not defined
    assert bool(r1 and r2) == False, "Wrong!! :) Object comparison is not as expected"

def test_Qualean_OR_short_Circuit():
    r1 = session4.Qualean(1)  # this will be a random decimal number
    # r2 is not defined
    assert bool(r1 or r2) == True, "Wrong!! :) Object comparison is not as expected"

def test_Qualean_ADD():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = session4.Qualean(number_2)  # this will be a random decimal number
    assert (r1.__add__(r2)) == (r1.number + r2.number), "Wrong!! :) Object comparison is not as expected"

def test_Qualean_MUL():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r2 = session4.Qualean(number_2)  # this will be a random decimal number
    assert (r1.__mul__(r2)) == (r1.number * r2.number), "Wrong!! :) Object comparison is not as expected"

def test_Qualean_SQRT():
    r1 = session4.Qualean(number_1)  # this will be a random decimal number
    r1.number = abs(r1.number)
    assert r1.__sqrt__() == r1.number.sqrt(), "Wrong!! :) Object comparison is not as expected"

def test_Qualean_SQRT_Negative():
    r1 = session4.Qualean(1)  # this will be a random decimal number
    r1.number = abs(r1.number)*(-1)
    assert type(r1.__sqrt__()) == complex, "Wrong!! :) Object comparison is not as expected"