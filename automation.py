### Python Automation: Project File Validation

import os

project_folder = "my_project"
required_files = [
    "config.json",
    "model.tflite",
    "requirements.txt"
]
print("Starting project validation...")

for file_name in required_files:
    file_path = os.path.join(project_folder, file_name)

    if os.path.exists(file_path):
        print(file_name, "exists - PASS")
    else:
        print(file_name, "missing - FAIL")

print("Project validation completed.")

Starting project validation...
config.json exists - PASS
model.tflite exists - PASS
requirements.txt missing - FAIL
Project validation completed.