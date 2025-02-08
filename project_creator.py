import os
import sys
import time
import subprocess
from groq import Groq  # pip install groq

# =========================
# Configuration & Constants
# =========================

BASE_DIR = "D:\\Learning_Projects"  # Base directory for projects

# Hardcoded Groq Cloud API key
GROQ_API_KEY = "API_KEY_HERE"

# =========================
# Animation & UI Functions
# =========================

def slow_print(text, delay=0.02):
    """Print text with a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(duration=1):
    """Display a simple loading bar animation."""
    sys.stdout.write("⏳ Processing: [")
    sys.stdout.flush()
    for _ in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / 20)
    sys.stdout.write("] ✅\n")
    sys.stdout.flush()

def spinner(duration=2):
    """Display a spinner animation for a given duration."""
    spinner_chars = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in spinner_chars:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")
            if time.time() >= end_time:
                break

def print_separator():
    print("──────────────────────────────────────────────────")

# =========================
# Utility Functions
# =========================

def open_folder(project_path):
    """Opens the given project folder in Windows Explorer."""
    try:
        os.startfile(project_path)
        print(f"📂 Opened folder: {project_path}")
    except Exception as e:
        print("❌ Failed to open folder:", e)

def initialize_git(project_path):
    """Initializes a Git repository in the given project directory."""
    try:
        subprocess.run(["git", "init"], cwd=project_path, check=True)
        print("✅ Git repository initialized!")
    except subprocess.CalledProcessError as e:
        print("❌ Git initialization failed:", e)

def choose_parent_directory():
    """
    Lists existing parent directories under BASE_DIR and lets the user select one or
    enter a new one (using a sorted list for clarity).
    """
    dirs = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
    sorted_dirs = sorted(dirs)
    print_separator()
    slow_print("📌 Select a Parent Directory or Create a New One:\n")
    for i, d in enumerate(sorted_dirs, 1):
        print(f"   {i}. {d}")
    choice = input("\nEnter a number to select or type a new category: ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(sorted_dirs):
            return sorted_dirs[index]
    # Treat input as a new category name.
    new_category = choice
    new_path = os.path.join(BASE_DIR, new_category)
    if not os.path.exists(new_path):
        create_new = input(f"Create new parent directory '{new_category}'? (y/n): ").strip().lower()
        if create_new == "y":
            os.makedirs(new_path, exist_ok=True)
            print(f"📁 Created parent directory: {new_category}")
    return new_category

def create_structure(structure, project_path):
    """
    Parses the provided structure string and creates folders and files.
    Each line starting with "📁" or "📄" is split at the first colon to extract the name.
    """
    lines = structure.strip().splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("📁"):
            folder_name = line.replace("📁", "").strip().split(":", 1)[0].strip()
            if folder_name:
                path = os.path.join(project_path, folder_name)
                os.makedirs(path, exist_ok=True)
                print(f"📁 Created: {folder_name}")
        elif line.startswith("📄"):
            file_name = line.replace("📄", "").strip().split(":", 1)[0].strip()
            if file_name:
                file_path = os.path.join(project_path, file_name)
                with open(file_path, "w") as f:
                    f.write(f"# {file_name} - Auto-generated file")
                print(f"📄 Created: {file_name}")

def default_structure_creation(project_path):
    """Creates a default folder structure with essential files."""
    default_structure = """
    📁 src
    📁 tests
    📄 README.md
    📄 requirements.txt
    📄 .gitignore
    """
    slow_print("\n📂 Creating default project structure...\n")
    spinner(2)
    create_structure(default_structure, project_path)
    slow_print("📁 Standard folder structure created!")

# =========================
# Groq Cloud API Integration
# =========================

def get_ai_generated_structure(tech_stack):
    """
    Uses the Groq Cloud API (via the groq Python package) to generate a project structure
    for the specified tech stack. The returned text should use lines starting with "📁" for
    folders and "📄" for files.
    """
    prompt = (f"Suggest a standard folder structure and essential files for a {tech_stack} project. "
              "Return the answer in plain text with each folder starting with '📁' and each file starting with '📄'.")
    try:
        client = Groq(api_key=GROQ_API_KEY)
        messages = [{"role": "user", "content": prompt}]
        slow_print("\n⏳ Sending request to Groq Cloud API...\n")
        spinner(3)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        response_text = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            sys.stdout.write(content)
            sys.stdout.flush()
            response_text += content
        print()  # New line after streaming output.
        return response_text
    except Exception as e:
        print("❌ Exception calling Groq Cloud API:", e)
        return ""

# =========================
# Main Functionality
# =========================

def main():
    slow_print("\n🎉 Welcome to the Ultimate Project Creator! 🚀\n")
    
    # Step 1: Choose or create a parent directory
    parent_dir = choose_parent_directory()
    
    # Step 2: Get the project name from the user
    project_name = input("\n📂 Enter your project name: ").strip()
    if not project_name:
        print("❌ Project name cannot be empty!")
        return
    project_path = os.path.join(BASE_DIR, parent_dir, project_name)
    if os.path.exists(project_path):
        print("❌ A project with that name already exists!")
        return
    os.makedirs(project_path, exist_ok=True)
    
    print_separator()
    slow_print(f"\n🛠️ Setting up '{project_name}' under '{parent_dir}'...\n")
    
    # Step 3: Choose between AI-powered tech stack generation or default structure
    use_ai = input("🤖 Use AI-powered tech stack generation? (y/n): ").strip().lower()
    if use_ai == "y":
        tech_stack = input("🔧 Enter your tech stack (e.g.,  Next.js + Express, Django + PostgreSQL, React + Node.js, Flutter + Firebase): ").strip()
        if not tech_stack:
            print("❌ Tech stack cannot be empty!")
            return
        slow_print(f"\n🔍 Fetching recommended structure for {tech_stack}...\n")
        structure = get_ai_generated_structure(tech_stack)
        if structure:
            slow_print("\n📜 AI-Generated Structure:")
            print(structure)
            create_structure(structure, project_path)
        else:
            print("❌ Failed to generate structure using AI. Falling back to default structure.")
            default_structure_creation(project_path)
    else:
        # Ask if the user wants to create a default project structure
        create_default = input("📂 Create default project structure? (y/n): ").strip().lower()
        if create_default == "y":
            default_structure_creation(project_path)
        else:
            slow_print("\n⏩ Skipping default project structure creation.")

    loading_bar()

    # Step 4: Optionally initialize a Git repository
    init_git = input("\n🛠️ Initialize a Git repository? (y/n): ").strip().lower()
    if init_git == "y":
        initialize_git(project_path)
    
    print_separator()
    slow_print(f"\n✅ Project '{project_name}' is ready at:\n📂 {project_path}\n")
    
    # Step 5: Optionally open the project folder
    open_proj = input("📂 Open project folder? (y/n): ").strip().lower()
    if open_proj == "y":
        open_folder(project_path)
    
    slow_print("\n✅ Project setup complete!\n")

if __name__ == "__main__":
    main()
