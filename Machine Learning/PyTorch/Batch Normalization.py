import numpy as np
from typing import Tuple, List


class Solution:
    def batch_norm(self, x: List[List[float]], gamma: List[float], beta: List[float],
                   running_mean: List[float], running_var: List[float],
                   momentum: float, eps: float, training: bool) -> Tuple[List[List[float]], List[float], List[float]]:
        # During training: normalize using batch statistics, then update running stats
        # During inference: normalize using running stats (no batch stats needed)
        # Apply affine transform: y = gamma * x_hat + beta
        # Return (y, running_mean, running_var), all rounded to 4 decimals as lists
        x = np.array(x)
        gamma = np.array(gamma)
        beta = np.array(beta)
        running_mean = np.array(running_mean)
        running_var = np.array(running_var)
        eps = 1e-5
        m = 0.1

        if training == False:
            x_norm = (x - running_mean) / np.sqrt(running_var + eps)
        else:
            mean_x = np.mean(x, axis=0)
            var_x = np.var(x, axis=0)
            x_norm = (x - mean_x) / np.sqrt(var_x + eps)
            running_mean = (1 - m) * running_mean + m * mean_x
            running_var = (1 - m) * running_var + m * var_x
        
        y = np.round(gamma * x_norm + beta, 4)
        running_mean = np.round(running_mean, 4)
        running_var = np.round(running_var, 4)
        return (y.tolist(), running_mean.tolist(), running_var.tolist())

        
