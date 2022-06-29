import pandas as pd
import numpy as np


def sps_read(mode, s_file_path, r_file_path, x_file_path):
    if mode == 'sx':
        return read_shot(s_file_path), read_x(x_file_path)
    if mode == 'all':
        return read_shot(s_file_path), read_rec(r_file_path), read_x(x_file_path)


def read_shot(s_file_path):
    s_file = pd.read_csv(s_file_path, header=None)
    s_head_num = 0
    for i in range(s_file.shape[0]):
        if s_file.loc[i][0][0] == 'H':
            s_head_num += 1
        else:
            break

    s_head = s_file[0:s_head_num]
    s_file = s_file.drop(s_file.index[0:s_head_num])
    s_column_name = {
        'sign': 1,
        'shot_line': 10,
        'shot_point': 10,
        'index': 3,
        'code': 2,
        'static': 4,
        'deep': 4,
        'base_level': 4,
        'tb': 2,
        'water_deep': 6,
        'X': 9,
        'Y': 10,
        'elevation': 6,
        'date': 3,
        'time': 6
    }
    df_s = pd.DataFrame(columns=s_column_name.keys())
    step = 0
    for col in s_column_name:
        df_s[col] = s_file[0].str.slice(start=step, stop=step + s_column_name[col])
        step += s_column_name[col]
    return df_s, s_head


def read_rec(r_file_path):
    # 头文件含多个分隔符要使用sep=None，不含多个则用默认参数，使用了sep=None会导致读取内容出错
    r_file = pd.read_csv(r_file_path, header=None, sep=None)
    r_head_num = 0
    for i in range(r_file.shape[0]):
        if r_file.loc[i][0][0] == 'H':
            r_head_num += 1
        else:
            break

    r_head = r_file[0:r_head_num]
    r_file = r_file.drop(r_file.index[0:r_head_num])
    r_column_name = {
        'sign': 1,
        'rec_line': 10,
        'rec_point': 10,
        'index': 3,
        'code': 2,
        'static': 4,
        'deep': 4,
        'base_level': 4,
        'tb': 2,
        'water_deep': 6,
        'X': 9,
        'Y': 10,
        'elevation': 6,
        'date': 3,
        'time': 6
    }
    df_r = pd.DataFrame(columns=r_column_name.keys())
    step = 0
    for col in r_column_name:
        df_r[col] = r_file[0].str.slice(start=step, stop=step + r_column_name[col])
        step += r_column_name[col]
    return df_r, r_head


def read_x(x_file_path):
    x_file = pd.read_csv(x_file_path, header=None)
    x_head_num = 0
    for i in range(x_file.shape[0]):
        if x_file.loc[i][0][0] == 'H':
            x_head_num += 1
        else:
            break

    x_head = x_file[0:x_head_num]
    x_file = x_file.drop(x_file.index[0:x_head_num])
    x_column_name = {
        'sign': 1,
        'tape_num': 6,
        'ff_id': 8,
        'record_increment': 1,
        'equipment_code': 1,
        'shot_line': 10,
        'shot_point': 10,
        'index': 1,
        'start_channel': 5,
        'end_channel': 5,
        'channel_increment': 1,
        'receiver_line': 10,
        'start_receiver_point': 10,
        'end_receiver_point': 10,
        'receiver_index': 1
    }
    df_x = pd.DataFrame(columns=x_column_name.keys())
    step = 0
    for col in x_column_name:
        df_x[col] = x_file[0].str.slice(start=step, stop=step + x_column_name[col])
        step += x_column_name[col]
    return df_x, x_head


def read_ob(ob_file_path):
    pass


def sps_out(df, head):
    df_out = df.iloc[:, 0].str.cat(others=[df.iloc[:, i] for i in range(1, len(df.columns))], sep=None)
    df_out = pd.concat([head, df_out])
    df_out.to_csv('shot.S', header=False, index=False)


file_path = 'C:/Users/xia/Downloads/秀水三维/sps/仪器-炮后/'


if __name__ == '__main__':
    (s, s_head), (x, x_head) = sps_read('sx', './s.S', './r.R', './x.X')
    print(0)



