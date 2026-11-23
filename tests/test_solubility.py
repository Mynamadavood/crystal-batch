"""Tests for crystal_batch.solubility against the hand calculations.

Reference answers: validation/03_mass_balance_hand.pdf (p.2) and
validation/05_checks_hand.pdf. Fill each `None` with the hand-calc value;
a case with a `None` is skipped, not passed.
"""
import pytest

solubility = pytest.importorskip("crystal_batch.solubility")

REL = 1e-3  # agreed tolerance: matches hand calc to ~4 sig figs


def _check(actual, expected):
    assert actual == pytest.approx(expected, rel=REL)


# --- mole_fraction(T_K) -----------------------------------------------------
@pytest.mark.parametrize(
    "T_K, expected",
    [
        (323.15,0.004082 ),  # hand calc, validation/05_checks
        (288.15, 0.001283),  # hand calc, validation/05_checks
    ],
)
def test_mole_fraction(T_K, expected):
    if expected is None:
        pytest.skip("expected value not filled in yet")
    _check(solubility.mole_fraction(T_K), expected)


# --- g_per_kg(x) ------------------------------------------------------------
@pytest.mark.parametrize(
    "x, expected",
    [
        (0.004082, 34.392),  # hand calc, validation/03 or 05
        (0.001283, 10.78),  # hand calc, validation/03 or 05
    ],
)
def test_g_per_kg(x, expected):
    if x is None or expected is None:
        pytest.skip("input/expected not filled in yet")
    _check(solubility.g_per_kg(x), expected)


# --- delta_H(T_K) -----------------------------------------------------------
# Units: Expected values in J/mol 
@pytest.mark.parametrize(
    "T_K, expected",
    [
        (298.15, 24050),  # Published Value (Fujiwara 2002): independent check
        (323.15, 29690),  # 50 °C hand calc, validation/03 or 05
        (288.15,21798),  #15 °C - extrapolated beyond the 20–50 °C fit
    ],
)
def test_delta_H(T_K, expected):
    if expected is None:
        pytest.skip("expected value not filled in yet")
    _check(solubility.delta_H(T_K), expected)
