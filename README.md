<p align="center">
  <img width="1280" height="640" alt="img" src="https://github.com/user-attachments/assets/4025b357-a6c9-4406-bd2c-ca8677b2c9fd" />
</p>

# skillHER 🎯

## Basic Details

### Team Name: togetHER

### Team Members
- Member 1: Vandhana K U - AISAT
- Member 2: sahala k s - AISAT

### Hosted Project Link
https://skillher.onrender.com

### Project Description
SkillHER is a women-only skill exchange platform designed to create a safe, supportive ecosystem where women can offer skills, request skills, and collaborate through mutual learning.
The platform enables peer-to-peer skill swapping without monetary transactions, focusing on empowerment, accessibility, and confidence-building.

### The Problem statement
Many women possess valuable skills but lack visibility and structured opportunities to share them.
At the same time, many women want to learn new skills but face barriers such as:
High course fees
Competitive environments
Lack of beginner-friendly platforms
Absence of women-focused networking spaces
Existing platforms like LinkedIn and Fiverr are primarily career-driven or monetized, making them less accessible for collaborative, non-commercial skill exchange.
There is currently no dedicated platform that enables women to exchange skills freely within a secure and empowering environment.

### The Solution
SkillHER introduces a structured skill-swap ecosystem where:
Users register with skills they offer and skills they want to learn
The system identifies mutual skill matches
Users can send and manage swap requests
Collaboration happens without financial pressure

The platform prioritizes:
Free access
Ease of use
Beginner-friendly participation
Women-centered community building

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used:  JavaScript, Python,css,html
- Frameworks used: flask 
- Libraries used: Flask- Routing and Backend Handling,
                  Jinja2- Template Rendering
-database used: SQLite3
- Tools used: Visual Studio Code,Git,GitHub

---

## Features

List the key features of your project:
- Feature 1: User Registration
Users can register by providing name, email, skill offered, and skill wanted.
- Feature 2: Skill Match System
The platform automatically identifies mutual skill exchange opportunities between users.
- Feature 3: Swap Request System
Users can send, accept, or reject swap requests.
- Feature 4: Dashboard View
Displays users, their skills, and potential matches.

---

## Implementation

### For Software:

#### Installation
bash
pip install flask


#### Run
bash
[
  git clone https://github.com/vandhanaunni543-eng/skillHER
  cd skillher
  python app.py
]


Then open:
bash
[
  http://127.0.0.1:5000
]




## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![<img width="1920" height="1020" alt="Screenshot 2026-02-28 155324" src="https://github.com/user-attachments/assets/0a2475e6-b4c8-4907-bf74-9f5a24ddb288" />
]
*Homepage displaying introduction and navigation.*

![<img width="1920" height="1020" alt="Screenshot 2026-02-28 155343" src="https://github.com/user-attachments/assets/8b24b37b-7b86-4259-abad-aedd39fe2b6f" />
]
*login page *

![<img width="1920" height="1020" alt="Screenshot 2026-02-28 155426" src="https://github.com/user-attachments/assets/d19a35fb-37f7-4435-b71d-f62ef5611fa2" />
]
*User registration form to enter skill details.*

#### Diagrams

**System Architecture:**

![<img width="1536" height="1024" alt="SkillHER app system architecture diagram" src="https://github.com/user-attachments/assets/b07cb169-2958-4aae-bf10-36737259f57e" />
]
*Explain your system architecture - The application follows a simple client-server architecture:
Frontend: HTML templates rendered using Flask
Backend: Flask application handling routes and logic
Database: SQLite storing user and swap data
Matching Logic: Backend filtering based on skill offered and skill wanted*

**Application Workflow:**

![<img width="1536" height="1024" alt="workflow" src="https://github.com/user-attachments/assets/abc3d3f6-c407-45e0-9c22-65c23abef8b8" />
]
*User registers with skill details
Data is stored in SQLite database
System checks for reciprocal skill matches
Users can send swap requests
Request status is updated and displayed*

---
---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** http://127.0.0.1:5000`

##### Endpoints

**GET /**
- **Description:** Returns landing page.
- **Response:**
HTML Page

**POST /register**
- **Description:** Registers a new user.
- **Request Body:*
    Name
    Email
    Password
    Skill Offerred
    Skill Wanted 

- *Response:*
/dashboard


*POST /login*
- *Description:* Logs in existing user.
- *Request Body:
    Name
    Password

- **Response:**
/dashboard


**POST /dashboard**
- **Description:** Returns dashboard with:
Logged-in user details
Skill matches
Swap requests

- **Response:**
user,match,swap request

---


### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
bash
python app.py


## Project Demo

### Video
https://drive.google.com/file/d/1NQpg05jesuaDOXqhZp_lCYDUDUQwcbrW/view?usp=drivesdk

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** ChatGPT

**Purpose:** 
- Example: Generated UI Components and Backend Help
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Percentage of AI-generated code:** 30%

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions


---

## Team Contributions

- Vandhana K U: Backend and DB
- sahala k s: Frontend

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
