import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 683820405 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p_value = ttest_1samp(x, 300)[1]
    alpha = 0.08
    p_value /= 2
    
    if np.mean(x) >= 300:
        return False
    
    return p_value < alpha
