フォルダ書類へ変換
=====================

URL
---

.. code-block::

   POST /DD/js.php?a=converttofolder

HTTP リクエストヘッダー
-----------------------

HTTP リクエストボディー
-----------------------

``application/json``

.. code-block:: 

   {
      "idl": ['00000000', '00000001', ...]
   }

HTTP レスポンスコード
-----------------------

成功の場合は 200 系

HTTP レスポンスボディー
-----------------------

``application/json``

.. code-block:: 

   {
      "allok": true,
      "message": ""
   }
