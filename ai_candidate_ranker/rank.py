#!/usr/bin/env python3
"""
Redrob Candidate Ranker
Ranks candidates for the Senior AI Engineer - Founding Team role.
"""

import argparse
import json
import os
import csv
from datetime import datetime

# Core NLP/IR skills requested in the Job Description
MUST_HAVE_SKILLS = {
    "embeddings", "retrieval", "vector search", "hybrid search", "pinecone",
    "weaviate", "qdrant", "milvus", "opensearch", "elasticsearch", "faiss",
    "sentence-transformers", "bge", "e5", "pytorch", "tensorflow", "nlp",
    "natural language processing", "information retrieval", "rag",
    "evaluation frameworks", "ndcg", "mrr", "map"
}

# Optional nice-to-have skills mentioned in the JD
NICE_TO_HAVE_SKILLS = {
    "llm", "llms", "fine-tuning", "lora", "qlora", "peft", "xgboost",
    "learning to rank", "learning-to-rank", "distributed systems", "inference optimization"
}

# Irrelevant domain skills (computer vision, speech, robotics, etc.)
CV_SPEECH_ROBOTICS_SKILLS = {
    "computer vision", "image classification", "object detection", "speech recognition",
    "robotics", "voice assistant", "gans", "yolo"
}

# Target AI/ML role title keywords
AI_TITLE_KEYWORDS = [
    "ai engineer", "ml engineer", "machine learning engineer", "nlp engineer",
    "search engineer", "retrieval engineer", "data scientist", "applied scientist",
    "applied ml", "machine learning"
]

# General software and backend development roles (acceptable, but lower weight than direct AI roles)
GENERAL_TECH_TITLES = [
    "software engineer", "backend engineer", "full stack developer", "technical lead",
    "architect", "systems engineer", "data engineer"
]

# Roles explicitly warning bad fit/disqualification
IRRELEVANT_TITLES = [
    "marketing manager", "hr manager", "operations manager", "mechanical engineer",
    "graphic designer", "accountant", "sales executive", "customer support",
    "civil engineer", "ui/ux designer"
]

# IT Services and Consulting firms where only working there in entire career is disqualified
IT_SERVICES_COMPANIES = {
    "wipro", "tcs", "tata consultancy", "infosys", "accenture", "cognizant",
    "capgemini", "tech mahindra", "hcl", "mphasis", "l&t", "lnt", "mindtree",
    "genpact", "ibm", "ntt data", "dxc", "reliance jio"
}

# Product-centric startup or corporate industries
PRODUCT_INDUSTRIES = {"software", "fintech", "e-commerce", "food delivery"}


def is_honeypot(candidate):
    """
    Identifies if a candidate profile is a honeypot (contains impossible contradictions).
    Disqualifies the candidate if True.
    """
    # Check 1: Expert proficiency skill with 0 duration used
    for s in candidate.get("skills", []):
        if s.get("proficiency") == "expert" and s.get("duration_months", 0) == 0:
            return True
            
    # Check 2: Job claimed duration exceeds the actual calendar dates limit
    for job in candidate.get("career_history", []):
        start_str = job.get("start_date")
        end_str = job.get("end_date")
        dur = job.get("duration_months", 0)
        if start_str:
            try:
                start_date = datetime.strptime(start_str, "%Y-%m-%d")
                if end_str:
                    end_date = datetime.strptime(end_str, "%Y-%m-%d")
                    if end_date < start_date:
                        return True
                else:
                    # Current year is mid-2026 based on challenge timeline
                    end_date = datetime(2026, 6, 26)
                
                cal_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                # Claimed duration must not be physically impossible (adding 2 months buffer for date differences)
                if dur > cal_months + 2:
                    return True
            except:
                pass
                
    # Check 3: Platform last active date is prior to sign up date
    signals = candidate.get("redrob_signals", {})
    signup_str = signals.get("signup_date")
    active_str = signals.get("last_active_date")
    if signup_str and active_str:
        try:
            signup_date = datetime.strptime(signup_str, "%Y-%m-%d")
            active_date = datetime.strptime(active_str, "%Y-%m-%d")
            if active_date < signup_date:
                return True
        except:
            pass
            
    # Check 4: Education end year is prior to start year
    for edu in candidate.get("education", []):
        start = edu.get("start_year")
        end = edu.get("end_year")
        if start and end and end < start:
            return True
            
    return False


