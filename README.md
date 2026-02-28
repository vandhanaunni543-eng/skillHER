10<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [skillHER] 🎯

## Basic Details

### Team Name: [togetHER]

### Team Members
- Member 1: [Vandhana K U] - [aisat]
- Member 2: [sahala k s] - [aisat]

### Hosted Project Link
[https://skillher.onrender.com]

### Project Description
[SkillHER is a women-only skill exchange platform designed to create a safe, supportive ecosystem where women can offer skills, request skills, and collaborate through mutual learning.
The platform enables peer-to-peer skill swapping without monetary transactions, focusing on empowerment, accessibility, and confidence-building.]

### The Problem statement
[Many women possess valuable skills but lack visibility and structured opportunities to share them.
At the same time, many women want to learn new skills but face barriers such as:
High course fees
Competitive environments
Lack of beginner-friendly platforms
Absence of women-focused networking spaces
Existing platforms like LinkedIn and Fiverr are primarily career-driven or monetized, making them less accessible for collaborative, non-commercial skill exchange.
There is currently no dedicated platform that enables women to exchange skills freely within a secure and empowering environment.]

### The Solution
[SkillHER introduces a structured skill-swap ecosystem where:
Users register with skills they offer and skills they want to learn
The system identifies mutual skill matches
Users can send and manage swap requests
Collaboration happens without financial pressure

The platform prioritizes:
Free access
Ease of use
Beginner-friendly participation
Women-centered community building]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used:  JavaScript, Python,css,html]
- Frameworks used: [flask ]
- Libraries used: [Flask (Routing and Backend Handling,
Jinja2 (Template Rendering]
-database used:[sq lite]
- Tools used: [Visual Studio Code,Git,
GitHub]

**For Hardware:**
- Main components: [List main components]
- Specifications: [Technical specifications]
- Tools required: [List tools needed]

---

## Features

List the key features of your project:
- Feature 1: [User Registration
Users can register by providing name, email, skill offered, and skill wanted.]
- Feature 2: [Skill Match System
The platform automatically identifies mutual skill exchange opportunities between users.]
- Feature 3: [Swap Request System
Users can send, accept, or reject swap requests.]
- Feature 4: [Dashboard View
Displays users, their skills, and potential matches.]

---

## Implementation

### For Software:

#### Installation
```bash
[pip install flask]
```

#### Run
```bash
[cd skillher
python app.py]```
Then open:

http://127.0.0.1:5000



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

**GET /api/endpoint**
- **Description:** [Returns a list of all registered users]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Anu",
      "skill_offered": "Graphic Design",
      "skill_wanted": "Python"
    }
  ]
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:*
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
