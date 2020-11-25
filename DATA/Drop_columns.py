# 필요없는 컬럼을 삭제해 용량을 줄임

import os.path
import pandas as pd
import numpy as np

str_list = ['08' ,'09' ,'10' ,'11' ,'12' ,'13' ,'14' ,'15' ,'16' ,'17']
drop_data = ["big_log_id", "location_x", "location_y", "location_z", "target", "target_account", "worldnum", "item_uid", "etc_str2", "etc_str3", "etc_num3", "etc_num4", "etc_num5", "etc_num6", "etc_num9", "etc_num10", "etc_num11", "etc_num13", "etc_num14", "etc_num15"]

for s in str_list:
    fname = 'log_201005' + s
    chk = '/home/tfir/KJS/labelLog/' + fname + '.csv'
    if os.path.isfile(chk):
        log = pd.read_csv(chk, low_memory=False)
        log.drop(drop_data, axis=1, inplace = True)
        log.to_csv('/home/tfir/KJS/FinalLog/labelLog/dropcol/' + fname + '.csv', index=False)
