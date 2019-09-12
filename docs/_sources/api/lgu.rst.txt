ListGroupUsers
==============

URL
---

.. code-block::

   GET /DD/js.php?a=lgu

HTTP レスポンスボディー
-----------------------

:ref:`setJson2R<js-json>`

.. code-block:: text

   {
      "users": users,
      "groups": groups,
      "PRO4_OC2_ATTS":"おしらせ～る II 項目名"
   }

users につきまして
^^^^^^^^^^^^^^^^^^^^^^

担当者情報の配列です。担当者 1 名分の情報：

.. code-block:: text

   {
      "id": ログイン ID,
      "name": 担当者名,
      "syscd": 担当者の内部コード,
      "isa": 管理者フラグ 0 or 1 (r3535 以降),
      "nop": ノーパス 0 or 1,
      "bg": belongingGroupIds,
      "dg": defaultGroupId,
      "userdir": 登録フォルダ(r3466 以降),
      "approver": 承認者フラグ 0 or 1 (r3535 以降)
   }

belongingGroupIds につきまして
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

所属しているグループ ID の配列です。例: ``[1, 2, 3]``

defaultGroupId につきまして
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

デフォルトグループの ID です。例: ``1``

未設定の場合は ``-1``

groups につきまして
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

グループ情報の配列です。グループ 1 個分の情報

.. code-block:: text

   {
      "id": グループ ID,
      "name": グループ名,
      "o": グループ専属書類 0 or 1,
      "f1": 項目 1 の名称,
      "f2": 項目 2 の名称,
      "f3": 項目 3 の名称,
      "f4": 項目 4 の名称,
      "f5": 項目 5 の名称,
      "f6": 項目 6 の名称,
      "f7": 項目 7 の名称,
      "userDate": 日付欄の名称,
      "company": 取引先欄の名称,
      "memo": コメント欄の名称
   }

