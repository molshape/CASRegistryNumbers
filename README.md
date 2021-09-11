# casregnum

![PyPI](https://img.shields.io/pypi/v/casregnum)

Python class to check, manage and sort CAS Registry Numbers&reg; (CAS RN&reg;).

<details>
<summary>Table of Content</summary>

1. [Description](#description)
2. [How to install and uninstall?](#how-to-install-and-uninstall)
3. [How to use?](#how-to-use)
4. [Examples](#examples)
	
</details>

## Description
**casregnum** is a Python class to check, manage and sort CAS Registry Numbers&reg; (CAS RN&reg;) by the [Chemical Abstracts Service](https://www.cas.org/). Check their official [FAQ](https://www.cas.org/support/documentation/chemical-substances/faqs) for more information on CAS numbers.


## How to install and uninstall? 
**chemregnum** can be installed from the [Python Package Index (PyPI)](https://pypi.org/) repository by calling

	pip install chemregnum

In order to uninstall **ChemFormula** from your local environment use

	pip uninstall chemregnum


## How to use?
**chemregnum** provides the `CAS` class for creating a CAS Registry Number&reg; instance:

```Python
from chemregnum import CAS

substance = CAS(cas_rn)
```

Note that `cas_rn` can either be an integer or a string. If you provide an integer, the `CAS` class will take care of formatting the CAS RN&reg; for you. If you provide a string, it needs to comply with the CAS number formatting rules, i. e. *2-7 digits* **dash** *two digits* **dash** *single check digit* (_____00-00-0).

Examples:

```Python
from casregnum import CAS

caffeine = CAS(58_08_2)
theine = CAS("58-08-2")
l_lacticacid = CAS(79_33_4)
d_lacticacid = CAS(10326_41_7)

print(f"str: {caffeine}")
print(f"int: {theine.cas_integer}")
print(f"{caffeine} == {theine}: {caffeine == theine}")
print(f"{caffeine} > {theine}: {caffeine > theine}")
print(f"{l_lacticacid} > {d_lacticacid}: {l_lacticacid > d_lacticacid}")
print(f"{l_lacticacid} < {d_lacticacid}: {l_lacticacid < d_lacticacid}")
```

will generate the following output:

```
str: 58-08-2
int: 58082
58-08-2 == 58-08-2: True
58-08-2 > 58-08-2: False
79-33-4 < 10326-41-7: True
```

