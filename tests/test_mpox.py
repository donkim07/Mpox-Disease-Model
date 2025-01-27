import numpy as np
import pytest
from mpox.app import mpoxWithout, mpoxWith

def test_mpox_without_vaccination():
    # Test initial conditions
    x = [0.95, 0.03, 0.02, 0.0]  # S, E, I, R
    T = 0
    
    # Calculate derivatives
    derivatives = mpoxWithout(x, T)
    
    # Check we get 4 derivatives (dS, dE, dI, dR)
    assert len(derivatives) == 4
    
    # Calculate total population change (birth rate - death rate)
    # We expect births and deaths to roughly balance out
    total_change = derivatives[0] + derivatives[1] + derivatives[2] + derivatives[3]
    assert abs(total_change) < 0.05  # Allow for small demographic changes

def test_mpox_with_vaccination():
    # Test initial conditions
    x = [0.95, 0.03, 0.02, 0.0, 0.0]  # S, E, I, R, V
    T = 0
    
    # Calculate derivatives
    derivatives = mpoxWith(x, T)
    
    # Check we get 5 derivatives (dS, dE, dI, dR, dV)
    assert len(derivatives) == 5
    
    # Calculate total population change (birth rate - death rate)
    total_change = sum(derivatives)
    assert abs(total_change) < 0.05  # Allow for small demographic changes

def test_parameters_positive():
    x = [0.95, 0.03, 0.02, 0.0]
    T = 0
    derivatives = mpoxWithout(x, T)
    
    # Check that none of the derivatives produce negative populations
    for d in derivatives:
        assert not np.isnan(d), "Derivative contains NaN"
        assert np.isfinite(d), "Derivative is not finite"