# 🚀 AuraRecruit — AI Candidate Ranker
### Built by Team NeuralHire | India Runs Data & AI Challenge

An intelligent candidate discovery and ranking engine that processes a pool of **100,000 candidates** and surfaces the top 100 fits for a given role using multi-dimensional scoring, honeypot filtering, and behavioral signals.

---

## ✨ Core Features

| Feature | Description |
|---|---|
| 🛡️ **Honeypot Filtering** | Rules-based detection of adversarial/fake profiles (expert skill with 0 months used, impossible date ranges, future signup dates). Filters **7,533 profiles** with 0% honeypot rate in top 100 |
| 🏭 **Consulting Filter** | Penalizes candidates whose entire career is at IT services firms (Wipro, TCS, Infosys, Cognizant, Accenture, etc.), prioritizing product-company engineers |
| 📊 **Multi-dimensional Scoring** | Weighs NLP/IR skills, experience (ideal 5–9 YOE), location (Noida/Pune preferred), title/keyword density across career history |
| 🧠 **Behavioral Multipliers** | Scales scores using notice period, login recency, recruiter response rate, interview completion rate, and offer acceptance rate |
| ⚡ **4 Job Roles Supported** | Senior AI Engineer, Applied ML Engineer, NLP & LLM Specialist, Search & Retrieval Engineer |
| 🌐 **Web Dashboard** | Interactive Flask UI with real-time re-ranking sliders, candidate drill-down, and Excel export |

---

## 🖥️ Quickstart — Run from Source (Recommended after cloning)

> **Requirements:** Python 3.10+, internet connection (first run only), `candidates.jsonl` dataset

### Option A — Double-click (Windows)

1. Clone this repo
2. Get `candidates.jsonl` from the challenge dataset
3. **Double-click `run.bat`** inside the `ai_candidate_ranker/` folder

The script will automatically:
- ✅ Check your Python version
- ✅ Install all dependencies (`flask`, `flask-cors`, `openpyxl`, etc.)
- ✅ Find `candidates.jsonl` automatically, or ask you for its path
- ✅ Start the server and open your browser at `http://127.0.0.1:5000`

---

### Option B — Manual (Mac/Linux/Windows terminal)

```bash
# 1. Clone the repo
git clone https://github.com/vipansh93/India_Runs2.git
cd India_Runs2/ai_candidate_ranker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the web dashboard
python app.py --candidates /path/to/candidates.jsonl
```

Then open your browser at **http://127.0.0.1:5000**

---

## 📁 Project Structure

```
ai_candidate_ranker/
├── app.py                    # Flask backend + scoring engine (web dashboard)
├── rank.py                   # Standalone CLI ranker (produces submission CSV)
├── index.html                # Full frontend UI (served by Flask)
├── requirements.txt          # Python dependencies
├── run.bat                   # 🟢 Windows one-click launcher (run this!)
├── aura_recruit.spec         # PyInstaller spec (for building the .exe)
├── submission_metadata.yaml  # Hackathon submission metadata
└── submission.csv            # Generated submission file
```

---

## 🏃 Running the CLI Ranker (produces submission CSV)

```bash
python rank.py \
  --candidates /path/to/candidates.jsonl \
  --out submission.csv
```

---

## ✅ Validating the Submission

```bash
python validate_submission.py submission.csv
# Expected output: Submission is valid.
```

---

## 🌐 Web Dashboard Features

Once the server is running at `http://127.0.0.1:5000`:

- **Role Selector** — Switch between 4 job roles, re-ranks instantly
- **Candidate List** — Top 100 ranked candidates with scores
- **Candidate Detail** — Click any candidate for full AI analysis, skill breakdown, career timeline
- **Scoring Sliders** — Adjust weights for experience, skills, location, behavioral signals in real-time
- **Excel Export** — Download a styled `.xlsx` report of the current ranking

---

## ⚠️ About `candidates.jsonl`

The dataset file (`candidates.jsonl`, ~465 MB) is **not included** in this repo due to GitHub's 100 MB file size limit.

You need to obtain it separately from the challenge organizers.

Once you have it, you can either:
- Place it in the `ai_candidate_ranker/` folder (run.bat will find it automatically)
- Or provide the path when prompted by `run.bat`
- Or pass it manually: `python app.py --candidates "C:\path\to\candidates.jsonl"`

---

## 🛠️ Building the EXE (optional)

If you want to package the app as a standalone Windows `.exe`:

```bash
pip install pyinstaller
pyinstaller aura_recruit.spec
# Output: dist/AuraRecruit.exe
```

---

## 📦 Dependencies

```
flask>=3.0.0
flask-cors>=4.0.0
openpyxl>=3.1.0
pyyaml>=6.0
```
