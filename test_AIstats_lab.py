import numpy as np

from AI_stats_lab import (
    joint_pmf,
    marginal_px,
    marginal_py,
    conditional_pmf_x_given_y,
    conditional_distribution_x_given_y,
    probability_sum_greater_than_3,
    independence_check,
    expected_x,
    expected_y,
    expected_xy,
    variance_x,
    variance_y,
    covariance_xy,
    correlation_xy,
    variance_sum,
    variance_identity_check,
)


def test_joint_pmf():
    assert np.isclose(joint_pmf(0, 0), 0.10)
    assert np.isclose(joint_pmf(1, 1), 0.20)
    assert np.isclose(joint_pmf(2, 2), 0.15)
    assert np.isclose(joint_pmf(3, 3), 0.10)
    assert np.isclose(joint_pmf(0, 2), 0.00)
    assert np.isclose(joint_pmf(5, 5), 0.00)


def test_marginals():
    assert np.isclose(marginal_px(0), 0.15)
    assert np.isclose(marginal_px(1), 0.40)
    assert np.isclose(marginal_px(2), 0.30)
    assert np.isclose(marginal_px(3), 0.15)

    assert np.isclose(marginal_py(0), 0.25)
    assert np.isclose(marginal_py(1), 0.35)
    assert np.isclose(marginal_py(2), 0.25)
    assert np.isclose(marginal_py(3), 0.15)


def test_conditional_pmf():
    assert np.isclose(conditional_pmf_x_given_y(1, 1), 0.20 / 0.35)
    assert np.isclose(conditional_pmf_x_given_y(2, 2), 0.15 / 0.25)
    assert np.isclose(conditional_pmf_x_given_y(3, 3), 0.10 / 0.15)


def test_conditional_distribution():
    dist = conditional_distribution_x_given_y(2)

    assert isinstance(dist, dict)
    assert np.isclose(dist[0], 0.00 / 0.25)
    assert np.isclose(dist[1], 0.05 / 0.25)
    assert np.isclose(dist[2], 0.15 / 0.25)
    assert np.isclose(dist[3], 0.05 / 0.25)
    assert np.isclose(sum(dist.values()), 1.0)


def test_probability_sum_greater_than_3():
    assert np.isclose(probability_sum_greater_than_3(), 0.50)


def test_independence_check():
    assert independence_check() is False


def test_expectations():
    assert np.isclose(expected_x(), 1.45)
    assert np.isclose(expected_y(), 1.30)
    assert np.isclose(expected_xy(), 2.60)


def test_variances():
    assert np.isclose(variance_x(), 0.9475)
    assert np.isclose(variance_y(), 1.01)


def test_covariance_and_correlation():
    assert np.isclose(covariance_xy(), 0.715)
    assert np.isclose(correlation_xy(), 0.731244, atol=1e-5)


def test_variance_sum():
    assert np.isclose(variance_sum(), 3.3875)


def test_variance_identity():
    assert variance_identity_check() is True
