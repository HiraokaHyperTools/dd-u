検索 API
===========

URL
---

.. code-block::

   POST /DD/ando.php?a=search


.. list-table:: QueryString
   :widths: auto
   :header-rows: 1

   * - Key
     - value
   * - start
     - スキップ件数。0 の場合、最初から表示
   * - q
     - WCQ 検索式を BASE64 ('base64url' encoding) 化したもの
   * - FindWay
     - "kw"=キーワード検索, 他カスタム検索
   * - KeywordSearch-FTS
     - 1 の場合「全文検索を含む」オン
   * - KeywordSearch
     - キーワード検索のキーワード
   * - userid
     - 未登録呼び出し対象の担当者 ID


.. list-table:: DB フィールドごとの QueryString
   :widths: auto
   :header-rows: 1

   * - Key
     - value
   * - Vid
     - 書類 ID を指定
   * - Cid
     - | 書類 ID の検索方法。
       | :ref:`wcq-opecodes` 参照。


Vid と Cid のほかに、このような組み合わせもあります。DateInput2 など、s,between が可能なフィールドは 3 列あります。

.. code-block::

   Vid    Cid
   Vgroup_id    Cgroup_id
   Vcreateuserid    Ccreateuserid
   Vadminuserid    Cadminuserid
   DateInput    DateInputCondition    DateInput2
   DateUpdate    DateUpdateCondition    DateUpdate2
   DateDeadline    DateDeadlineCondition    DateDeadline2
   DateUser    DateUserCondition    DateUser2
   Vcampanyname    Ccampanyname
   Vtitle    Ctitle    Vtitle_2
   Vproject    Cproject    Vproject_2
   Vusercustomitem1    Cusercustomitem1    Vusercustomitem1_2
   Vusercustomitem2    Cusercustomitem2    Vusercustomitem2_2
   Vusercustomitem3    Cusercustomitem3    Vusercustomitem3_2
   Vusercustomitem4    Cusercustomitem4    Vusercustomitem4_2
   Vusercustomitem5    Cusercustomitem5    Vusercustomitem5_2
   Vmemo    Cmemo

Vexeword を指定した場合は拡張子を検索します。
"*.doc/*.docx" のように複数の拡張子を検索することも可能。"フォルダ" の場合はフォルダを検索します。


次の項目は bool です。"1" か "0" で検索。検索したくない場合は空文字列。

.. code-block::

   Vgroup_only
   Vf_individual
   Vf_secret
   Vf_handin

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
