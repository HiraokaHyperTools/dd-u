WCQ 検索式
=============

WCQ (Word Complex Query)

逆ポーランド法で検索式を組み立てます。8 ビットのバイナリセーフ、バイトオーダーはリトルエンディアンです。

引数は左からプッシュします。中置記法で ``1 < 2`` の場合、後置記法では ``1 2 <``

1 バイト目の構造
-----------------

.. code-block::

   0x00 - 0x7F = 引数(文字列、バイト数を示します)
   0x80 - 0xBF = 引数(DB フィールド)
   0xC0 - 0xFF = オペコード

文字列
-----------------

ボム無しの UTF-8 です。``(バイト数) + (文字列、NUL 終端なし)``

.. csv-table:: DB フィールド（特記しないものは文字列）
   :widths: auto
   :header-rows: 1

   DB 列番,DB 列名,名称,型
   0,id,書類 ID,
   2,filepath,書類ファイルの相対パス,
   5,title,項目 1,
   6,project,項目 2,
   8,campanyname,会社名,
   9,memo,コメント欄,
   10,f_secret,マル秘 (bool),
   13,createuserid,登録担当者 ID,
   14,adminuserid,承認担当者 ID,
   15,createdate,登録日 (date),
   16,modifydate,更新日 (date),
   17,usercustomitem1,項目 3,
   18,usercustomitem2,項目 4,
   19,usercustomitem3,項目 5,
   20,usercustomitem4,項目 6 ,
   21,usercustomitem5,項目 7,
   23,linkname1,リンク名称 1,
   24,linkname2,リンク名称 2,
   25,linkname3,リンク名称 3,
   26,linkname4,リンク名称 4,
   27,linkname5,リンク名称 5  ,
   29,linkpath1,リンクパス 1,
   30,linkpath2,リンクパス 2,
   31,linkpath3,リンクパス 3,
   32,linkpath4,リンクパス 4,
   33,linkpath5,リンクパス 5,
   35,modifytime,更新時間,time without time zone
   43,limitdate,提出期限,date
   44,f_handin,提出済み,boolean
   45,f_individual,個人書類,boolean
   47,userdate,日付,date
   50,group_id,グループ ID (int),integer
   51,group_only,グループ専属書類 (bool),boolean
   52,exeword,拡張子,
   53,lock,読み取り専用,boolean

.. _wcq-opecodes:

オペコード
-------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - コード
     - 名前
     - 意味
     - 分類
     - numArgs
   * - 0xC0
     - And
     - 引数 1 and 2
     - BinaryOpBool
     - 2
   * - 0xC1
     - Or
     - 引数 1 or 2
     - BinaryOpBool
     - 2
   * - 0xC2
     - s,contain
     - 引数 1 が引数 2 ～を含む検索
     - BinaryOpStr
     - 2
   * - 0xC3
     - s,startswith
     - ～で始まる
     - BinaryOpStr
     - 2
   * - 0xC4
     - s,endswith
     - ～で終わる
     - BinaryOpStr
     - 2
   * - 0xC5
     - s,is
     - 完全一致
     - BinaryOpStr
     - 2
   * - 0xC6
     - d,is
     - 等しい(日付)
     - BinaryOpDate
     - 2
   * - 0xC7
     - d,between
     - ～と～の間(日付) 1 between 2 and 3
     - TernaryOpDate
     - 3
   * - 0xC8
     - d,less
     - より前 1<2
     - BinaryOpDate
     - 2
   * - 0xC9
     - d,greater
     - より後 1>2
     - BinaryOpDate
     - 2
   * - 0xCA
     - d,isnot
     - 等しくない 1!=2
     - BinaryOpDate
     - 2
   * - 0xCB
     - TRUE
     -
     - Literal
     -
   * - 0xCC
     - FALSE
     -
     - Literal
     -
   * - 0xCD
     - s,kw
     - 引数 1 でキーワード検索
     - UnaryOpStr
     - 1
   * - 0xCE
     - s,geq
     - ～以上(文字列) 1>=2
     - BinaryOpStr
     - 2
   * - 0xCF
     - s,leq
     - ～以下(文字列) 1<=2
     - BinaryOpStr
     - 2
   * - 0xD0
     - s,isnot
     - ～以外(文字列) 1!=2
     - BinaryOpStr
     - 2
   * - 0xD1
     - s,isempty
     - 引数 1 が空文字列
     - UnaryOpStr
     - 1
   * - 0xD2
     - s,notcontained
     - 引数 1 が 2 を含まない
     - BinaryOpStr
     - 2
   * - 0xD3
     - d,geq
     - ～以降(日付) 1>=2
     - BinaryOpDate
     - 2
   * - 0xD4
     - d,leq
     - ～以前(日付) 1<=2
     - BinaryOpDate
     - 2
   * - 0xD5
     - i,is
     - 等しい(int) 1=2
     - BinaryOpInt
     - 2
   * - 0xD6
     - i,isnot
     - 等しくない(int) 1!=2
     - BinaryOpInt
     - 2
   * - 0xD7
     - b,is
     - 引数 1 が true
     - UnaryOpBool
     - 1
   * - 0xD8
     - b,isnot
     - 引数 1 がfalse
     - UnaryOpBool
     - 1
   * - 0xD9
     - s,fts1
     - 引数 1 で全文検索
     - UnaryOpStr
     - 1
   * - 0xDA
     - f,between
     - strtod 相当 1 between 2 and 3
     - TernaryOpFloat
     - 3
   * - 0xDB
     -
     - | LongStr です。(バイト数 DWORD) + (文字列、NUL 終端なし)
       | r3296 以降で対応。
     - LongStr
     -
   * - 0xDC
     - s,imagesearch
     - | JSON 文字列で 引数 1 を指定し、画像検索します。
       | {
       |  "a":["aHashAsString","more",...],
       |  "dv":["dvHashAsString","more",...]
       | }
     - UnaryOpStr
     - 1
   * - 0xDD
     - s,equals
     - | 一致。 
       | s,startswith と s,endswith を組み合わせたもの
       | r3566 以降で対応。
     - BinaryOpStr
     - 2
