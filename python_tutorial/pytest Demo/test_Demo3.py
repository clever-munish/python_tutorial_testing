# Marks in pytest cmd is pytest -rA -m smoke , regression
import pytest


@pytest.mark.smoke
def test_demo3():
    print("Inside sample file one")


@pytest.mark.regression
def test_demo3():
    print("Inside sample file two")


@pytest.mark.smoke
def test_demo3():
    print("Inside sample file three")


@pytest.mark.regression
def test_demo3():
    print("Inside sample file four")
