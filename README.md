# casregnum

![PyPI Version](https://img.shields.io/pypi/v/casregnum)
![CI](https://github.com/molshape/CASRegistryNumbers/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/github/molshape/CASRegistryNumbers/graph/badge.svg?token=5HZN6RX2XA)](https://codecov.io/github/molshape/CASRegistryNumbers) \
![Python Versions](https://img.shields.io/pypi/pyversions/casregnum)
![License](https://img.shields.io/github/license/molshape/casregnum) \
![GitHub stars](https://img.shields.io/github/stars/molshape/casregnum)


Python class to manage, check and sort CAS Registry Numbers&reg; (CAS RN&reg;).

<details>
<summary>Table of Contents</summary>

1. [Description](#description)
2. [How to install and uninstall?](#how-to-install-and-uninstall)
3. [How to use?](#how-to-use)
4. [Examples](#examples)
	
</details>

## Description
**casregnum** is a Python class to manage, check, and sort CAS Registry Numbers&reg; (CAS RN&reg;) by the [Chemical Abstracts Service](https://www.cas.org/). Check their official [FAQ website](https://www.cas.org/support/documentation/chemical-substances/faqs) for more information on CAS numbers.


## How to install and uninstall
**casregnum** can be installed from the [Python Package Index (PyPI)](https://pypi.org/) repository by calling

    pip install casregnum

or

    uv add casregnum

In order to uninstall **casregnum** from your local environment use

    pip uninstall casregnum

or

    uv remove casregnum


## How to use
**casregnum** provides the `CAS` class for creating a CAS Registry Number&reg; instance:

```Python
from casregnum import CAS

substance = CAS(cas_rn)
```

Note that `cas_rn` can either be an integer or a string. If you provide an integer, the `CAS` class will take care of formatting the CAS RN&reg; for you. If you provide a string, it needs to comply with the CAS number formatting rules, i. e. *2-7 digits* **dash** *two digits* **dash** *single check digit* (_____00-00-0).

The `CAS` class offers the following three properties:

```Python
.cas_string   # CAS number formatted as a string
.cas_integer  # CAS number as an integer
.check_digit  # check digit of the CAS number
```

## Examples:

```Python
from casregnum import CAS

caffeine = CAS(58_08_2)
theine = CAS("58-08-2")
l_lacticacid = CAS(79_33_4)
d_lacticacid = CAS(10326_41_7)
octanes = [
    CAS(111_65_9), CAS(592_27_8), CAS(589_81_1), CAS(589_53_7), CAS( 590_73_8), CAS(584_94_1),
    CAS(589_43_5), CAS(592_13_2), CAS(563_16_6), CAS(583_48_2), CAS( 619_99_8), CAS(564_02_3),
    CAS(540_84_1), CAS(560_21_4), CAS(565_75_3), CAS(609_26_7), CAS(1067_08_9), CAS(594_82_1),
]

print(f"str: {caffeine}")
print(f"int: {theine.cas_integer}")
print(f"check digit: {caffeine.check_digit}")
print(f"{caffeine} == {theine}: {caffeine == theine}")
print(f"{caffeine} > {theine}: {caffeine > theine}")
print(f"{l_lacticacid} > {d_lacticacid}: {l_lacticacid > d_lacticacid}")
print(f"{l_lacticacid} < {d_lacticacid}: {l_lacticacid < d_lacticacid}")

for i, isomer in enumerate(sorted(octanes), start=1):
    print(f"{isomer:>9}", end=", ")
    if i % 6 == 0:
        print()
```

This will generate the following output:

    str: 58-08-2
    int: 58082
    check digit: 2
    58-08-2 == 58-08-2: True
    58-08-2 > 58-08-2: False
    79-33-4 > 10326-41-7: False
    79-33-4 < 10326-41-7: True
    111-65-9,  540-84-1,  560-21-4,  563-16-6,  564-02-3,  565-75-3,
    583-48-2,  584-94-1,  589-43-5,  589-53-7,  589-81-1,  590-73-8,
    592-13-2,  592-27-8,  594-82-1,  609-26-7,  619-99-8, 1067-08-9,
