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
    
    # Check conservation of population (sum of derivatives should be close to 0)
    assert abs(sum(derivatives)) < 1e-10

def test_mpox_with_vaccination():
    # Test initial conditions
    x = [0.95, 0.03, 0.02, 0.0, 0.0]  # S, E, I, R, V
    T = 0
    
    # Calculate derivatives
    derivatives = mpoxWith(x, T)
    
    # Check we get 5 derivatives (dS, dE, dI, dR, dV)
    assert len(derivatives) == 5
    
    # Check conservation of population (sum of derivatives should be close to 0)
    assert abs(sum(derivatives)) < 1e-10