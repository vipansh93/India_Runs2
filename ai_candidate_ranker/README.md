# Intelligent Candidate Discovery & Ranking System

This repository contains the candidate ranking engine built for the Redrob hackathon. The system parses a pool of 100,000 candidates and identifies the top 100 fits for the **Senior AI Engineer - Founding Team** role based on experience, location, career alignment, technical skills, and behavioral signals, while actively filtering out adversarial trap and honeypot candidates.

## Core Features
1. **Honeypot Protection**: Rules-based filtering to detect semantic contradictions (e.g. expert skill with 0 months used, role duration > calendar limits, signup dates in the future). This filters out 7,533 profiles, keeping our top 100 100% honeypot-free (0% honeypot rate vs. the 10% DQ threshold).
2. **Consulting Filter**: Detects and penalizes candidates whose entire career history consists exclusively of IT consulting/services firms (e.g., Wipro, TCS, Cognizant, Infosys, Capgemini, Accenture), prioritizing product-company engineers.
3. **Multi-dimensional Scoring**: Weighs NLP/IR technical skills, experience alignment (ideal 5–9 YOE), location (Noida/Pune or willing to relocate in India), and career title/keyword density.
4. **Behavioral Modifiers**: Scales base scores by behavioral signals (notice periods, login activity recency, response rates, and interview completion rates) to ensure candidates are active and hireable.
5. **Ultra-fast Standard Library Execution**: Written entirely in pure Python (no external dependencies required for the ranking script), completing in **~40 seconds** on 100,000 records on a single CPU core.

## Getting Started

### Prerequisites
- Python 3.10+
- The `pyyaml` library (only for metadata/yaml parsing, if needed)

```bash
pip install -r requirements.txt
```

### Running the Ranker
To rank the candidates and produce the submission CSV:

```bash
python rank.py --candidates ../India_runs_data_and_ai_challenge/candidates.jsonl --out ../India_runs_data_and_ai_challenge/team_antigravity.csv
```

### Running the Web Dashboard

To run the interactive web application:

1. **Install web dependencies**:
   ```bash
   pip install flask flask-cors
   ```

2. **Start the Flask server**:
   ```bash
   python app.py
   ```
   This will load the 100k candidate pool in memory, pre-filter the honeypots, and start the development server on `http://127.0.0.1:5000`.

3. **Access the Dashboard**:
   Open your web browser and navigate to `http://127.0.0.1:5000`.
   - **Page 1 (Home)**: High-fidelity cinematic landing page outlining the talent discovery engine parameters.
   - **Page 2 (Discovery Workspace)**: Multi-dimensional filtering panel allowing real-time re-ranking of the 100k candidates on CPU, dynamic matched skills highlighting, strengths/cautions lists, timeline keyword highlighting, and behavioral HUD signals.

### Validating the Submission
To verify the output CSV structure and values against the hackathon rules:

```bash
python ../India_runs_data_and_ai_challenge/validate_submission.py ../India_runs_data_and_ai_challenge/team_antigravity.csv
```
This should output `Submission is valid.`
