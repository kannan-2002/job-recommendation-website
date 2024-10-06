document.getElementById('userForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    // Gather form input data
    const name = document.getElementById('name').value;
    const skills = document.getElementById('skills').value.split(',').map(skill => skill.trim());
    const experience_level = document.getElementById('experience').value;
    const desired_roles = document.getElementById('roles').value.split(',').map(role => role.trim());
    const locations = document.getElementById('locations').value.split(',').map(location => location.trim());
    const job_type = document.getElementById('job_type').value;

    // Build the user profile object
    const profile = {
        name: name,
        skills: skills,
        experience_level: experience_level,
        preferences: {
            desired_roles: desired_roles,
            locations: locations,
            job_type: job_type
        }
    };

    // Send profile to backend
    const response = await fetch('/recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(profile),
    });

    // Display the recommendations
    const data = await response.json();
    const recommendations = data.recommendations;

    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<h3>Recommended Jobs:</h3>';

    if (recommendations.length > 0) {
        recommendations.forEach(job => {
            resultsDiv.innerHTML += `
                <div class="card mb-3">
                    <div class="card-body">
                        <h5 class="card-title">${job.job_title}</h5>
                        <p class="card-text">Company: ${job.company}</p>
                        <p class="card-text">Location: ${job.location}</p>
                        <p class="card-text">Job Type: ${job.job_type}</p>
                        <p class="card-text">Experience Level: ${job.experience_level}</p>
                        <p class="card-text">Required Skills: ${job.required_skills.join(', ')}</p>
                    </div>
                </div>
            `;
        });
    } else {
        resultsDiv.innerHTML += `<p>No matching jobs found.</p>`;
    }
});
