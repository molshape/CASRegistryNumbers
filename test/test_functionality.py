import pytest

from casregnum import CAS


@pytest.fixture
def octanes():
    return [
        CAS(111_65_9), CAS(592_27_8), CAS(589_81_1), CAS(589_53_7), CAS(590_73_8), CAS(584_94_1),
        CAS(589_43_5), CAS(592_13_2), CAS(563_16_6), CAS(583_48_2), CAS(619_99_8), CAS(564_02_3),
        CAS(540_84_1), CAS(560_21_4), CAS(565_75_3), CAS(609_26_7), CAS(1067_08_9), CAS(594_82_1),
    ]


@pytest.fixture
def octanes_sorted():
    return [
        CAS(111_65_9), CAS(540_84_1), CAS(560_21_4), CAS(563_16_6), CAS(564_02_3), CAS(565_75_3),
        CAS(583_48_2), CAS(584_94_1), CAS(589_43_5), CAS(589_53_7), CAS(589_81_1), CAS(590_73_8),
        CAS(592_13_2), CAS(592_27_8), CAS(594_82_1), CAS(609_26_7), CAS(619_99_8), CAS(1067_08_9),
    ]


# pytest fixtures


@pytest.fixture
def caffeine():
    return CAS(58_08_2)


@pytest.fixture
def theine():
    return CAS("58-08-2")


@pytest.fixture
def l_lacticacid():
    return CAS(79_33_4)


@pytest.fixture
def d_lacticacid():
    return CAS("10326-41-7")


# Tests for functionality


def test_cas_check_digit(caffeine):
    assert caffeine.check_digit == 2


def test_cas_check_digit_print(caffeine):
    assert caffeine.check_digit


def test_cas_string_output(caffeine):
    assert str(caffeine) == "58-08-2"


def test_cas_equal(caffeine, theine):
    assert caffeine == theine


def test_cas_lesser_than(l_lacticacid, d_lacticacid):
    assert l_lacticacid < d_lacticacid


def test_cas_format_string(caffeine):
    assert f"{caffeine:0>12}"


def test_for_sorting(octanes, octanes_sorted):
    assert sorted(octanes) == octanes_sorted


# Tests for error handling


def test_cas_equal_invalid(caffeine):
    with pytest.raises(TypeError):
        assert caffeine == "theine"


def test_cas_lesser_than_invalid(l_lacticacid):
    with pytest.raises(TypeError):
        assert l_lacticacid < "D-lactic acid"


def test_cas_invalid_input():
    with pytest.raises(TypeError):
        CAS(6417.5)


def test_cas_format_unreadable():
    with pytest.raises(ValueError):
        CAS("64 - 17 - 5")


def test_cas_range_error():
    with pytest.raises(ValueError):
        CAS(100)


def test_cas_check_digit_error():
    with pytest.raises(ValueError):
        CAS("64-17-6")
