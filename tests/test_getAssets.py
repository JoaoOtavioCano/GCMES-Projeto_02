from backend.getAssets import calculateGainLossPercentage

import math

def test_calculateGainLossPercentage():
    assert math.isclose(calculateGainLossPercentage(11, 10), 10)
    assert math.isclose(calculateGainLossPercentage(9, 10), -10)
    assert math.isclose(calculateGainLossPercentage(10, 10), 0)