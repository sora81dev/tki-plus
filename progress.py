import tqdm
from tqdm.notebook import trange
import numpy as np
import time

def bsar(n):
    for i in range(n):
        bar = '■'*i + "."*(n-i)
        print(f"\r\033[K[\033[33m{bar}\033[39m] {i/n*100:.02f}% ({i}/{n})", end="")
        time.sleep(0.5)

def new_progress(long, slp=1):
    """
    Explain:
    This function creates a progress bar.
    If you're jupyter user, you can use jupyter_progress func.

    Args:
    parameter1 (int)       : This parameter must be set. (Func name: long)
                             This is length of the progress bar.
    parameter2 (float, int): You do not need to set this parameter. (Func name: slp)
                             Default value is 1.
                             This is the time per progress. (Unit: seconds)

    Return:
    None
    """

    for i in tqdm.tqdm(range(int(long))):
        time.sleep(slp)

def jupyter_progress(long, slp=1):
    """
    Explain:
    This function creates a progress bar.
    ※If you're not jupyter user, you mustn't use jupyter_progress func.

    Args:
    parameter1 (int)       : This parameter must be set. (Func name: long)
                             This is length of the progress bar.
    parameter2 (float, int): You do not need to set this parameter. (Func name: slp)
                             Default value is 1.
                             This is the time per progress. (Unit: seconds)

    Return:
    None
    """

    for i in trange(long, leave=False):
        time.sleep(slp)