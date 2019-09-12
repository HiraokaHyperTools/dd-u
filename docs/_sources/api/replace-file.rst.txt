ファイル差し替え
=================

URL
---

.. code-block::

   POST /DD/js.php?a=rf2&id={id}&alwaysrename={alwaysrename}

Query string
------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Key
     - value
   * - id
     - 書類 ID
   * - alwaysrename
     - 1 ならば強制差し替え (r3489 以降)

HTTP リクエストヘッダー
---------------------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Key
     - value
   * - X-FILE-NAME
     - ファイル名。拡張子が重要です
   * -  X-FILE-SIZE
     - ファイルのバイト数

(2016/10/3 修正) アンダーバーではなく、ハイフンで送ってください!

HTTP リクエストボディー
----------------------------

ファイルの中身

HTTP レスポンスコード
---------------------------

成功した場合は 200

.. code-block:: text

   HTTP/1.1 500 Upload error
   HTTP/1.1 500 Replace failed
   HTTP/1.1 500 NotImpl
   HTTP/1.1 500 AccessDenied
   HTTP/1.1 500 ReplaceShareViolation
