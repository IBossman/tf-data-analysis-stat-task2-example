import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 563165218 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # p - уровень доверия
    # x - массив уровней значимости
    # alpha - уровень значимости
    
    alpha = 1 - p
    loc = x.mean()
    quantile = alpha
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * quantile, \
           loc - scale * quantile
