from casregnum import CAS

caffeine = CAS(58_08_2)
theine = CAS("58-08-2")
l_lacticacid = CAS(79_33_4)
d_lacticacid = CAS(10326_41_7)
octanes = [
    CAS(111_65_9), CAS(592_27_8), CAS(589_81_1), CAS(589_53_7), CAS(590_73_8), CAS(584_94_1),
    CAS(589_43_5), CAS(592_13_2), CAS(563_16_6), CAS(583_48_2), CAS(619_99_8), CAS(564_02_3),
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
