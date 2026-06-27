# Resume Generation Guide for Agentic AI

This repository is designed as a structured workspace and guide for an Agentic AI to generate highly tailored, high-quality resumes. The workspace contains subordinate directories with specific README files detailing how to interact with each part of the system.

---

## 🚀 How to Handle Prompts (e.g., "generate resume")

When you receive a prompt to **"generate resume"**, **"tailor my resume"**, or any similar instruction, follow this step-by-step workflow:

### Step 1: Parse and Validate Job Description(s) (in `JD/`)
- Read and process all files in the [JD/](file:///mnt/WindowsDrive/Fedora/Projects/Resume/JD/) folder.
- **CRITICAL**: The [JD/](file:///mnt/WindowsDrive/Fedora/Projects/Resume/JD/) folder **must never be empty**. If there are no job descriptions, immediately halt execution and request a job description from the user.
- **Multiple JDs**: If there are multiple Job Descriptions in the folder, you must synthesize their requirements and fit **ALL** of them into the target resume.
- **Company Research**: Use web search or look up details about the target company (its domain, culture, technology stack, and values). You must gather detailed info about the target company and use it to adjust the resume tone, highlight relevant experience, and select matching keywords.

### Step 2: Read Profile Data (in `Profile_data/`)
- Read all files in the [Profile_data/](file:///mnt/WindowsDrive/Fedora/Projects/Resume/Profile_data/) directory to extract the user's master career history, skills, and projects.

### Step 3: Synthesize Tailored Profile (in `Consolidated_data/`)
- Synthesize a consolidated profile matching the target JD(s) and company.
- Identify and list any gaps (skills/qualifications in JD but missing in Profile_data) in the synthesis markdown file under a `## Missing / Gaps` section.

### Step 4: Choose Template (in `Templates/`)
- Check the available templates in the [Templates/](file:///mnt/WindowsDrive/Fedora/Projects/Resume/Templates/) folder.
- **Template Selection Logic**: If there is more than one template available, you **MUST FORCE the user to select one** template (by asking/prompting them explicitly) and pause until they respond.
  - *Exception*: Do not prompt if the user has already specified a template in their initial instruction or provided an override like *"select whatever you think is the best"* or similar instructions.

### Step 5: Generate Output (in `Output_Resume/`)
- Fill the selected template with the consolidated data.
- **LaTeX Template Compatibility**:
  - If a LaTeX template is detected (e.g., a `.tex` file or a subdirectory containing `.tex`, `.cls`, or `.sty` files):
    - **Do NOT edit or modify** files in the original template directory under `Templates/` directly, to avoid ruining the clean template.
    - You **must copy the entire LaTeX template directory** to the output directory ([Output_Resume/](file:///mnt/WindowsDrive/Fedora/Projects/Resume/Output_Resume/)) first.
    - Perform all edits, personalization, and LaTeX compilation within that copied directory in `Output_Resume/`.
- Save the final resume in the output folder following the naming convention: `YYYYMMDD_JobTitle_Resume`.

---

## 🔒 Security & Password Handling
If a password, API key, or access credential is required to access external files, build systems, or services, the agent must securely prompt the user for input and handle it in memory. Never write raw passwords, keys, or security tokens to the repository files or log outputs.
