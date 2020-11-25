# 로그 파일을 필요한 피쳐만 뽑아 정렬

import os.path
import pandas as pd
import numpy as np

str_list = ['08' ,'09' ,'10' ,'11' ,'12' ,'13' ,'14' ,'15' ,'16' ,'17']
type_list = [34, 36, 39, 42, 44, 58, 59, 76, 77, 98, 99]
#drop_data = ["big_log_id", "target", "target_account", "worldnum", "item_uid", "etc_str2", "etc_str3", "etc_num3", "etc_num4", "etc_num5", "etc_num6", "etc_num9", "etc_num10", "etc_num11", "etc_num13", "etc_num14", "etc_num15"]

for s in str_list:
    fname = 'log_201005' + s
    chk = '/home/tfir/KJS/FinalLog/testLog/etc/dropcol/' + fname + '.csv'
    if os.path.isfile(chk):
        log = pd.read_csv(chk, low_memory=False)
 #       log.drop(drop_data, axis=1, inplace = True)

# Player Action
        login_count = log.loc[log.log_id==103].groupby('actor_account').count()['log_id']
        logout_count = log.loc[log.log_id==104].groupby('actor_account').count()['log_id']
        play_time = log.loc[log.log_id==104].groupby('actor_account').sum()['etc_num7']
        money_up = log.loc[log.log_id==187].groupby('actor_account').sum()['etc_num8']
        money_down = log.loc[log.log_id==188].groupby('actor_account').sum()['etc_num8']
        ip_count = log.loc[log.log_id==103].groupby('actor_account').count()['etc_str1']
        max_level_a = log.loc[log.log_id==113].groupby('actor_account').max()['etc_num2']
        max_level_b = log.loc[log.log_id==103].groupby('actor_account').max()['etc_num2']
        max_level = pd.merge(max_level_a, max_level_b, on='actor_account', how='outer').fillna(0).max(axis=1)
        max_level.name = 'etc_num2'
        log_tmp = log.loc[log.log_id.isin([187, 188])]
        social_deal = log_tmp.loc[log_tmp.etc_num7.isin(type_list)].groupby("actor_account").count()["etc_num7"]

#        money_change = pd.merge(money_up, money_down, on='actor_account', how='outer').fillna(0)
#        money_change['change'] = money_change['etc_num8_x'] - money_change['etc_num8_y']
#        money_change.drop(['etc_num8_x', 'etc_num8_y'], axis=1, inplace=True)
#        tmp = pd.merge(money_change, play_time, on='actor_account', how='right')
#        tmp['result'] = tmp['change'] / tmp['etc_num7']
#        tmp.drop(['change', 'etc_num7'], axis=1, inplace=True)
#        avg_money = tmp
        login_day_count = login_count.copy()
        tmp2=pd.DataFrame(login_day_count)
        tmp2['result'] = 1
        tmp2.drop(['log_id'], axis=1, inplace=True)
        login_day_count = tmp2
        Player_information = pd.merge(login_count, logout_count, on='actor_account', how='outer')
        Player_information = pd.merge(Player_information, login_day_count, on='actor_account', how='outer')
        Player_information = pd.merge(Player_information, play_time, on='actor_account', how='outer')       
        Player_information = pd.merge(Player_information, money_up, on='actor_account', how='outer') 
        Player_information = pd.merge(Player_information, money_down, on='actor_account', how='outer') 
#        Player_information = pd.merge(Player_information, avg_money, on='actor_account', how='outer')
        Player_information = pd.merge(Player_information, ip_count, on='actor_account', how='outer')
        Player_information = pd.merge(Player_information, max_level, on='actor_account', how='outer')
        Player_information = pd.merge(Player_information, social_deal, on='actor_account', how='outer')

        Player_information.columns = ["login_count", "logout_count", "login_day_count", "play_time", "money_up", "money_down", "ip_count", "max_level", "social_deal"]
        Player_information.fillna(0, inplace=True)

