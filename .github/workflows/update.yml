name: Auto-update Fire Docs

on:
  schedule:
    - cron: '0 3 * * *'
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests beautifulsoup4 lxml

      - name: Run parser
        run: python parser.py

      - name: Commit and push if changed
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add docs.json
          git diff --quiet && git diff --staged --quiet || (git commit -m "Автообновление: пожарная документация $(date +%Y-%m-%d)" && git push)
