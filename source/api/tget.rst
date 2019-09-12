サムネイル tget
==================

概要
----

指定した書類のサムネイル画像を出力します。

TIF/PDF/JPEG などの画像データを対象としています。

Word/Excel など文書の場合は、書類を示すアイコン画像を出力します。

URL
---

.. code-block::

   GET /DD/tget.php?{session_id}&id={id}


.. list-table:: QueryString
   :widths: auto
   :header-rows: 1

   * - Key
     - value
   * - session_id
     - php のセッション ID
   * - id
     - 書類 ID
   * - w
     - 幅
   * - path
     - フォルダ書類の中身のサムネイルを得る場合、その相対パス
   * - g
     - 1 の場合 96px
   * - p
     - ページ番号。最初は 1
   * - gpc
     - 1 の場合、HTTP レスポンスヘッダー X-PGCnt にページ数を設定。サムネイルは出力しません。
   * - pinfo
     - 1 の場合、JSON で ``PageCount:$cnt`` を返します。サムネイルは出力しません。
   * - rot
     - 回転。使用できません。
   * - t
     - 不要、ブラウザキャッシュ対策用
   * - idver
     - 特殊。

HTTP リクエストヘッダー
-----------------------

特になし

HTTP レスポンスヘッダー
-----------------------

特になし

HTTP レスポンスボディー
-----------------------

画像の場合は ``image/jpeg``
