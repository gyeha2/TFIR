# 최종 피쳐 선정

import pandas as pd
import os
import numpy as np

I = "Player_information.csv"
A = "Player_action.csv"
G = "Group_activity.csv"

columns = ["actor_account", "login_count", "play_time", "max_level", "playtime_per_day", "abyss", "sit_count", "teleport_count", "reborn_count", "social_deal", "sit_count_perday", "use_portal_count_perday", "teleport_count_perday", "total_party_time", "sit_count/play_time", "killed_by_pc/play_time", "killed_by_npc/play_time", "total_party_time/play_time", "teleport_count/play_time", "social_deal/play_time", "play_time/login_count", "reborn_count/login_count", "sit_count/max_level", "play_time/question_count", "class"] # label일ㄸㅐ 클래스넣어주기
change_columns = ["actor_account", "login_count", "playtime", "level", "playtime_per_day", "abyss_level", "sit", "teleport", "reborn", "social_deal", "sit_per_day", "portal_use_per_day", "teleport_per_day", "party_time", "sit_per_playtime", "pk_per_playtime", "npk_per_playtime", "partytime_per_playtime", "teleport_per_playtime", "social_deal_per_playtime", "playtime_per_login", "reborn_per_login", "sit_per_leveling", "playtime_per_quest", "class"]
drop_columns = ["login_day_count", "exp_get_amount", "item_get_count", "killed_by_pc", "killed_by_npc", "exp_repair_count", "money_get_count", "use_portal_count", "question_count", "logout_count", "avg_money", "ip_count", "guild_join_count", "average_party"]

df1 = pd.read_csv(I)
df2 = pd.read_csv(A)
df2.drop(["class"], axis=1, inplace=True)
df3 = pd.read_csv(G)
df3.drop(["class"], axis=1, inplace=True)

alpha = pd.merge(df1, df2, on="actor_account", how="outer")
alpha = pd.merge(alpha, df3, on="actor_account", how="outer")

alpha["sit_count_perday"] = alpha["sit_count"] / alpha["login_day_count"]
alpha["use_portal_count_perday"] = alpha["use_portal_count"] / alpha["login_day_count"]
alpha["sit_count/play_time"] = alpha["sit_count"] / alpha["play_time"]
alpha["killed_by_pc/play_time"] = alpha["killed_by_pc"] / alpha["play_time"]
alpha["killed_by_npc/play_time"] = alpha["killed_by_npc"] / alpha["play_time"]
alpha["total_party_time/play_time"] = alpha["total_party_time"] / alpha["play_time"]
alpha["teleport_count/play_time"] = alpha["teleport_count"] / alpha["play_time"]
alpha["social_deal/play_time"] = alpha["social_deal"] / alpha["play_time"]
alpha["play_time/login_count"] = alpha["play_time"] / alpha["login_count"]
alpha["reborn_count/login_count"] = alpha["reborn_count"] / alpha["login_count"]
alpha["sit_count/max_level"] = alpha["sit_count"] / alpha["max_level"]
alpha["play_time/question_count"] = alpha["play_time"] / alpha["question_count"]
alpha["playtime_per_day"] = alpha["play_time"] / alpha["login_day_count"]
alpha["teleport_count_perday"] = alpha["teleport_count"] / alpha["login_day_count"]

alpha.drop(drop_columns, axis=1, inplace=True)
alpha = alpha[columns]
alpha.columns = change_columns

alpha[alpha==np.inf] = np.nan
alpha.fillna(0, inplace=True)

alpha.to_csv("alpha.csv", index=False, encoding='utf8')
