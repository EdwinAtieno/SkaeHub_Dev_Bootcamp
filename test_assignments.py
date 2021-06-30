import csv

import strength_password
import Leap_year
import Length_word
import duplicate
import csv_dict

# QUESTION NUMBER 1
# check leap year

# Test to check year is a number
def integer(x):
    leap= Leap_year.Ifleap(x)
    return leap
def test_not_divisible():
    assert integer(2020)>0

#Test whether a year is a leap year
def test_leap_year():
    is_leap = Leap_year.Ifleap(2000)
    assert is_leap is True

#Test whether a year is NOT a leap year
def test_not_leap_year():
    not_leap = Leap_year.Ifleap(1800)
    assert not_leap is False

#QUESTION NUMBER 2
# python test to check password
# Test low password length
def test_weak_password_size():
    password = strength_password.password_output(1)
    assert len(password) == 6

#Test medium password length
def test_medium_password_size():
    password = strength_password.password_output(2)
    assert len(password) == 8
#Test high password length
def test_strong_password_size():
    password = strength_password.password_output(3)
    assert len(password) == 12


# QUESTION NUMBER 3
# checking on the length of a word
def test_length_last_word():
    last_word = Length_word.Sentence("eddy mzae Atieno")
    assert last_word <= 7
# check if accepts empty strings
def test_length_last_Empty_word():
    last_word = Length_word.Sentence("")
    assert last_word == 0

# QUESTION NUMBER 4
#check if it's a dictionary
def test_csv_dictionary():
    csv_dicts = csv_dict.csv_as_dict('edd.csv')
    assert isinstance(csv_dicts,dict) == False

# Check if it's empty
def test_empty():
    csv_dicts = csv_dict.empty('edd.csv')
    assert csv_dicts == False
# test to know if it exists
def test_path():
    csv_dicts = csv_dict.path("edd.csv")
    assert csv_dicts == True


# QUESTION NUMBER 5
# test on a List to check if it's a set
def test_set():
    leap = duplicate.delete_redudancy([])
    assert leap == set([])

# checks if an empty or

def test_empty():
    men = duplicate.delete_redudancy([])
    assert len(men) == 0

# check if the type is set
def test_type():
    types = duplicate.delete_redudancy([])
    assert type(types) == set
