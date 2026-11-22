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
        (323.15, None),  # TODO: 50 °C, from 05_checks
        (288.15, None),  # TODO: 15 °C (extrapolated), from 05_checks
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
        (None, None),  # TODO: x at 50 °C -> 34.388 g/kg (05_checks)
        (None, None),  # TODO: x at 15 °C -> g/kg (05_checks)
    ],
)
def test_g_per_kg(x, expected):
    if x is None or expected is None:
        pytest.skip("input/expected not filled in yet")
    _check(solubility.g_per_kg(x), expected)


# --- delta_H(T_K) -----------------------------------------------------------
# TODO: state units of expected values here (J/mol or kJ/mol) to match your function.
@pytest.mark.parametrize(
    "T_K, expected",
    [
        (298.15, None),  # TODO: Fujiwara's published value
        (323.15, None),  # TODO: 50 °C
        (288.15, None),  # TODO: 15 °C (extrapolated)
    ],
)
def test_delta_H(T_K, expected):
    if expected is None:
        pytest.skip("expected value not filled in yet")
    _check(solubility.delta_H(T_K), expected)
