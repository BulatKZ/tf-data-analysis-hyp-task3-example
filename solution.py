import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 1612072510 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    threshold = -300
    t_stat, p_val = stats.ttest_1samp(x, threshold)
    if p_val < 0.04:
        #print("Отклоняем нулевую гипотезу")
        return False
    else:
        return True
        #print("Не отклоняем нулевую гипотезу")
    #return ... # Ваш ответ, True или False