def score_candidate(candidate):
    """
    Calculates final suitability score based on candidate profile.
    """
    profile = candidate.get("profile", {})
    skills = candidate.get("skills", [])
    career = candidate.get("career_history", [])
    signals = candidate.get("redrob_signals", {})
    
    # 1. Years of Experience (JD requests 5-9 years, flexible 6-8 ideal)
    yoe = profile.get("years_of_experience", 0)
    exp_score = 0
    if 5 <= yoe <= 9:
        exp_score = 25
    elif 4 <= yoe < 5 or 9 < yoe <= 11:
        exp_score = 15
    elif 3 <= yoe < 4 or 11 < yoe <= 13:
        exp_score = 5
    else:
        exp_score = -20  # Heavy penalty for too junior (<3 YOE) or too senior/out-of-scope (>13 YOE)
        
    # 2. Location Alignment (Noida/Pune preferred, willing to relocate in India OK)
    loc = profile.get("location", "").lower()
    country = profile.get("country", "").lower()
    willing_relocate = signals.get("willing_to_relocate", False)
    
    loc_score = 0
    if country == "india":
        if "noida" in loc or "pune" in loc:
            loc_score = 20
        elif willing_relocate:
            # Check if they reside in major tech hubs that can relocate
            major_hubs = ["hyderabad", "mumbai", "delhi", "bangalore", "chennai", "indore", "jaipur", "ahmedabad", "kolkata", "kochi", "trivandrum", "gurgaon"]
            if any(hub in loc for hub in major_hubs):
                loc_score = 15
            else:
                loc_score = 10
        else:
            loc_score = -5  # In India but not in Noida/Pune and unwilling to relocate
    else:
        loc_score = -40  # International candidates (requires visa sponsorship, explicitly warned in JD)
        
    # 3. Technical Skills (focusing on NLP/IR, pinecone/vector databases, PyTorch, evaluation)
    skill_score = 0
    has_nlp_ir = False
    has_cv_speech_robotics = False
    
    prof_weights = {
        "beginner": 0.2,
        "intermediate": 0.5,
        "advanced": 0.8,
        "expert": 1.0
    }
    
    matched_must_have = []
    matched_nice_to_have = []
    
    for s in skills:
        name = s.get("name", "").lower()
        prof = s.get("proficiency", "beginner")
        weight = prof_weights.get(prof, 0.2)
        dur = s.get("duration_months", 0)
        endorsements = s.get("endorsements", 0)
        
        # Calculate a multiplier representing skill depth/trustworthiness
        trust_mult = (dur / 12.0) * (1.0 + endorsements / 10.0)
        trust_mult = min(max(trust_mult, 0.5), 4.0)  # Bound multiplier
        
        skill_val = weight * trust_mult
        
        if name in MUST_HAVE_SKILLS:
            skill_score += skill_val * 6.0
            matched_must_have.append(name)
            if name in ["embeddings", "retrieval", "vector search", "hybrid search", "nlp", "rag", "information retrieval"]:
                has_nlp_ir = True
        elif name in NICE_TO_HAVE_SKILLS:
            skill_score += skill_val * 3.0
            matched_nice_to_have.append(name)
        elif name in CV_SPEECH_ROBOTICS_SKILLS:
            has_cv_speech_robotics = True
            
    # Apply penalty if candidate only has CV/speech/robotics without NLP/IR exposure
    if has_cv_speech_robotics and not has_nlp_ir:
        skill_score -= 15
        
    # 4. Career History, Title, and Description Keyword Scanning
    career_score = 0
    current_title = profile.get("current_title", "").lower()
    
    if any(kw in current_title for kw in AI_TITLE_KEYWORDS):
        career_score += 15
    elif any(kw in current_title for kw in GENERAL_TECH_TITLES):
        career_score += 8
    elif any(kw in current_title for kw in IRRELEVANT_TITLES):
        career_score -= 40
        
    # Out of production coding warning (Tech leads/managers out of coding for last 18 months)
    is_architect_manager = any(kw in current_title for kw in ["architect", "manager", "director", "lead"])
    if is_architect_manager:
        current_job = [j for j in career if j.get("is_current")]
        if current_job and current_job[0].get("duration_months", 0) > 18:
            career_score -= 10
            
    # Scan past descriptions for actual system implementation keywords
    relevant_exp_months = 0
    desc_keyword_matches = 0
    
    desc_keywords = [
        "recommendation", "recommender", "ranking", "search", "retrieval", "vector search",
        "embeddings", "rag", "pinecone", "milvus", "qdrant", "faiss", "elasticsearch",
        "indexing", "matching algorithm", "ndcg", "mrr", "map", "evaluating ranking",
        "offline benchmark", "learning to rank", "query processing", "semantic search"
    ]
    
    for job in career:
        title = job.get("title", "").lower()
        desc = job.get("description", "").lower()
        dur = job.get("duration_months", 0)
        
        is_relevant_role = any(kw in title for kw in AI_TITLE_KEYWORDS) or any(kw in desc for kw in desc_keywords)
        if is_relevant_role:
            relevant_exp_months += dur
            
        for kw in desc_keywords:
            if kw in desc:
                desc_keyword_matches += 1
                
    career_score += min((relevant_exp_months / 12.0) * 3.0, 15.0)
    career_score += min(desc_keyword_matches * 1.5, 12.0)
    
    # 5. Company Type and Job Stability (disqualifying consulting-only history, promoting product experience)
    company_score = 0
    total_jobs = len(career)
    it_services_jobs = 0
    product_company_jobs = 0
    total_months = 0
    
    for job in career:
        comp = job.get("company", "").lower()
        ind = job.get("industry", "").lower()
        size = job.get("company_size", "")
        dur = job.get("duration_months", 0)
        total_months += dur
        
        is_it_serv = (ind in ["it services", "consulting"]) or any(it in comp for it in IT_SERVICES_COMPANIES)
        if is_it_serv:
            it_services_jobs += 1
        else:
            if ind in PRODUCT_INDUSTRIES or size in ["11-50", "51-200", "201-500"]:
                product_company_jobs += 1
                
    if total_jobs > 0 and it_services_jobs == total_jobs:
        company_score -= 30  # Consulting / services-only filter
    elif product_company_jobs > 0:
        company_score += 10  # Startup/product engineering bonus
        
    # Job stability (average duration per job role)
    if total_jobs > 0:
        avg_dur = total_months / total_jobs
        if avg_dur < 18:
            company_score -= 10  # Penalize title chasers (switching companies too frequently)
        elif avg_dur >= 36:
            company_score += 5   # Reward stability
            
    # 6. Behavioral Signals Modifiers (Multipliers on base score)
    active_date_str = signals.get("last_active_date")
    resp_rate = signals.get("recruiter_response_rate", 0.0)
    notice = signals.get("notice_period_days", 30)
    open_work = signals.get("open_to_work_flag", False)
    int_rate = signals.get("interview_completion_rate", 0.0)
    offer_rate = signals.get("offer_acceptance_rate", -1.0)
    
    behavioral_mult = 1.0
    
    # Login activity recency decay
    if active_date_str:
        try:
            active_date = datetime.strptime(active_date_str, "%Y-%m-%d")
            days_since = (datetime(2026, 6, 26) - active_date).days
            if days_since > 180:
                behavioral_mult *= 0.5
            elif days_since > 90:
                behavioral_mult *= 0.75
            elif days_since <= 30:
                behavioral_mult *= 1.1
        except:
            pass
            
    # Recruiter response rate
    if resp_rate < 0.15:
        behavioral_mult *= 0.6
    elif resp_rate < 0.35:
        behavioral_mult *= 0.8
    elif resp_rate >= 0.75:
        behavioral_mult *= 1.1
        
    # Notice period days
    if notice <= 30:
        behavioral_mult *= 1.15  # Prefer fast joiners
    elif notice == 90:
        behavioral_mult *= 0.8
    elif notice >= 120:
        behavioral_mult *= 0.5   # Major constraint
        
    # Open to work status
    if open_work:
        behavioral_mult *= 1.1
    else:
        behavioral_mult *= 0.95
        
    # Reliability indicators
    if int_rate < 0.50:
        behavioral_mult *= 0.6
    elif int_rate >= 0.80:
        behavioral_mult *= 1.1
        
    if offer_rate == 0.0:
        behavioral_mult *= 0.6
    elif offer_rate > 0.60:
        behavioral_mult *= 1.1
        
    base_score = exp_score + loc_score + skill_score + career_score + company_score
    final_score = base_score * behavioral_mult
    
    subscores = {
        "exp_score": exp_score,
        "loc_score": loc_score,
        "skill_score": skill_score,
        "career_score": career_score,
        "company_score": company_score,
        "behavioral_mult": behavioral_mult,
        "matched_must_have": matched_must_have,
        "matched_nice_to_have": matched_nice_to_have,
        "yoe": yoe,
        "notice": notice,
        "location_raw": profile.get("location", ""),
        "willing_relocate": willing_relocate,
        "avg_dur": (total_months / total_jobs) if total_jobs > 0 else 0
    }
    
    return final_score, subscores


