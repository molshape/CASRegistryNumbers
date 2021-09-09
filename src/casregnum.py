import re

### Class for CAS Registry Numbers
class CAS:
    def __init__(self, cas_reg_num):
        # case that input cas_reg_num is an integer
        if isinstance(cas_reg_num, int):
            self.cas_integer = cas_reg_num
            # convert integer into (formatted) CAS string
            reCAS_RN = re.compile("(\d{2,7})(\d{2})(\d{1})")
            self.CAS = reCAS_RN.sub("\g<1>-\g<2>-\g<3>", str(cas_reg_num))
        # case that cas_reg_num is a string
        elif isinstance(cas_reg_num, str):
            self.CAS = cas_reg_num
        # case that  cas_reg_num is neither an integer nor a string
        else:
            raise TypeError(
                f"Invalid CAS Registry Number format '{cas_reg_num}' (expected an integer (<class 'int'>) or a string (<class 'str'>), but found {type(cas_reg_num)})"
            )
        # extract check digit = last digit of the CAS number
        self.check_digit = int(str(cas_reg_num)[-1])

    def __str__(self):
        return self.CAS

    ### Returns CAS Registry Number
    @property
    def CAS(self):
        return self.__sCAS

    ### Sets CAS Registry Number
    ###    if the passed input value is a string, parse the string according to _____00-00-0
    ###    if the passed input value is an integer, create the string arrocing to _____00-00-0
    @CAS.setter
    def CAS(self, cas_reg_num):
        # convert (formatted) CAS string into integer
        reCAS_RN = re.match("(\d{2,7})\-(\d{2})-(\d{1})", cas_reg_num)
        if reCAS_RN:
            self.cas_integer = self.__iCAS = int(
                reCAS_RN.group(1) + reCAS_RN.group(2) + reCAS_RN.group(3)
            )
        # cas_reg_num is not following the notation rule for CAS numbers => ValueError
        else:
            raise ValueError(
                f"Invalid CAS number format for '{cas_reg_num}' (must follow the notation _____00-00-0)"
            )
        self.__sCAS = cas_reg_num

    ### Returns CAS Registry Number as an integer (without the hyphens)
    @property
    def cas_integer(self):
        return self.__iCAS

    @cas_integer.setter
    def cas_integer(self, cas_reg_num):
        # by definition, the lowest theoretical CAS number is 10-00-4,
        # the officially lowest CAS number on record is 35-66-5
        # (Source: https://twitter.com/CASChemistry/status/1144222698740092929)
        if cas_reg_num < 10004:
            raise TypeError(
                f"Invalid CAS number '{cas_reg_num}' (must be an integer >= 10004)"
            )
        self.__iCAS = cas_reg_num

    ### Returns check digit of the CAS Registry Number
    @property
    def check_digit(self):
        return self.__check_digit

    ### Sets the CAS Registry Number check digit
    @check_digit.setter
    def check_digit(self, digit_to_test):
        # check if the check digit fits to the CAS Number
        # Source: https://www.cas.org/support/documentation/chemical-substances/checkdig
        # get the CAS number without the check digit (integer value of cas_integer/10) => change integer into string => reverse string (cas_digits)
        cas_digits = str(int(self.cas_integer / 10))[::-1]
        # calculate check sum
        check_sum = 0
        for pos, digit in enumerate(cas_digits, start=1):
            check_sum += pos * int(digit)
        # test (check sum mod 10) against check digit
        if check_sum % 10 != int(digit_to_test):
            raise ValueError(
                f"Invalid CAS number '{self.CAS}' (found check digit '{digit_to_test}', but expected '{check_sum % 10}')"
            )
        self.__check_digit = int(digit_to_test)