# Player Action
        sit_count = log.loc[log.log_id==118].groupby('actor_account').count()['log_id']
        exp_get_amount = log.loc[log.log_id==143].groupby('actor_account').sum()['etc_num7']
        item_get_count = log.loc[log.log_id==202].groupby('actor_account').sum()['etc_num1']
        exp_repair_count = log.loc[log.log_id==148].groupby('actor_account').count()['log_id']
        money_get_count = log.loc[log.log_id==187].groupby('actor_account').count()['log_id']
        abyss = log.loc[log.log_id==719].groupby('actor_account').max()['etc_num8']
        use_portal_count = log.loc[log.log_id==151].groupby('actor_account').count()['log_id']
        killed_by_pc = log.loc[log.log_id==137].groupby('actor_account').count()['log_id']
        killed_by_npc = log.loc[log.log_id==138].groupby('actor_account').count()['log_id']
        teleport_count = log.loc[log.log_id==142].groupby('actor_account').count()['log_id']
        reborn_count = log.loc[log.log_id==145].groupby('actor_account').count()['log_id']
        question_count = log.loc[log.log_id==504].groupby('actor_account').count()['log_id']

        Player_action = pd.merge(sit_count, exp_get_amount, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, item_get_count, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, exp_repair_count, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, money_get_count, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, abyss, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, use_portal_count, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, killed_by_pc, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, killed_by_npc, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, teleport_count, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, reborn_count, on='actor_account', how='outer')
        Player_action = pd.merge(Player_action, question_count, on='actor_account', how='outer')

        Player_action.columns = ["sit_count", "exp_get_amount", "item_get_count", "exp_repair_count", "money_get_count", "abyss", "use_portal_count", "killed_by_pc", "killed_by_npc", "teleport_count", "reborn_count", "question_count"]
        Player_action.fillna(0, inplace=True)

# Group Activity
        total_party_time = log.loc[log.log_id==127].groupby('actor_account').sum()['etc_num12']
        group_join_count = log.loc[log.log_id==605].groupby('actor_account').count()['log_id']

        out_count = log.loc[log.log_id==127].groupby('actor_account').count()['log_id']

#        tmp3 = pd.merge(total_party_time, out_count, on='actor_account', how='outer')
#        tmp3['result'] = tmp3['etc_num12'] / tmp3['log_id']
#        tmp3.drop(['etc_num12', 'log_id'], axis=1, inplace=True)
#        average_party = tmp3

        g1=log.loc[log.log_id==601].groupby('actor_account').count()['log_id']
        g2=log.loc[log.log_id==602].groupby('actor_account').count()['log_id']
        g3=log.loc[log.log_id==603].groupby('actor_account').count()['log_id']
        g4=log.loc[log.log_id==604].groupby('actor_account').count()['log_id']
        g5=log.loc[log.log_id==605].groupby('actor_account').count()['log_id']
        g6=log.loc[log.log_id==606].groupby('actor_account').count()['log_id']
        g7=log.loc[log.log_id==607].groupby('actor_account').count()['log_id']
        g8=log.loc[log.log_id==608].groupby('actor_account').count()['log_id']
        g9=log.loc[log.log_id==609].groupby('actor_account').count()['log_id']
        g10=log.loc[log.log_id==610].groupby('actor_account').count()['log_id']
        g11=log.loc[log.log_id==611].groupby('actor_account').count()['log_id']
        g12=log.loc[log.log_id==612].groupby('actor_account').count()['log_id']

        G = pd.merge(g1, g2, on='actor_account', how='outer')
        G = pd.merge(G, g3, on='actor_account', how='outer')
        G = pd.merge(G, g4, on='actor_account', how='outer')
        G = pd.merge(G, g5, on='actor_account', how='outer')
        G = pd.merge(G, g6, on='actor_account', how='outer')
        G = pd.merge(G, g7, on='actor_account', how='outer')
        G = pd.merge(G, g8, on='actor_account', how='outer')
        G = pd.merge(G, g9, on='actor_account', how='outer')
        G = pd.merge(G, g10, on='actor_account', how='outer')
        G = pd.merge(G, g11, on='actor_account', how='outer')
        G = pd.merge(G, g12, on='actor_account', how='outer')

        G.fillna(0)
        G['S'] = G.sum(axis=1)

        Group_activity = pd.merge(total_party_time, group_join_count, on='actor_account', how='outer')
        Group_activity = pd.merge(Group_activity, out_count, on='actor_account', how='outer')
#        Group_activity = pd.merge(Group_activity, average_party, on='actor_account', how='outer')
        Group_activity.columns = ["total_party_time", "guild_join_count", "out_count"] 
        Group_activity.fillna(0, inplace=True)

    Player_information.to_csv("/home/tfir/KJS/FinalLog/Player_information/" + fname + ".csv", encoding="utf8")
    Player_action.to_csv("/home/tfir/KJS/FinalLog/Player_action/" + fname + ".csv", encoding="utf8")
    Group_activity.to_csv("/home/tfir/KJS/FinalLog/Group_activity/" + fname + ".csv", encoding="utf8")
    print("One to_csv complete")
