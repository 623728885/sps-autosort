import pandas as pd
import numpy as np


def read_ob(ob_file_path):
    ob_file = pd.read_csv(ob_file_path, header=None, engine='python', error_bad_lines=False)
    return ob_file


if __name__ == '__main__':
    ob = read_ob('./ob1')
    print(0)
