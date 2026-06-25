"""
Agentic Resume Generator Pipeline
Run: python main.py
Reads ALL files from JD/ and Profile_data/, writes a human-readable
consolidated_data.md to Consolidated_data/, then renders the resume.
"""

import os
import glob
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

JD_DIR           = "JD"
PROFILE_DIR      = "Profile_data"
CONSOLIDATED_DIR = "Consolidated_data"
TEMPLATES_DIR    = "Templates"
OUTPUT_DIR       = "Output_Resume"


def _read_files(directory: str) -> dict[str, str]:
    """Read all non-README text files in a directory. Returns {filename: content}."""
    result = {}
    for path in sorted(glob.glob(os.path.join(directory, "*"))):
        if os.path.basename(path).lower() == "readme.md":
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                result[os.path.basename(path)] = f.read()
        except (UnicodeDecodeError, IsADirectoryError):
            pass  # Skip binary files (e.g. .pdf) until parser is added
    if not result:
        raise FileNotFoundError(f"No readable files found in '{directory}/'")
    return result


def read_jd() -> dict[str, str]:
    """Step 1 — Read all JDs from the JD folder."""
    return _read_files(JD_DIR)


def read_profile() -> dict[str, str]:
    """Step 2 — Read all profile sources from Profile_data."""
    return _read_files(PROFILE_DIR)


def consolidate_and_save(jds: dict[str, str], profiles: dict[str, str]) -> str:
    """Step 3 — Merge all sources into a readable .md and write it to Consolidated_data.

    The agent reads this file before rendering. Replace the stub sections below
    with LLM calls to produce structured, JD-tailored content.
    """
    os.makedirs(CONSOLIDATED_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "# Consolidated Resume Context",
        f"_Generated: {timestamp}_",
        "",
        "---",
        "",
        "## Job Descriptions",
        "",
    ]
    for fname, content in jds.items():
        lines += [f"### {fname}", "", content.strip(), ""]

    lines += ["---", "", "## Candidate Profile", ""]
    for fname, content in profiles.items():
        lines += [f"### {fname}", "", content.strip(), ""]

    lines += [
        "---",
        "",
        "## Agent Notes",
        "",
        "<!-- TODO: Replace this section with LLM-generated tailored summary,",
        "     ranked skills, and highlighted experience relevant to the JD above. -->",
        "",
    ]

    md_path = os.path.join(CONSOLIDATED_DIR, "consolidated_data.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return md_path


def select_template() -> str:
    """Step 4 — Select the first available template from Templates/."""
    files = (
        glob.glob(os.path.join(TEMPLATES_DIR, "*.html")) +
        glob.glob(os.path.join(TEMPLATES_DIR, "*.docx"))
    )
    if not files:
        raise FileNotFoundError(f"No template found in '{TEMPLATES_DIR}/'")
    return files[0]


def render_resume(template_path: str, consolidated_path: str) -> str:
    """Step 5 — Render resume from template using the consolidated context."""
    from jinja2 import Template
    with open(template_path, "r", encoding="utf-8") as f:
        template = Template(f.read())
    with open(consolidated_path, "r", encoding="utf-8") as f:
        context_md = f.read()
    # TODO: Parse consolidated_path into structured vars for the template
    return template.render(context=context_md)


def save_output(content: str) -> str:
    """Step 6 — Write the finished resume to Output_Resume."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(OUTPUT_DIR, f"resume_{timestamp}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    return out_path


def main():
    print("── Reading job descriptions ──")
    jds = read_jd()
    print(f"   Found: {list(jds.keys())}")

    print("── Reading profile sources ──")
    profiles = read_profile()
    print(f"   Found: {list(profiles.keys())}")

    print("── Writing consolidated_data.md ──")
    consolidated_path = consolidate_and_save(jds, profiles)
    print(f"   Saved → {consolidated_path}")

    print("── Selecting template ──")
    template_path = select_template()
    print(f"   Using: {template_path}")

    print("── Rendering resume ──")
    rendered = render_resume(template_path, consolidated_path)

    print("── Saving output ──")
    out_path = save_output(rendered)
    print(f"✅ Resume saved → {out_path}")


if __name__ == "__main__":
    main()
