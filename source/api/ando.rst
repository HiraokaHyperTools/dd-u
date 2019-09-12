Ando 能力
===========

URL
---

.. code-block::

   POST /DD/ando.php?a=ando

HTTP リクエストヘッダー
---------------------------

特になし

HTTP リクエストボディー
---------------------------

特になし


HTTP レスポンスヘッダー
---------------------------

特になし

HTTP レスポンスボディー
---------------------------

JSON 交じりの HTML で出力します。

.. code-block:: html

   <html><body><!-- <mydd:ando>XXX</mydd:ando> --></body></html>

XXX の部分に JSON が入ります。

JSON の構成:

.. code-block::

   {
      "feat": {
         "mydd:ando":1,
         "0.1":1,
         ...
      },
      "PRO4_CORP_NAME": "",
      "PRO4_VER": "4.2.xxx"
   }

feat の概要
^^^^^^^^^^^^^^^^^

* デジタルドルフィンズのバージョンアップにより、機能が増えていきます。
* ``"mydd:ando":1`` の場合は、mydd:ando を備えていることを意味します。
* ``"mydd:ando":0`` は使用しません。項目そのものが無くなります。

feat 一覧
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: auto
   :header-rows: 1

   * - キー
     - 意味
   * - mydd:ando
     - Ando 機能に対応
   * - 0.1
     - 同上
   * - uname
     - f=search の時に、uname:"担当者名" を追加します
   * - oc2
     - おしらせ～る 2 に対応
   * - LongStr
     - WCQ が LongStr に対応
   * - X-mrRes
     - 一部アクションの結果を HTTP レスポンスヘッダ X-mrRes に整数で設定します
   * - anr:fp
     - ``js.php?a=anr`` で、``{"fp": "ファイルパス", "relfp": "相対ファイルパス"}`` を追加で返します
   * - replace_js:newmt
     - ``core.php?a=replace_js`` で、``$_REQUEST["newmt"]`` が非 FALSE の場合、書類の更新日時を更新します。
   * - u:approver
     - ``js.php?a=lgu`` で、``approver`` を返します。
   * - s,equals
     - WCQ 検索式で ``s,equals`` に対応。
