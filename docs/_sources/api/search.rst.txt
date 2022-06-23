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

.. list-table:: 追加の QueryString
  :widths: auto
  :header-rows: 1

  * - キー
    - 値の設定
  * - ``Vid``
    - 書類 ID を指定
  * - ``Cid``
    - | 書類 ID の検索方法
      | :ref:`s-cond` 参照

  * - ``Vgroup_id``
    - | グループ ID を指定
  * - ``Cgroup_id``
    - | グループ ID の検索方法
      | :ref:`i-cond` 参照

  * - ``Vcreateuserid``
    - | 登録者 ID を指定
  * - ``Ccreateuserid``
    - | 登録者 ID の検索方法
      | :ref:`s-cond` 参照

  * - ``Vadminuserid``
    - | 承認者 ID を指定
  * - ``Cadminuserid``
    - | 承認者 ID の検索方法
      | :ref:`s-cond` 参照

  * - ``DateInput``
    - | 登録日付 を指定
      | 日付の範囲を検索する場合は ``DateInput`` に開始日を指定し ``DateInput2`` に終了日を指定
  * - ``DateInputCondition``
    - | 登録日付 の検索方法を指定
      | :ref:`d-cond` 参照

  * - ``DateUpdate``
    - | 更新日付 を指定
      | 日付の範囲を検索する場合は ``DateUpdate`` に開始日を指定し ``DateUpdate2`` に終了日を指定
  * - ``DateUpdateCondition``
    - | 更新日付 の検索方法を指定
      | :ref:`d-cond` 参照

  * - ``DateDeadline``
    - | 提出期限 を指定
      | 日付の範囲を検索する場合は ``DateDeadline`` に開始日を指定し ``DateDeadline2`` に終了日を指定
  * - ``DateDeadlineCondition``
    - | 提出期限 の検索方法を指定
      | :ref:`d-cond` 参照

  * - ``DateUser``
    - | ユーザー日付 を指定
      | 日付の範囲を検索する場合は ``DateUser`` に開始日を指定し ``DateUser2`` に終了日を指定
  * - ``DateUserCondition``
    - | ユーザー日付 の検索方法を指定
      | :ref:`d-cond` 参照

  * - ``Vcampanyname``
    - | 会社名 を指定
      | 数値の範囲を検索する場合は ``Vcampanyname`` に最小値を指定し ``Vcampanyname_2`` に最大値を指定
  * - ``Ccampanyname``
    - | 会社名 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vtitle``
    - | 項目 1 を指定
      | 数値の範囲を検索する場合は ``Vtitle`` に最小値を指定し ``Vtitle_2`` に最大値を指定
  * - ``Ctitle``
    - | 項目 1 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vproject``
    - | 項目 2 を指定
      | 数値の範囲を検索する場合は ``Vproject`` に最小値を指定し ``Vproject_2`` に最大値を指定
  * - ``Cproject``
    - | 項目 2 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vusercustomitem1``
    - | 項目 3 を指定
      | 数値の範囲を検索する場合は ``Vusercustomitem1`` に最小値を指定し ``Vusercustomitem1_2`` に最大値を指定
  * - ``Cusercustomitem1``
    - | 項目 3 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vusercustomitem2``
    - | 項目 4 を指定
      | 数値の範囲を検索する場合は ``Vusercustomitem2`` に最小値を指定し ``Vusercustomitem2_2`` に最大値を指定
  * - ``Cusercustomitem2``
    - | 項目 4 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vusercustomitem3``
    - | 項目 5 を指定
      | 数値の範囲を検索する場合は ``Vusercustomitem3`` に最小値を指定し ``Vusercustomitem3_2`` に最大値を指定
  * - ``Cusercustomitem3``
    - | 項目 5 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vusercustomitem4``
    - | 項目 6 を指定
      | 数値の範囲を検索する場合は ``Vusercustomitem4`` に最小値を指定し ``Vusercustomitem4_2`` に最大値を指定
  * - ``Cusercustomitem4``
    - | 項目 6 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vusercustomitem5``
    - | 項目 7 を指定
      | 数値の範囲を検索する場合は ``Vusercustomitem5`` に最小値を指定し ``Vusercustomitem5_2`` に最大値を指定
  * - ``Cusercustomitem5``
    - | 項目 7 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkname1``
    - | リンク名称 1 を指定
      | 数値の範囲を検索する場合は ``Vlinkname1`` に最小値を指定し ``Vlinkname1_2`` に最大値を指定
  * - ``Clinkname1``
    - | リンク名称 1 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkname2``
    - | リンク名称 2 を指定
      | 数値の範囲を検索する場合は ``Vlinkname2`` に最小値を指定し ``Vlinkname2_2`` に最大値を指定
  * - ``Clinkname2``
    - | リンク名称 2 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkname3``
    - | リンク名称 3 を指定
      | 数値の範囲を検索する場合は ``Vlinkname3`` に最小値を指定し ``Vlinkname3_2`` に最大値を指定
  * - ``Clinkname3``
    - | リンク名称 3 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkname4``
    - | リンク名称 4 を指定
      | 数値の範囲を検索する場合は ``Vlinkname4`` に最小値を指定し ``Vlinkname4_2`` に最大値を指定
  * - ``Clinkname4``
    - | リンク名称 4 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkname5``
    - | リンク名称 5 を指定
      | 数値の範囲を検索する場合は ``Vlinkname5`` に最小値を指定し ``Vlinkname5_2`` に最大値を指定
  * - ``Clinkname5``
    - | リンク名称 5 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkpath1``
    - | リンクパス 1 を指定
      | 数値の範囲を検索する場合は ``Vlinkpath1`` に最小値を指定し ``Vlinkpath1_2`` に最大値を指定
  * - ``Clinkpath1``
    - | リンクパス 1 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkpath2``
    - | リンクパス 2 を指定
      | 数値の範囲を検索する場合は ``Vlinkpath2`` に最小値を指定し ``Vlinkpath2_2`` に最大値を指定
  * - ``Clinkpath2``
    - | リンクパス 2 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkpath3``
    - | リンクパス 3 を指定
      | 数値の範囲を検索する場合は ``Vlinkpath3`` に最小値を指定し ``Vlinkpath3_2`` に最大値を指定
  * - ``Clinkpath3``
    - | リンクパス 3 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkpath4``
    - | リンクパス 4 を指定
      | 数値の範囲を検索する場合は ``Vlinkpath4`` に最小値を指定し ``Vlinkpath4_2`` に最大値を指定
  * - ``Clinkpath4``
    - | リンクパス 4 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vlinkpath5``
    - | リンクパス 5 を指定
      | 数値の範囲を検索する場合は ``Vlinkpath5`` に最小値を指定し ``Vlinkpath5_2`` に最大値を指定
  * - ``Clinkpath5``
    - | リンクパス 5 の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vmemo``
    - | コメント を指定
      | 数値の範囲を検索する場合は ``Vmemo`` に最小値を指定し ``Vmemo_2`` に最大値を指定
  * - ``Cmemo``
    - | コメント の検索方法を指定
      | :ref:`s-cond` 参照

  * - ``Vgroup_only``
    - | グループ専属書類 の検索条件を指定
      | 省略可能
      | ``0`` の場合は チェック無 の書類に限定
      | ``1`` の場合は チェック有 の書類に限定

  * - ``Vf_individual``
    - | 個人書類 の検索条件を指定
      | 省略可能
      | ``0`` の場合は チェック無 の書類に限定
      | ``1`` の場合は チェック有 の書類に限定

  * - ``Vf_secret``
    - | 丸秘書類 の検索条件を指定
      | 省略可能
      | ``0`` の場合は チェック無 の書類に限定
      | ``1`` の場合は チェック有 の書類に限定

  * - ``Vf_handin``
    - | 提出済み書類 の検索条件を指定
      | 省略可能
      | ``0`` の場合は チェック無 の書類に限定
      | ``1`` の場合は チェック有 の書類に限定


  * - ``Vexeword``
    - | 拡張子を検索
      | ``*.pdf`` で PDF を検索します。
      | ``*.doc/*.docx`` のように指定して、複数の拡張子を検索します。
      | ``フォルダ`` を指定して、フォルダ書類を検索します。



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
