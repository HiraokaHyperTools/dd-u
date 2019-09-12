書類登録 API
================

概要
----

書類 ID を作成します

URL
---

.. code-block::

   POST /DD/js.php?a=anr


HTTP リクエストボディー
-----------------------

.. list-table:: QueryString
   :widths: auto
   :header-rows: 1

   * - Key
     - value
   * - exeword
     - 拡張子。"フォルダ"の場合は、空のフォルダー書類を登録します。
   * - group_id
     - グループ ID
   * - createuserid
     - 登録担当者 ID
   * - adminuserid
     -
   * - campanyname
     -
   * - title
     -
   * - project
     -
   * - usercustomitem1
     -
   * - usercustomitem2
     -
   * - usercustomitem3
     -
   * - usercustomitem4
     -
   * - usercustomitem5
     -
   * - memo
     -
   * - drawingplanno
     - 20 文字まで
   * - systemid
     - 20 文字まで
   * - oldfilename
     - 80 文字まで
   * - limitdate
     -
   * - userdate
     -
   * - group_only
     -
   * - f_individual
     -
   * - f_handin
     -
   * - Vf_secret
     -
   * - REG
     - 1 の場合、登録済みにします。それ以外は、未登録になります。

HTTP レスポンスボディー
-----------------------

:ref:`setJson2R<js-json>`

JSON

.. code-block:: JSON

   {
      "id": "id",
      "fp": "fp",
      "relfp": "relfp"
   }