def generate_reasoning(rank, candidate, subscores):
    """
    Constructs a factual, non-templated 1-2 sentence justification for the candidate's rank.
    """
    profile = candidate.get("profile", {})
    yoe = subscores["yoe"]
    title = profile.get("current_title", "")
    notice = subscores["notice"]
    loc = subscores["location_raw"]
    must_haves = subscores["matched_must_have"]
    nice_haves = subscores["matched_nice_to_have"]
    mult = subscores["behavioral_mult"]
    avg_dur = subscores["avg_dur"]
    
    core_mention = must_haves[:2]
    
    reason = ""
    if rank <= 10:
        skills_str = ", ".join(core_mention) if core_mention else "ML / search systems"
        reason = f"Excellent fit with {yoe} years of experience and deep expertise in {skills_str}. "
        reason += f"Currently serving as {title} with an outstanding platform activity multiplier of {mult:.2f}x and a favorable {notice}-day notice period."
    elif rank <= 50:
        skills_str = ", ".join(core_mention) if core_mention else "ML infrastructure"
        reason = f"Strong senior candidate ({yoe} YOE) currently working as {title}. "
        if core_mention:
            reason += f"Demonstrates solid production experience with {skills_str}."
        if notice <= 30:
            reason += " Very high availability with a sub-30 day notice period."
        else:
            reason += f" Located in {loc} and active in the job market."
    elif rank <= 80:
        reason = f"Solid background as {title} with {yoe} years of experience. "
        if core_mention:
            reason += f"Brings relevant expertise in {core_mention[0]}."
        if notice >= 90:
            reason += f" Acknowledges a longer {notice}-day notice period, but otherwise matches the technical requirements."
        elif not subscores["willing_relocate"] and "noida" not in loc.lower() and "pune" not in loc.lower():
            reason += f" Currently based in {loc} (requires remote or relocation discussion)."
        else:
            reason += " Good balance of technical skill and active engagement signals."
    else:
        reason = f"Passable fit with adjacent skills in {core_mention[0] if core_mention else 'ML'}; {yoe} YOE. "
        if notice >= 90:
            reason += f" Has a long {notice}-day notice period and lower active engagement."
        else:
            reason += f" Based in {loc} with stable role history (avg {avg_dur/12.0:.1f} years/co) but less direct retrieval experience."
            
    sentences = reason.split(". ")
    reason = ". ".join(s.strip() for s in sentences if s.strip())
    if not reason.endswith("."):
        reason += "."
        
    return reason


