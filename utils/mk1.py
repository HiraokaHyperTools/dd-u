#!/usr/bin/python3.9

import string
import os
import sys
import io

thisDir = os.path.dirname(os.path.realpath(__file__))


def loadTemplate(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def resolveTemplate(template, records):
    writer = io.StringIO()
    for record in records:
        print(
            string.Template(template).safe_substitute(record),
            file=writer
        )
    return writer.getvalue()


def star_map(callback, array_items):
    return map(
        lambda array_item: callback(*array_item),
        array_items
    )



root = {
    "out5": resolveTemplate(
        loadTemplate(os.path.join(thisDir, 'temp5.txt')),
        star_map(
            lambda key, disp: ({
                "key": "V" + key,
                "cond": "C" + key,
                "disp": disp,
            }),
            [
                ["group_id", "グループ ID"]
            ]
        )
    ),

    "out1": resolveTemplate(
        loadTemplate(os.path.join(thisDir, 'temp1.txt')),
        star_map(
            lambda key, disp: ({
                "key": "V" + key,
                "cond": "C" + key,
                "disp": disp,
            }),
            [
                ["createuserid", "登録者 ID"],
                ["adminuserid", "承認者 ID"],
            ]
        )
    ),

    "out2": resolveTemplate(
        loadTemplate(os.path.join(thisDir, 'temp2.txt')),
        star_map(
            lambda key1, disp, cond, key2: ({
                "key1": key1,
                "disp": disp,
                "cond": cond,
                "key2": key2,
            }),
            [
                ["DateInput", "登録日付", "DateInputCondition", "DateInput2"],
                ["DateUpdate", "更新日付", "DateUpdateCondition", "DateUpdate2"],
                ["DateDeadline", "提出期限", "DateDeadlineCondition", "DateDeadline2"],
                ["DateUser", "ユーザー日付", "DateUserCondition", "DateUser2"],
            ]
        )
    ),

    "out3": resolveTemplate(
        loadTemplate(os.path.join(thisDir, 'temp3.txt')),
        star_map(
            lambda key, disp: ({
                "key1": "V" + key,
                "key2": "V" + key + "_2",
                "cond": "C" + key,
                "disp": disp,
            }),
            [
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
        )
    ),

    "out4": resolveTemplate(
        loadTemplate(os.path.join(thisDir, 'temp4.txt')),
        star_map(
            lambda key, disp: ({
                "key": "V" + key,
                "disp": disp,
            }),
            [
                ["group_only", "グループ専属書類"],
                ["f_individual", "個人書類"],
                ["f_secret", "丸秘書類"],
                ["f_handin", "提出済み書類"],
            ]
        )
    ),
}

with open(
    os.path.join(thisDir, '../source/api/custom1.txt'),
    'w',
    encoding='utf-8'
) as writer:
    print(
        string.Template(
            loadTemplate(
                os.path.join(thisDir, 'mk1.txt')
            )
        ).safe_substitute(root),
        file=writer
    )
