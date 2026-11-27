"""Tests for crystal_batch.balance against the hand calculations.

Reference answers: validation/03_mass_balance_hand.pdf (p.1-2); 293.15 K cases from validation/05_checks_hand.pdf p.1.
Seed is excluded from product (added, not produced) - 03 p.2.
"""
import pytest
from crystal_batch import balance   # plain import: red (not skipped) until balance.py exists

REL = 1e-3  # agreed tolerance: matches hand calc to ~4 sig figs
M_WATER = 350.0  # kg
T_SAT = 323.15   # K (50 °C)
T_EXTRAP = 288.15  # K (15 °C) - below Fujiwara fit, must warn
T_EDGE = 293.15    # K (20 °C) - lower edge of fit, must NOT warn


def _check(actual, expected):
    assert actual == pytest.approx(expected, rel=REL)


# --- dissolved(m_water, T_sat) ----------------------------------------------
def test_dissolved():
    _check(balance.dissolved(M_WATER, T_SAT), 12.036)  # kg, 03 p.1


# --- mother_liquor(m_water, T_final) ----------------------------------------
@pytest.mark.filterwarnings("error")
def test_mother_liquor_in_range():
    _check(balance.mother_liquor(M_WATER, T_EDGE), 4.426)  # kg, 05 p.1 


def test_mother_liquor_extrapolated_warns():
    with pytest.warns(UserWarning):
        ml = balance.mother_liquor(M_WATER, T_EXTRAP)
    _check(ml, 3.774)  # kg, 03 p.1


# --- product(m_water, T_sat, T_final) ---------------------------------------
@pytest.mark.filterwarnings("error")
def test_product_in_range():
    _check(balance.product(M_WATER, T_SAT, T_EDGE), 7.610)  # kg, 05 p.1


def test_product_extrapolated_warns():
    with pytest.warns(UserWarning):
        p = balance.product(M_WATER, T_SAT, T_EXTRAP)
    _check(p, 8.262)  # kg, 03 p.2


def test_product_rejects_T_final_above_T_sat():
    with pytest.raises(ValueError):
        balance.product(M_WATER, T_SAT, T_SAT + 5)


# --- recovery(m_water, T_sat, T_final) --------------------------------------
def test_recovery_extrapolated_warns():
    with pytest.warns(UserWarning):
        r = balance.recovery(M_WATER, T_SAT, T_EXTRAP)
    _check(r, 0.686)  # fraction, 03 p.2


@pytest.mark.filterwarnings("error")
def test_recovery_in_range():
    r = balance.recovery(M_WATER, T_SAT, T_EDGE)
    _check(r, 0.6323)  # fraction 05 p.1: 7.6103 / 12.036

# --- physics checks ---------------------------------------------------------
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_closure():
    assert balance.product(M_WATER,T_SAT,T_EXTRAP)+ balance.mother_liquor(M_WATER,T_EXTRAP) == pytest.approx(balance.dissolved(M_WATER,T_SAT), rel=1e-12)  # true by construction ; regression guard 


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_colder_gives_more_product():
    assert balance.product(M_WATER,T_SAT,T_EDGE) < balance.product(M_WATER,T_SAT,T_EXTRAP)

def test_recovery_zero_when_no_cooling():
    assert balance.recovery(M_WATER, T_SAT, T_SAT) == pytest.approx(0, abs=1e-12)