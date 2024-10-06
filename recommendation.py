from models import UserProfile
from database import create_connection, close_connection

def fetch_jobs_from_db(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    return jobs

def match_jobs(profile: UserProfile, connection):
    jobs = fetch_jobs_from_db(connection)
    recommendations = []
    
    for job in jobs:
        job['required_skills'] = eval(job['required_skills'])

        if profile.experience_level == job['experience_level'] and \
           profile.preferences.job_type == job['job_type'] and \
           job['location'] in profile.preferences.locations and \
           set(profile.skills).intersection(job['required_skills']):
            recommendations.append({
                "job_title": job['job_title'],
                "company": job['company'],
                "location": job['location'],
                "job_type": job['job_type'],
                "required_skills": job['required_skills'],
                "experience_level": job['experience_level']
            })

    return recommendations
