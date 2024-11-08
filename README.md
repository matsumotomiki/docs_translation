# ja page initialization
```bash
export LC_ALL=C
cd ~/git/clickhouse-docs
yarn cache clean
yarn install
yarn prep-from-master
cp -r docs/en docs/ja
find docs/ja -type f -exec sed -i '' 's|slug: /en/|slug: /ja/|g' {} \;
find docs/ja -type f -exec sed -i '' "s|slug: '/en/|slug: '/ja/|g" {} \;
find docs/ja -type f -exec sed -i '' "s|slug: \"/en/|slug: \"/ja/|g" {} \;
find docs/ja -type f -exec sed -i '' 's|(/docs/en/|(/docs/ja/|g' {} \;
find docs/ja -type f -exec sed -i '' 's|@site/docs/en/|@site/docs/ja/|g' {} \;
find docs/ja -type f -exec sed -i '' 's|"/docs/en/|"/docs/ja/|g' {} \;
sed -i '' '1 s/^---$/---\nslug: \/ja/' docs/ja/intro.md
yarn start
```

# docs_translation
```bash
cd ~/git/docs_translation
source venv/bin/activate
cp -r ~/git/clickhouse-docs/docs/ja ~/git/clickhouse-docs/docs/ja_bk
python3 translate_long_text.py ~/git/clickhouse-docs/docs/ja_bk ~/git/clickhouse-docs/docs/ja
rm -f ~/git/clickhouse-docs/docs/ja_bk
```

# remove translated_ header
```bash
find . -type f -name 'translated_*' -exec bash -c 'mv "$0" "${0/translated_/}"' {} \;
```