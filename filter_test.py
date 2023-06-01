'''
CSE163 Final Project Group 3
Henry Ramstad, Ani Ramadurai, Annika Halvorson

Filter_test.py defines the testing functions for filter.py and ensures
that as the datasets are manipulated they return the correct information.

The function assert_equals and check_approx_equals was taken directly from
the CSE163_utils files provided for the assesments as a framework to
 uild additional functions.
'''
import pandas as pd
from typing import Any
import math
import numpy as np

TOLERANCE = 0.001
DF_BALLARD = pd.read_csv('Filtered Data/ballard_filtered.csv')
DF_FREMONT = pd.read_csv('Filtered Data/fremont_filtered.csv')
DF_BURKE = pd.read_csv('Filtered Data/burke_filtered.csv')
DF_ELLIOTT = pd.read_csv('Filtered Data/elliot_filtered.csv')


def check_approx_equals(expected: Any, received: Any) -> bool:
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    try:
        if type(expected) == dict:
            # first check that keys match, then check that the
            # values approximately match
            return expected.keys() == received.keys() and \
                all([check_approx_equals(expected[k], received[k])
                    for k in expected.keys()])
        elif type(expected) == list or type(expected) == set:
            # Checks both lists/sets contain the same values
            return len(expected) == len(received) and \
                all([check_approx_equals(v1, v2)
                     for v1, v2 in zip(expected, received)])
        elif type(expected) == float:
            return math.isclose(expected, received, abs_tol=TOLERANCE)
        elif type(expected) == np.ndarray:
            return np.allclose(expected, received, atol=TOLERANCE,
                               equal_nan=True)
        elif type(expected) == pd.DataFrame:
            try:
                pd.testing.assert_frame_equal(expected, received,
                                              atol=TOLERANCE)
                return True
            except AssertionError:
                return False
        elif type(expected) == pd.Series:
            try:
                pd.testing.assert_series_equal(expected, received,
                                               atol=TOLERANCE)
                return True
            except AssertionError:
                return False
        else:
            return expected == received
    except Exception as e:
        print(f"EXCEPTION: Raised when checking check_approx_equals {e}")
        return False


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
    test_row_count(DF_FREMONT, 54)
    test_row_count(DF_BALLARD, 54)
    test_row_count(DF_BURKE, 54)
    test_row_count(DF_ELLIOTT, 54)

    test_column_count(DF_FREMONT, 4)
    test_column_count(DF_BALLARD, 4)
    test_column_count(DF_BURKE, 4)
    test_column_count(DF_ELLIOTT, 4)

    test_lat_lon(DF_FREMONT, 47.648116, -122.349834)
    test_lat_lon(DF_BURKE, 47.681344, -122.265128)
    test_lat_lon(DF_BALLARD, 47.671213, -122.384746)
    test_lat_lon(DF_ELLIOTT, 47.616238, -122.356984)


if __name__ == "__main__":
    main()
