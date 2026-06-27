# Templates Folder

AGENT INSTRUCTION: This folder contains base resume templates. Supported formats: .html, .docx, .pdf, .txt, .tex (LaTeX), or any other readable format. Select the most appropriate template for the target role. If the template is Jinja2-compatible (.html, .txt), render it by injecting consolidated data. For .docx, use python-docx to populate placeholders. For .pdf templates, use them as visual references and reproduce the layout in a generated output file.

AGENT INSTRUCTION: If you encounter a template format not covered above, document how you handled it by appending a new clause to this README under a "## Learned Formats" section.

AGENT INSTRUCTION: If there are multiple templates available in this folder, you MUST explicitly ask the user to select one, and wait for their choice before proceeding. The only exception is if the user has already given instructions on template choice or prompted you with an override like "select whatever you think is the best".

AGENT INSTRUCTION: If you detect a LaTeX template (e.g., a `.tex` file or a directory containing LaTeX template files such as `.tex`, `.cls`, `.sty`):
- Do NOT edit or modify files in the original template directory under `Templates/` directly, to avoid ruining the clean template.
- You MUST copy the entire LaTeX template directory to the output directory (`Output_Resume/`).
- Perform all file edits, placeholders filling, and LaTeX compilation inside that copied directory in `Output_Resume/` to ensure the original template remains pristine.

