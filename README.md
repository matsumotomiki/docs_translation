# ja page initialization
```bash
cd ~/git/clickhouse-docs
yarn cache clean
yarn install
yarn prep-from-master
cp -r docs/en docs/ja
find docs/ja -type f -exec sed -i '' 's|slug: /en/|slug: /ja/|g' {} \;
find docs/ja -type f -exec sed -i '' "s|slug: '/en/|slug: '/ja/|g" {} \;
find docs/ja -type f -exec sed -i '' "s|slug: \"/en/|slug: \"/ja/|g" {} \;
sed -i '' '1 s/^---$/---\nslug: \/ja/' docs/ja/intro.md
yarn start
```

# docs_translation
```bash
cd ~/git/docs_translation
source venv/bin/activate
mv translate.py ~/git/clickhouse-docs/docs/ja_bk
python3 translate.py ~/git/clickhouse-docs/docs/ja_bk ~/git/clickhouse-docs/docs/ja
rm -f ~/git/clickhouse-docs/docs/ja_bk
```

