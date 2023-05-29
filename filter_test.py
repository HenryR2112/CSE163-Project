import pandas as pd
from typing import Any
import math
import numpy as np
TOLERANCE = 0.001

DF_FREMONT = 

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


def filter_range_test() -> None:
    '''
    a test function for filter_range in
    a3_pandas and a3_manual python files
    '''
    pass


def mean_attack_for_type_test() -> None:
    '''
    a test function for mean_attack_for_type in
    a3_pandas and a3_manual python files
    '''
    pass



def count_types_test() -> None:
    '''
    a test function for count_types in
    a3_pandas and a3_manual python files
    '''
    pass



def mean_attack_per_type_test() -> None:
    '''
    a test function for mean_attack_per_type in
    a3_pandas and a3_manual python files
    '''
    pass


def main():
    test_row_count(df_fremont, 45251)
    test_column_count(df_fremont, 2)
    test_column_count(df_ballard, 2)
    test_column_count(df_burke, 2)
    test_column_count(df_elliott, 2)


    test_max_level()

    filter_range_test()

    mean_attack_for_type_test()

    count_types_test()

    mean_attack_per_type_test()


if __name__ == "__main__":
    main()
