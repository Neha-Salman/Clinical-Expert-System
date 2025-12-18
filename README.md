**MediAssist – Clinical Expert System**

MediAssist is a command-line clinical expert system designed to assist users by providing preliminary medical recommendations based on their symptoms.
It uses a rule-based decision tree to simulate expert reasoning and guide users toward appropriate medical actions such as home care, doctor consultation, specialist referral, or emergency services.

*Disclaimer: This system is for educational purposes only and does not replace professional medical advice.*

Project Objectives

- To demonstrate expert system concepts in Artificial Intelligence
- To apply rule-based reasoning using a decision tree
- To simulate real-world clinical decision-making
- To log patient data and generate weekly analytical summaries

**Key Features**

🔹 Symptom-Based Diagnosis
- Interactive yes/no questions
- Binary decision tree traversal
- Covers common symptoms such as:
  - Fever, cough, flu
  - Headache, dizziness
  - Injuries, infections
  - Allergies, dehydration, BP issues

🔹 Severity Classification
- Low
- Medium
- High
- Emergency

🔹 Specialty Recommendation
Suggests appropriate medical specialties such as:
- General Practitioner
- Emergency Medicine
- Cardiology
- Neurology
- Pulmonology
- Gastroenterology
- Pediatrics (age-based adjustment)

🔹 Age-Based Logic
- Automatically adjusts recommendations for patients 18 years or younger
- Redirects to Pediatrics when applicable

🔹 Patient Record Management
- Stores patient data in patient_records.txt
- Logged details include:
  - Timestamp (Pakistan Standard Time)
  - Name, age, gender
  - Symptoms and answers
  - Diagnosis result
  - Severity & specialty
  - Optional user feedback

🔹 Weekly Summary Report
Displays:
- Total cases logged
- Case distribution by severity
- Case distribution by specialty
- Helpfulness feedback statistics

System Architecture

- Knowledge Representation: Rule-based decision tree
- Inference Mechanism: Depth-first traversal
- Data Storage: Text-based logging
- User Interface: Command Line Interface (CLI)

Technologies Used

- Language: Python 3
- Libraries:
  - datetime
  - collections
  - copy
  - os
