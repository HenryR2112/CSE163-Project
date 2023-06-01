'''
CSE163 Final Project Group 3
Henry Ramstad, Ani Ramadurai, Annika Halvorson

Filter_test.py defines the testing functions for filter.py and ensures
that as the datasets are manipulated they return the correct information.

The function assert_equals was taken directly from the CSE163_utils files
provided for the assesments as a framework to build additional functions.
'''
import pandas as pd
from typing import Any
import math
import numpy as np

DF_BALLARD = ''
DF_FREMONT = ''
DF_BURKE = ''
DF_ELLIOTT = ''

def assert_equals(expected: Any, received: Any) -> None:
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the arugment is a data structure will do an approximate check
    on all of its contents.
    """

    if type(expected) == str:
        # Make sure strings have explicit quotes around them
        err_msg = f'Failed: Expected "{expected}", but received "{received}"'
    elif type(expected) in [np.ndarray, pd.Series, pd.DataFrame]:
        # Want to make multi-line output for data structures
        err_msg = f'Failed: Expected\n{expected}\n\nbut received\n{received}'
    else:
        err_msg = f'Failed: Expected {expected}, but received {received}'

    assert check_approx_equals(expected, received), err_msg


def test_column_count(df: pd.DataFrame, count: int) -> None:
    '''
    a test function to determine if a filtered dataframe has
    the correct number of columns
    '''
    assert_equals(count, df.shape[1])


def test_row_count(df: pd.DataFrame, count: int) -> None:
    '''
    a test function to determine if a filtered dataframe has
    the correct number of rows
    '''
    assert_equals(count, df.shape[0])


def test_lat_lon(df: pd.DataFrame, lat: float, lon: float) -> None:
    '''
    a test function to evaluate if the generated columns lat
    and lon in the modified dataframes match through the entire
    column.
    '''
    assert_equals((df['lon'][0], df['lat'][0]), (lon, lat))
    assert_equals((df['lon'][10], df['lat'][10]), (lon, lat))
    assert_equals((df['lon'][50], df['lat'][50]), (lon, lat))


def main():
    test_row_count(DF_FREMONT, 45251)
    test_row_count(DF_BALLARD, 45251)
    test_row_count(DF_BURKE, 45251)
    test_row_count(DF_ELLIOTT, 45251)
    
    test_column_count(DF_FREMONT, 3)
    test_column_count(DF_BALLARD, 3)
    test_column_count(DF_BURKE, 3)
    test_column_count(DF_ELLIOTT, 3)
    
    test_lat_lon(DF_FREMONT, -120, 20)
    test_lat_lon(DF_BALLARD, -120, 20)
    test_lat_lon(DF_BURKE, -120, 20)
    test_lat_lon(DF_ELLIOTT, -120, 20)





if __name__ == "__main__":
    main()
