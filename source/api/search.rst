検索 API
===========

URL
---

.. code-block::

   POST /DD/ando.php?a=search


.. list-table:: QueryString
   :widths: auto
   :header-rows: 1

   * - キー
     - 値の設定
   * - FindWay
     - :ref:`FindWay` を参照
   * - q
     - | 省略可能
       | WCQ 検索式を BASE64 ('base64url' encoding) でエンコードしたもの
       | :ref:`wcq_section` を参照
   * - userid
     - | 省略可能
       | 未登録呼び出し対象の担当者 ID
   * - start
     - | 省略可能
       | スキップ件数。0 の場合、最初から表示

.. _FindWay:

FindWay の指定
-------------------------------------

FindWay の指定により、検索条件の設定方法が変化します。

.. list-table:: FindWay 許容値
  :widths: auto
  :header-rows: 1

  * - 設定値
    - 検索方法
  * - ``kw``
    - | キーワード検索で検索
      | :ref:`kw` を参照
  * - ``c``
    - | カスタム検索 1 で検索
      | :ref:`c` を参照
  * - ``c2``
    - | カスタム検索 2 で検索

.. _kw:

キーワード検索での条件指定
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

キーワード検索をしたい場合の指定です。

.. list-table:: 追加の QueryString
   :widths: auto
   :header-rows: 1

   * - キー
     - 値の設定
   * - KeywordSearch-FTS
     - | 省略可能
       | ``1`` の場合「全文検索を含む」オン
   * - KeywordSearch
     - キーワード検索のキーワード

.. _c:

カスタム検索 1 での条件指定
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

カスタム検索 (旧式) をしたい場合の指定です。

.. include:: custom1.txt

.. _s-cond:

文字列項目の検索条件
^^^^^^^^^^^^^^^^^^^^^^^^^^^

詳細については :ref:`wcq-opecodes` を参照

.. list-table:: condition 値
  :widths: auto
  :header-rows: 1

  * - 値
    - 動作
  * - ``s,contain``
    - ``を含む`` 検索
  * - ``s,notcontained``
    - ``を含まない`` 検索
  * - ``s,startswith``
    - ``から始まる`` 検索
  * - ``s,endswith``
    - ``で終わる`` 検索
  * - ``s,isempty``
    - ``空白`` 検索
  * - ``s,isnotempty``
    - ``空白でない`` 検索
  * - ``s,is``
    - ``完全一致`` 検索
  * - ``f,geq``
    - ``以上の数値`` 検索
  * - ``f,leq``
    - ``以下の数値`` 検索

.. _d-cond:

日付項目の検索条件
^^^^^^^^^^^^^^^^^^^^^^^^^^^

詳細については :ref:`wcq-opecodes` を参照

.. list-table:: condition 値
  :widths: auto
  :header-rows: 1

  * - 値
    - 動作
  * - ``d,is``
    - ``と等しい日付`` 検索
  * - ``d,between``
    - ``右の日付けまで`` 検索
  * - ``d,leq``
    - ``よりも前の日付`` 検索
  * - ``d,geq``
    - ``よりも後の日付`` 検索
  * - ``d,isnot``
    - ``以外の日付`` 検索

.. _i-cond:

整数項目の検索条件
^^^^^^^^^^^^^^^^^^^^^^^^^^^

詳細については :ref:`wcq-opecodes` を参照

.. list-table:: condition 値
  :widths: auto
  :header-rows: 1

  * - 値
    - 動作
  * - ``i,is``
    - ``等しい`` 検索
  * - ``i,isnot``
    - ``等しくない`` 検索


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

HTML で表示されます。

API 用の場合、XXX に JSON を返します。``<!-- <mydd:ando>XXX</mydd:ando> -->``

.. code-block:: JSON

   {
      "f":"thumbnail",
      "cntTotal":"総件数",
      "cntRecords":"ヒット件数",
      "start":"スキップ件数",
      "needNext":"次へがある場合 1",
      "cntPrev":"検索結果より前にある件数",
      "cntNext":"検索結果より後にある件数",
      "recs":[
         {
            "id":"書類 ID",
            "modifydate":"更新日",
            "createdate":"作成日",
            "title":"項目 1",
            "campanyname":"会社名",
            "project":"項目 2",
            "usercustomitem1":"項目 3",
            "usercustomitem2":"項目 4",
            "usercustomitem3":"項目 5",
            "usercustomitem4":"項目 6",
            "usercustomitem5":"項目 7",
            "memo":"コメント欄",
            "exeword":"拡張子",
            "fp":"書類ダウンロード用 URL の一部",
            "tget_query":"サムネイル取得用 URL",
            "IsDLAllowed":"ダウンロード許可の場合 1"
         }
      ]
   }