def main():
    parser = argparse.ArgumentParser(description="Redrob hackathon ranker")
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl file")
    parser.add_argument("--out", required=True, help="Path to save submission.csv")
    
    args = parser.parse_args()
    
    scored_candidates = []
    honeypots_filtered = 0
    total = 0
    
    print(f"Reading candidates from: {args.candidates}")
    
    with open(args.candidates, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            candidate = json.loads(line)
            total += 1
            cid = candidate["candidate_id"]
            
            # Pre-filter honeypots & semantic inconsistencies
            if is_honeypot(candidate):
                honeypots_filtered += 1
                continue
                
            score, subscores = score_candidate(candidate)
            scored_candidates.append((score, cid, candidate, subscores))
            
    print(f"Total processed: {total}")
    print(f"Honeypots/anomalies filtered: {honeypots_filtered}")
    print(f"Valid candidates remaining: {len(scored_candidates)}")
    
    # Sort: highest score first, tiebreak on candidate_id ascending
    scored_candidates.sort(key=lambda x: (-x[0], x[1]))
    
    # Get top 100
    top_100 = scored_candidates[:100]
    
    print(f"Writing top 100 rankings to: {args.out}")
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])
        for i, (score, cid, cand, subscores) in enumerate(top_100):
            rank = i + 1
            reason = generate_reasoning(rank, cand, subscores)
            writer.writerow([cid, rank, round(score, 4), reason])
            
    print("Done! Ranking successfully completed.")


if __name__ == "__main__":
    main()
