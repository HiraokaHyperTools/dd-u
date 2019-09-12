ログイン
===========

URL
---

.. code-block::

   POST /DD/ando.php?a=login

HTTP リクエストヘッダー
---------------------------

.. code-block::

   Content-Type: application/x-www-form-urlencoded

HTTP リクエストボディー
---------------------------

.. list-table:: POST body
   :widths: auto
   :header-rows: 1

   * - Key
     - 値
   * - ID
     - ログイン ID
   * - Password
     - パスワード
   * - syskey
     - シングルサインイン用のキー
   * - REMEMBERME
     - パスワードを 1 日間記憶します。
   * - APIOnly
     - 1 の場合、ライセンス数を消費しなくなります。その代償として、Web 画面が使用できなくなります。
   * - APIApp
     - アプリケーション名。任意です。

HTTP レスポンスヘッダー
---------------------------

.. code-block::

   Location: ...

HTTP レスポンスボディー
---------------------------

特になし。

ログイン後、検索画面に移動した場合は、つぎのような JSON が挿入されます。

.. code-block:: html

   <!-- <mydd:ando>{"f":"search"}</mydd:ando> -->



