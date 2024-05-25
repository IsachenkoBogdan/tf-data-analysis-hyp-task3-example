import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 683820405 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.08
    return ztest(x, value=300, alternative='larger')[1] < alpha
