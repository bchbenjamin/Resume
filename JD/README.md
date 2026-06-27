# JD Folder

AGENT INSTRUCTION: This folder contains the target Job Description. Supported formats: .txt, .pdf, .docx, .html. Whenever asked to generate a resume, your first step is to read all files in this folder. Parse HTML files by extracting visible text content (strip tags). Use this to identify required skills, keywords, qualifications, and tone for the role.

AGENT INSTRUCTION: If you encounter a file format not listed above, attempt to read it as plain text. If successful, append a note about the format to this README under a "## Learned Formats" section.

AGENT INSTRUCTION: After parsing the JD, explicitly flag any required qualifications, skills, or experiences that are absent from Profile_data. List these gaps in the Consolidated_data synthesis file under a "## Missing / Gaps" section so the user can address them.

AGENT INSTRUCTION: Ensure that this folder is never empty. If no Job Description file is present, do not proceed and ask the user to provide one.

AGENT INSTRUCTION: If there are multiple Job Descriptions (JDs) in this folder, you must synthesize and fit ALL the JDs' requirements, skills, and qualifications into the output resume.

AGENT INSTRUCTION: You must perform research to get a lot of information about the company that the JD is targeting (using web search or extracting details from the JD/public profile). Use this company info to align the resume's tone, highlight matching cultural/technical values, and optimize keywords for that specific company.

