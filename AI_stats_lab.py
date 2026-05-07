
---

## `AI_stats_lab.py`

```python
import numpy as np


# -------------------------------------------------
# Sparse 4 by 4 Joint PMF
# -------------------------------------------------

def joint_pmf(x, y):
    """
    Joint PMF table:

             y=0   y=1   y=2   y=3
    x=0      0.10  0.05  0.00  0.00
    x=1      0.15  0.20  0.05  0.00
    x=2      0.00  0.10  0.15  0.05
    x=3      0.00  0.00  0.05  0.10
    """
    pass


def marginal_px(x):
    """
    Compute PX(x) by summing joint_pmf(x, y) over y = 0,1,2,3.
    """
    pass


def marginal_py(y):
    """
    Compute PY(y) by summing joint_pmf(x, y) over x = 0,1,2,3.
    """
    pass


def conditional_pmf_x_given_y(x, y):
    """
    Compute P(X=x given Y=y).

    P(X=x given Y=y) = joint_pmf(x,y) / PY(y)

    If PY(y) is zero, return 0.
    """
    pass


def conditional_distribution_x_given_y(y):
    """
    Return conditional distribution of X given Y=y
    as dictionary:

    {
        0: P(X=0 given Y=y),
        1: P(X=1 given Y=y),
        2: P(X=2 given Y=y),
        3: P(X=3 given Y=y)
    }
    """
    pass


def probability_sum_greater_than_3():
    """
    Compute P(X + Y > 3).
    """
    pass


def independence_check():
    """
    Return True if X and Y are independent.

    X and Y are independent if:

    joint_pmf(x,y) = PX(x) * PY(y)

    for every x and y.
    """
    pass


# -------------------------------------------------
# Expectation, Covariance, and Correlation
# -------------------------------------------------

def expected_x():
    """
    Compute E[X].
    """
    pass


def expected_y():
    """
    Compute E[Y].
    """
    pass


def expected_xy():
    """
    Compute E[XY].
    """
    pass


def variance_x():
    """
    Compute Var(X).
    """
    pass


def variance_y():
    """
    Compute Var(Y).
    """
    pass


def covariance_xy():
    """
    Compute Cov(X,Y).

    Cov(X,Y) = E[XY] - E[X]*E[Y]
    """
    pass


def correlation_xy():
    """
    Compute correlation coefficient:

    rho_XY = Cov(X,Y) / sqrt( Var(X) * Var(Y) )
    """
    pass


def variance_sum():
    """
    Compute Var(X+Y).
    """
    pass


def variance_identity_check():
    """
    Verify:

    Var(X+Y) = Var(X) + Var(Y) + 2*Cov(X,Y)

    Return True if the identity holds, else False.
    """
    pass
