import re

"""
Class for CAS Registry Numbers® (CAS RN®)
allwos to manage, check and sort CAS Registry Numbers®
see https://www.cas.org/support/documentation/chemical-substances/checkdig for a complete specification of the CAS Registry Numbers®
and the calculation method to determine the check digit
"""


class CAS:
    def __init__(self, cas_rn):
        # case that input cas_rn is an integer
        if isinstance(cas_rn, int):
            self.cas_integer = cas_rn
            # convert integer into (formatted) CAS string
            self.cas_string = re.sub(
                "^(\d{2,7})(\d{2})(\d{1})$", "\g<1>-\g<2>-\g<3>", str(cas_rn)
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

    ### default string output for CAS Registry Numbers
    def __str__(self):
        return str(self.cas_string)

    ### defines a string format for CAS Registry Numbers
    def __format__(self, format_spec):
        return f"{self.cas_string:{format_spec}}"

    ### checks if two CAS Registry Numbers are equal
    def __eq__(self, other):
        return True if self.cas_integer == other.cas_integer else False

    ### checks if self.cas_integer < other.cas_integer
    def __lt__(self, other):
        return True if self.cas_integer < other.cas_integer else False

    ### Returns CAS Registry Number
    @property
    def cas_string(self):
        return self.__cas_string

    ### Sets CAS Registry Number
    ###    if the passed input value is a string, parse the string according to _____00-00-0
    ###    if the passed input value is an integer, create the string arrocing to _____00-00-0
    @cas_string.setter
    def cas_string(self, cas_rn):
        # convert (formatted) CAS string into integer
        if regex_cas := re.match("^(\d{2,7})\-(\d{2})-(\d{1})$", cas_rn):
            self.cas_integer = self.__cas_integer = int(
                regex_cas.group(1) + regex_cas.group(2) + regex_cas.group(3)
            )
        # cas_rn is not following the notation rule for CAS numbers => ValueError
        else:
            raise ValueError(
                f"Invalid CAS number format for '{cas_rn}' (must follow the notation _____00-00-0)"
            )
        self.__cas_string = cas_rn

    ### Returns CAS Registry Number as an integer (without the hyphens)
    @property
    def cas_integer(self):
        return self.__cas_integer

    @cas_integer.setter
    def cas_integer(self, cas_rn):
        # by definition, the lowest theoretical CAS number is 10-00-4,
        # the officially lowest CAS number on record is 35-66-5 (as of June 2019)
        # (Source: https://twitter.com/CASChemistry/status/1144222698740092929)
        if cas_rn < 10004 or cas_rn > 9999999995:
            raise ValueError(
                f"Invalid CAS number '{cas_rn}' (must be an integer between 10004 and 9999999995)"
            )
        self.__cas_integer = cas_rn

    ### Returns check digit of the CAS Registry Number
    @property
    def check_digit(self):
        return self.__check_digit

    ### Sets the CAS Registry Number check digit
    @check_digit.setter
    def check_digit(self, digit_to_test):
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
                f"Invalid CAS number '{self.cas_string}' (found check digit '{digit_to_test}', but expected '{check_sum % 10}')"
            )
        self.__check_digit = int(digit_to_test)
