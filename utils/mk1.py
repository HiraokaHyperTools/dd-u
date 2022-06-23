#!/usr/bin/python3.9

import string
import os
import sys

baseDir = os.path.dirname(os.path.realpath(__file__))

items5 = [
    ["group_id", "グループ ID"],
]
items1 = [
    ["createuserid", "登録者 ID"],
    ["adminuserid", "承認者 ID"],
]
items2 = [
    ["DateInput", "登録日付", "DateInputCondition", "DateInput2"],
    ["DateUpdate", "更新日付", "DateUpdateCondition", "DateUpdate2"],
    ["DateDeadline", "提出期限", "DateDeadlineCondition", "DateDeadline2"],
    ["DateUser", "ユーザー日付", "DateUserCondition", "DateUser2"],
]
items3 = [
    ["campanyname", "会社名"],
    ["title", "項目 1"],
    ["project", "項目 2"],
    ["usercustomitem1", "項目 3"],
    ["usercustomitem2", "項目 4"],
    ["usercustomitem3", "項目 5"],
    ["usercustomitem4", "項目 6"],
    ["usercustomitem5", "項目 7"],
    ["linkname1", "リンク名称 1"],
    ["linkname2", "リンク名称 2"],
    ["linkname3", "リンク名称 3"],
    ["linkname4", "リンク名称 4"],
    ["linkname5", "リンク名称 5"],
    ["linkpath1", "リンクパス 1"],
    ["linkpath2", "リンクパス 2"],
    ["linkpath3", "リンクパス 3"],
    ["linkpath4", "リンクパス 4"],
    ["linkpath5", "リンクパス 5"],
    ["memo", "コメント"],
]
items4 = [
    ["group_only", "グループ専属書類"],
    ["f_individual", "個人書類"],
    ["f_secret", "丸秘書類"],
    ["f_handin", "提出済み書類"],
]

tofile = sys.stdout

with open(os.path.join(baseDir, 'temp5.txt'), 'r', encoding='utf-8') as f:
    temp5 = f.read()

for (key, disp) in items5:
    print(
        string.Template(temp5).safe_substitute({
            "key": "V" + key,
            "cond": "C" + key,
            "disp": disp,
        }),
        file=tofile
    )


with open(os.path.join(baseDir, 'temp1.txt'), 'r', encoding='utf-8') as f:
    temp1 = f.read()

for (key, disp) in items1:
    print(
        string.Template(temp1).safe_substitute({
            "key": "V" + key,
            "cond": "C" + key,
            "disp": disp,
        }),
        file=tofile
    )


with open(os.path.join(baseDir, 'temp2.txt'), 'r', encoding='utf-8') as f:
    temp2 = f.read()

for (key1, disp, cond, key2) in items2:
    print(
        string.Template(temp2).safe_substitute({
            "key1": key1,
            "disp": disp,
            "cond": cond,
            "key2": key2,
        }),
        file=tofile
    )


with open(os.path.join(baseDir, 'temp3.txt'), 'r', encoding='utf-8') as f:
    temp3 = f.read()

for (key, disp) in items3:
    print(
        string.Template(temp3).safe_substitute({
            "key1": "V" + key,
            "key2": "V" + key + "_2",
            "cond": "C" + key,
            "disp": disp,
        }),
        file=tofile
    )


with open(os.path.join(baseDir, 'temp4.txt'), 'r', encoding='utf-8') as f:
    temp4 = f.read()

for (key, disp) in items4:
    print(
        string.Template(temp4).safe_substitute({
            "key": "V" + key,
            "disp": disp,
        }),
        file=tofile
    )
