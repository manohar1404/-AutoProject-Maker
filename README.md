
---

```markdown
# Ultimate Project Creator 🎉🚀

The **Ultimate Project Creator** is a fun, command-line tool that helps you quickly create project folder structures. It can use AI to generate a tech stack based folder layout or use a default layout. You can also choose to initialize a Git repository and open your new project folder.

---

## Features ✨

- **Interactive CLI:**  
  - Choose or create a parent directory.
  - Enter your project name.
  - Choose between an AI-powered structure or a default layout.
  - Enjoy fun animations like typing effects, loading bars, and spinners.
  
- **AI-Powered Generation:**  
  - Uses the Groq Cloud API to suggest a folder and file structure based on your tech stack (e.g., Next.js, Flask, Django).

- **Default Structure:**  
  - Create a simple structure with folders like `src` and `tests` and files like `README.md` and `.gitignore`.

- **Git Integration:**  
  - Option to initialize a Git repository.

- **Automatic Folder Opening:**  
  - Option to open your project folder automatically in Windows Explorer.

---

## Prerequisites 🛠️

- **Python 3.6+**
- **Groq Python Package:**  
  Install it using:  
  ```bash
  pip install groq
  ```
- **Git:** (optional) for Git repository initialization.
- A valid Groq Cloud API key .

---

## Installation & Setup 📥

1. **Clone or Download** the repository with the script.
2. **Install the Groq Package:**  
   Open a terminal and run:  
   ```bash
   pip install groq
   ```
3. **Configure the Script:**  
   - Set your base directory in the script (`BASE_DIR` is set to `D:\Learning_Projects` by default).
   - The Groq API key is already hardcoded. Replace it if you have your own.

---

## How to Use 💻

1. **Run the Script:**  
   Open a terminal, navigate to the folder with the script, and run:
   ```bash
   python project_creator.py
   ```
2. **Follow the Prompts:**  
   - **Parent Directory:** Select an existing parent directory or type a new one.
   - **Project Name:** Enter your desired project name.
   - **Choose Structure Mode:**  
     - Type `y` to use AI-powered tech stack generation and then enter your tech stack (e.g., "Next.js", "nexjs", "Flask", etc.).  
     - Type `n` if you want to use the default project structure.  
       *If you choose not to use AI, the tool will ask if you want to create the default structure (y/n).*
   - **Git Initialization:** Choose whether to initialize a Git repository.
   - **Open Project Folder:** Choose whether to open your project folder after creation.
3. **Watch the Animations:**  
   Enjoy the typing effects, spinner, and loading bar as the script runs!

---

## Demo Video 🎥





---

## Example Output 📝

```plaintext
🎉 Welcome to the Ultimate Project Creator! 🚀

──────────────────────────────────────────────────
📌 Select a Parent Directory or Create a New One:
   1. AI-Projects
   2. Cloud-Computing
   3. Cybersecurity
   4. Miscellaneous
   5. Web-Development
   6. test

Enter a number to select or type a new category: 6

📂 Enter your project name: my_project

🛠️ Setting up 'my_project' under 'test'...

🤖 Use AI-powered tech stack generation? (y/n): y
🔧 Enter your tech stack (e.g., Next.js, Flask, Django, ): nexjs

🔍 Fetching recommended structure for nexjs...
... (spinner and streaming output) ...

📜 AI-Generated Structure:
📁 pages: This folder contains the page components...
... (more output) ...

⏳ Processing: [████████████████████] ✅

🛠️ Initialize a Git repository? (y/n): y
✅ Git repository initialized!

✅ Project 'my_project' is ready at:
📂 D:\Learning_Projects\test\my_project

📂 Open project folder? (y/n): y
📂 Opened folder: D:\Learning_Projects\test\my_project

✅ Project setup complete!
```

---

## Customization 🔧

- **Base Directory:**  
  Change the `BASE_DIR` variable to change where projects are created.
  
- **Default Structure:**  
  Edit the default structure text in the script to customize the folder layout.

- **Groq API Key:**  
  Replace the  key with your own  .

---

## License 📄

This project is open-source and available under the [MIT License](LICENSE).

---

*Have fun and happy coding! 😄👍*
```

---

Feel free to modify the sections or add more details as needed. Enjoy using the Ultimate Project Creator!
