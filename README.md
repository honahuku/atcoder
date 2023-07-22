# atcoder

## CLIツール
[Tatamo/atcoder-cli](https://github.com/Tatamo/atcoder-cli)と[online-judge-tools/oj](https://github.com/online-judge-tools/oj/tree/master)を利用しています。

```bash
npm install -g atcoder-cli
pip3 install --user online-judge-tools

acc login
acc session
oj login https://beta.atcoder.jp/
acc new abc300

acc add

# 問題を選択
cd abc300/a
# ディレクトリにコンテスト情報を登録
oj d https://atcoder.jp/contests/abc300/tasks/abc300_b

# テスト
# 個別のケース
python3 main.py < test/sample-1.in 

# すべてのケース
oj t -c "python3 ./main.py" -d test/

# 提出
acc s
# oj s main.py
```
参考:
[atcoder-cli チュートリアル | わたしろぐ](http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/)
[コマンドラインツールatcoder-cliを公開しました | わたしろぐ](http://tatamo.81.la/blog/2018/12/07/atcoder-cli/)
[oj/docs/getting-started.ja.md at master · online-judge-tools/oj](https://github.com/online-judge-tools/oj/blob/master/docs/getting-started.ja.md)

### 設定
お好みで以下を設定
```bash
# acc newですべての問題をダウンロードする
acc config default-task-choice all
```
