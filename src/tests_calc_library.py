from calc_library import *
import pytest
import pdb


def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

    pytest.approx(0.2) == add(0.1, 0.1)
    pytest.approx(0.0) == add(0.1, -0.1)
    pytest.approx(-0.2) == add(-0.1, -0.1)
    pytest.approx(0.0) == add(0.0, 0.0)

    with pytest.raises(TypeError):
        add("a", 5)
    


def test_sub():
    assert sub(1, 1) == 0
    assert sub(-1, 1) == -2
    assert sub(-1, -1) == 0
    assert sub(1, -1) == 2

    pytest.approx(0.0) == sub(0.1, 0.1)
    pytest.approx(0.2) == sub(0.1, -0.1)
    pytest.approx(-0.2) == sub(-0.1, 0.1)
    pytest.approx(0.0) == sub(0.0, 0.0)

    with pytest.raises(TypeError):
        sub("a", 5)
    

def test_mul():
    assert mul(1, 1) == 1
    assert mul(-1, 1) == -1
    assert mul(1, -1) == -1
    assert mul(-1, -1) == 1
    assert mul(0, 1) == 0
    assert mul(1, 0) == 0
    assert mul(10, 10000) == 100000

    pytest.approx(0.01) == mul(0.1, 0.1)
    pytest.approx(-0.01) == mul(0.1, -0.1)
    pytest.approx(-0.01) == mul(-0.1, 0.1)
    pytest.approx(0.01) == mul(-0.1, -0.1)
    pytest.approx(0.0) == mul(0.0, 0.0)

    with pytest.raises(TypeError):
        mul("a", 1)


def test_div():
    assert div(1, 1) == 1
    assert div(-1, 1) == -1
    assert div(1, -1) == -1
    assert div(-1, -1) == 1
    assert div(0, 1) == 0
    assert div(100, 10) == 10

    pytest.approx(1.0) == div(0.1, 0.1)
    pytest.approx(-1.0) == div(0.1, -0.1)
    pytest.approx(-1.0) == div(-0.1, 0.1)
    pytest.approx(1.0) == div(-0.1, -0.1)
    pytest.approx(0.0) == div(0.0, 1.0)

    with pytest.raises(TypeError):
        div("a", 1)

    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

    with pytest.raises(ValueError):
        factorial(-1)
        factorial(1.5)

    with pytest.raises(TypeError):
        factorial("a")
        factorial("")


def test_sqr():
    assert sqr(1, 1) == 1
    assert sqr(4, 2) == 2
    assert sqr(10, -1) == 0.1

    pytest.approx(0.1) == sqr(0.01, 2)
    pytest.approx(0.01) == sqr(0.1, 2)
    pytest.approx(0.01) == sqr(0.0001, 4)

    with pytest.raises(TypeError):
        sqr("a", 1)
        sqr(1, "a")
        sqr("a", "a")
        sqr("", 1)
        sqr(1, "")
        sqr("", "")
        sqr(None, 2)
        sqr(4, None)

    with pytest.raises(ZeroDivisionError):
        sqr(4, 0)

    with pytest.raises(AssertionError):
        sqr(-4, 2)


def test_power():
    assert power(1, 0) == 1
    assert power(0, 1) == 0
    assert power(0, 0) == 1
    assert power(10, -1) == 0.1
    assert power(-1, 2) == 1
    assert power(-1, 3) == -1
    assert power(4, 0.5) == 2

    with pytest.raises(TypeError):
        power("a", 1)
        power(1, "a")
        power("a", "a")
        power("", 1)
        power(1, "")
        power("", "")
        power(None, 2)

    with pytest.raises(AssertionError):
        power(-4, 0.5)


def test_comb_num():
    assert comb_num(20, 10) == 184_756
    assert comb_num(0, 0) == 1

    with pytest.raises(ValueError):
        comb_num(10, 20)
        comb_num(-10, -20)
        comb_num(-20, 10)

    with pytest.raises(TypeError):
        comb_num(20.0, 10)
        comb_num(20, 10.0)
        comb_num("20", 10)

