# Token-zasyon

A small project to train a Byte Pair Encoding (BPE) tokenizer on Turkish financial text and save the trained tokenizer as a JSON file.

## Contents
- `train.py` — training script that builds a BPE tokenizer using the `tokenizers` library.
- `finans_verisi.txt.txt` — example training data (this repository ignores `.txt` files by default).
- `finans_bpe_tokenizer.json` — the output file produced by `train.py` after a successful run.

## Requirements
- Python 3.8+ (tested with Python 3.15)
- `tokenizers` Python package

## Quick setup
1. Create and activate a virtual environment in the project folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell
# or: .venv\Scripts\activate  # cmd.exe
```

2. Install the required package:

```powershell
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install tokenizers
```

## Run training
Execute the training script with the venv Python interpreter:

```powershell
.venv\Scripts\python.exe c:/Users/Mdn/Desktop/tokenizasyon/train.py
```

On success the script will save `finans_bpe_tokenizer.json` in the project folder.

## Notes
- `train.py` contains a small helper to detect `finans_verisi.txt` vs `finans_verisi.txt.txt` so the script works if the data file has an extra `.txt` suffix.
- The repository `.gitignore` is configured to ignore `*.txt` files so training data is not pushed to the remote.

## License
MIT — feel free to modify and reuse.
