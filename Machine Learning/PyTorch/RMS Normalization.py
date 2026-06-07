import numpy as np
from typing import List


class Solution:
    def rms_norm(self, x: List[float], gamma: List[float], eps: float) -> List[float]:
        # Implement RMS Normalization (similar to LayerNorm but without mean centering or beta)
        # Normalize x, then scale by gamma
        # Return result rounded to 4 decimal places as a list
        x = np.array(x)
        gamma = np.array(gamma)

        rms = np.sqrt(np.mean(x ** 2) + eps)
        x_norm = x / rms
        y = gamma * x_norm
        return np.round(y, 4).tolist()

#It is similar to Layer Normalization but without mean centering or beta. Instead of normalizing by the standard deviation, we normalize by the root mean square (RMS) of the input. The formula for RMS Normalization is:
#x_norm = x / sqrt(mean(x^2) + eps)
#y = gamma * x_norm

#it is used in some transformer architectures as an alternative to Layer Normalization, especially in cases where mean centering is not desired. It can help stabilize training and improve convergence in certain scenarios.