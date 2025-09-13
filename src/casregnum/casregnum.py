"""
Class for CAS Registry Numbers® (CAS RN®)
allows to manage, check and sort CAS Registry Numbers®
see https://www.cas.org/support/documentation/chemical-substances/checkdig
for a complete specification of the CAS Registry Numbers®
and the calculation method to determine the check digit
"""

from __future__ import annotations

import re


class CAS:
    """
    Class for CAS Registry Numbers® (CAS RN®) -
    allows to manage, check and sort CAS Registry Numbers®

    Example usage:
    ```python
    from casregnum import CAS
    caffeine = CAS("58-08-2")
    print(caffeine)
    ```
    """
    def __init__(self, cas_rn: int | str) -> None:
        # case that input cas_rn is an integer
        if isinstance(cas_rn, int):
            self.cas_integer = cas_rn
            # convert integer into (formatted) CAS string
            self.cas_string = re.sub(
                r"^(\d{2,7})(\d{2})(\d{1})$", r"\g<1>-\g<2>-\g<3>", str(cas_rn)
            )
        # case that cas_rn is a string
        elif isinstance(cas_rn, str):
            self.cas_string = cas_rn
        # case that cas_rn is neither an integer nor a string
        else:
            raise TypeError(
                f"Invalid CAS Registry Number format '{cas_rn}' (expected an integer (<class 'int'>) or a string (<class 'str'>), but found {type(cas_rn)})"
            )
        # extract check digit = last digit of the CAS number
        self.check_digit = int(str(cas_rn)[-1])

    # default string output for CAS Registry Numbers
    def __str__(self) -> str:
        return str(self.cas_string)

    # defines a representation for CAS Registry Numbers
    def __repr__(self) -> str:
        return f"CAS(cas_rn='{self.cas_string}')"

    # defines a string format for CAS Registry Numbers
    def __format__(self, format_spec) -> str:
        return f"{self.cas_string:{format_spec}}"

    # checks if two CAS Registry Numbers are equal
    def __eq__(self, other: CAS) -> bool:
        if not isinstance(other, CAS):
            raise TypeError("Comparisons can only be made between CAS objects.")
        return self.cas_integer == other.cas_integer

    # checks if self.cas_integer < other.cas_integer
    def __lt__(self, other: CAS) -> bool:
        if not isinstance(other, CAS):
            raise TypeError("Comparisons can only be made between CAS objects.")
        return self.cas_integer < other.cas_integer

    # Returns CAS Registry Number
    @property
    def cas_string(self) -> str:
        """
        Returns the CAS Registry Number as a formatted string (e.g. "58-08-2").
        """
        return self._cas_string

    # Sets CAS Registry Number
    #    if the passed input value is a string, parse the string according to _____00-00-0
    #    if the passed input value is an integer, create the string arrocing to _____00-00-0
    @cas_string.setter
    def cas_string(self, cas_rn: str) -> None:
        # convert (formatted) CAS string into integer
        if regex_cas := re.match(r"^(\d{2,7})\-(\d{2})-(\d{1})$", cas_rn):
            self.cas_integer = self._cas_integer = int(
                regex_cas.group(1) + regex_cas.group(2) + regex_cas.group(3)
            )
        # cas_rn is not following the notation rule for CAS numbers => ValueError
        else:
            raise ValueError(
                f"Invalid CAS number format for '{cas_rn}' (must follow the notation _____00-00-0)"
            )
        self._cas_string = cas_rn

    # Returns CAS Registry Number as an integer (without the hyphens)
    @property
    def cas_integer(self) -> int:
        """
        Returns the CAS Registry Number as an integer (e.g. 58082).
        """
        return self._cas_integer

    @cas_integer.setter
    def cas_integer(self, cas_rn: int) -> None:
        # by definition, the lowest theoretical CAS number is 10-00-4,
        # the officially lowest CAS number on record is 35-66-5 (as of June 2019)
        # (Source: https://twitter.com/CASChemistry/status/1144222698740092929)
        if cas_rn < 10004 or cas_rn > 9999999995:
            raise ValueError(
                f"Invalid CAS number '{cas_rn}' (must be an integer between 10004 and 9999999995)"
            )
        self._cas_integer = cas_rn

    # Returns check digit of the CAS Registry Number
    @property
    def check_digit(self) -> int:
        """
        Returns the check digit of the CAS Registry Number (e.g. 2 for "58-08-2").
        """
        return self._check_digit

    # Sets the CAS Registry Number check digit
    @check_digit.setter
    def check_digit(self, digit_to_test: int) -> None:
        # check if the check digit fits to the CAS Number
        # Source: https://www.cas.org/support/documentation/chemical-substances/checkdig
        # get the CAS number without the check digit = integer value of (cas_integer/10)
        # => change that integer back into a string => reverse that string => cas_digits
        cas_digits = str(int(self.cas_integer / 10))[::-1]
        # calculate check sum
        check_sum = 0
        for pos, digit in enumerate(cas_digits, start=1):
            check_sum += pos * int(digit)
        # test (check sum mod 10) against check digit
        if check_sum % 10 != int(digit_to_test):
            raise ValueError(
                f"Invalid CAS number '{self.cas_string}' "
                f"(found check digit '{digit_to_test}', but expected '{check_sum % 10}')"
            )
        self._check_digit = int(digit_to_test)
