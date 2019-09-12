ダウンロード fget
=====================

URL
---

.. code-block::

   GET /DD/fget.php?pid={pid}&dummy={dummy}&path=/{session_id}/{id}{ext}{fp}


.. list-table:: QueryString
   :widths: auto
   :header-rows: 1

   * - Key
     - value
   * - session_id
     - php のセッション ID
   * - pid
     - 版管理している書類を対象とする場合は親の書類 ID
   * - dummy
     - ブラウザキャッシュ対策用
   * - id
     - 書類 ID
   * - ext
     - 拡張子。必要な場合、付与しても構いません。その場合、動作には影響しません
   * - fp
     - フォルダー書類の場合は、ファイルへの相対パス

HTTP リクエストヘッダー
-----------------------

``HTTP_RANGE`` 次のような書式に対応：

.. code-block:: text

   0-499
   -500
   9500-

HTTP レスポンスコード
-----------------------

成功の場合は 200 系

.. code-block:: text

   HTTP/1.1 206 Partial Content
   HTTP/1.1 416 Requested range not satisfiable

HTTP レスポンスボディー
-----------------------

通常は書類ファイルそのまま出力しますが、状況により異なったファイル形式で出力しようとします。

* $_GET["tiff2pdf"] が 1 で、TIFF 書類の場合、PDF 形式に変換を試みます。
* UA がスマホまたは Mac OS X の場合、PDF 形式に変換を試みます。
* 動画の場合、変換中は HTML を出力する場合があります。
* PDF 形式で、印刷が許可されていない閲覧者が入手しようとしている時、PDF に印刷不可のセキュリティーをセットしようとします。
