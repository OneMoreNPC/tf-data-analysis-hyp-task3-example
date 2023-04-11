import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 49479018

def solution(x: np.array) -> bool: 
    alpha = 0.02
    stat, pval  = ztest(x, value=300, alternative='larger')
    return pval < alpha
