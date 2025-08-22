# SmartXplore — Research Paper Summarizer (Web Demo)

Minimal Flask web app to summarize PDFs or pasted text using Sumy's LSA summarizer.

## Quickstart

1) Create & activate a virtual environment (recommended). In VS Code:
- Press **Ctrl+Shift+P** → *Python: Create Environment* → *Venv* → pick interpreter
- Or run manually:

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

2) Install deps:

```bash
pip install -r requirements.txt
```

3) Run the app:

```bash
python app.py
# open http://127.0.0.1:5000
```

## Notes
- Summary length slider lets you choose 1–15 sentences.
- For scanned PDFs you need OCR (future: `pytesseract` + `ocrmypdf`).

## Production
Use a WSGI server like waitress:

```bash
waitress-serve --host=0.0.0.0 --port=5000 app:app
```