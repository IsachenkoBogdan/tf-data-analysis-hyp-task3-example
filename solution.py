import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 683820405 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    return ttest_1samp(x, 300, alternative='less').pvalue < 0.08 
