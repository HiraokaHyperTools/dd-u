.. _js-json:

js.php の返す JSON
=====================

.. code-block:

   Content-Type: text/javascript+json; charset=utf-8

.. list-table::
   :widths: auto
   :header-rows: 1

   * - ルーチン
     - | X-JSON:
       | ヘッダー付与の条件
     - HTTP レスポンス ボディー
     - HTTP_X_SET_BRACKETS = 0
     - HTTP_X_SET_BRACKETS = 1
   * - setJson
     - 5,000 バイト未満の場合
     - JSON
     - JSON
     - JSON
   * - setJson2
     - 5,000 バイト未満の場合
     - (JSON)
     - JSON
     - (JSON)
   * - setJson2B
     - 付与しません
     - (JSON)
     - JSON
     - (JSON)
   * - setJson2R
     - 付与しません
     - JSON
     - JSON
     - (JSON)
