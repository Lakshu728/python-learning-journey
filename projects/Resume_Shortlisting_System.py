# Ai Resume screening system (Mini ATS)
def get_resume():
    '''Take resume details from user'''
    name = input("Enter candidate name: ")
    skills = input("enter skills (comma separated): ")
    
    # convert into list
    skills_list = [skill.strip().lower() for skill in skills.split(",")]
    
    return {"name": name, "skills": skills_list}

def calculate_score(candidate_skills, job_skills):
    '''Match skills and calculate score'''
    match_count = 0
    
    for skill in candidate_skills:
        if skill in job_skills:
            match_count += 1
            
    score = (match_count / len(job_skills)) * 100
    return score

def main():
    print("======== AI Resume Screening system ==========") 
    
    # job Description Input 
    job_input = input("enter required job skills ( comma separated): ")
    job_skills = [skill.strip().lower() for skill in job_input.split(",")]
    
    # number of candidates
    n = int(input("enter number of candidates: "))
    
    candidates = []
    
    # take candidate data
    for i in range(n):
        print(f"\n Enter Details for candidate {i+1}")
        candidate = get_resume()
        
        score = calculate_score(candidate["skills"], job_skills) 
        candidate["score"] = score
        
        candidates.append(candidate)
        
    # sort candidate by score (highest first)
    candidates.sort(key=lambda x:x["score"], reverse=True)
        
        
    #display results
    print("\n ==== Result =====")
    for c in candidates:
         print(f"{c['name']} -> {c['score']:.2f}% match")
            
            
    # top candidate
    print("\n Best Candidate: ") 
    print(f"{candidates[0]['name']} with {candidates[0]['score']:.2f}% match")
        
        
# run program
main()            