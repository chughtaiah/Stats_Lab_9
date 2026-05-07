import numpy as np

from AI_stats_lab import (
    joint_cdf_unit_square,
    rectangle_probability,
    marginal_fx_unit_square,
    marginal_fy_unit_square,
    joint_pmf_heads,
    marginal_px_heads,
    marginal_py_heads,
    check_independence_heads,
)


# -------------------------------------------------
# Question 1 tests
# -------------------------------------------------

def test_joint_cdf_unit_square_inside():
    assert np.isclose(joint_cdf_unit_square(0.5, 0.4), 0.2)


def test_joint_cdf_unit_square_outside():
    assert np.isclose(joint_cdf_unit_square(-1, 0.5), 0.0)
    assert np.isclose(joint_cdf_unit_square(2, 2), 1.0)


def test_rectangle_probability():
    # For uniform unit square, probability equals rectangle area
    # P(0.2 < X <= 0.7, 0.1 < Y <= 0.6) = 0.5 * 0.5 = 0.25
    result = rectangle_probability(0.2, 0.7, 0.1, 0.6)
    assert np.isclose(result, 0.25, atol=1e-6)


def test_marginals_unit_square():
    assert np.isclose(marginal_fx_unit_square(0.3), 1.0)
    assert np.isclose(marginal_fx_unit_square(1.2), 0.0)
    assert np.isclose(marginal_fy_unit_square(0.8), 1.0)
    assert np.isclose(marginal_fy_unit_square(-0.5), 0.0)


# -------------------------------------------------
# Question 2 tests
# -------------------------------------------------

def test_joint_pmf_heads():
    assert np.isclose(joint_pmf_heads(0, 0), 0.25)
    assert np.isclose(joint_pmf_heads(0, 1), 0.25)
    assert np.isclose(joint_pmf_heads(1, 1), 0.25)
    assert np.isclose(joint_pmf_heads(1, 2), 0.25)
    assert np.isclose(joint_pmf_heads(1, 0), 0.0)


def test_marginal_px_heads():
    assert np.isclose(marginal_px_heads(0), 0.5)
    assert np.isclose(marginal_px_heads(1), 0.5)


def test_marginal_py_heads():
    assert np.isclose(marginal_py_heads(0), 0.25)
    assert np.isclose(marginal_py_heads(1), 0.5)
    assert np.isclose(marginal_py_heads(2), 0.25)


def test_check_independence_heads():
    assert check_independence_heads() is False
