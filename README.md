**MediAssist – Clinical Expert System**

MediAssist is a rule-based clinical expert system developed in Python that provides preliminary medical guidance based on user-reported symptoms.
The system applies expert system principles from Artificial Intelligence, using a binary decision tree to infer possible conditions, assess severity, and recommend appropriate medical actions or specialties.
This project was developed as part of the CT-262: Introduction to Artificial Intelligence course.

Project Purpose

The primary goal of MediAssist is to demonstrate the design and implementation of an AI-based expert system in a healthcare-inspired domain.
The project focuses on:
  - Rule-based reasoning
  - Decision tree inference
  - Knowledge representation
  - User interaction and data logging

System Overview

MediAssist simulates the behavior of a clinical decision-support expert system by asking structured yes/no questions related to common symptoms.
Based on user responses, the system:
1. Traverses a predefined decision tree
2. Infers a possible clinical outcome
3. Assigns a severity level
4. Recommends an appropriate medical specialty or action

Key Features

**- Rule-Based Diagnosis**
  - Binary decision tree structure
  - Yes/No symptom-driven questioning
  - Deterministic inference (no randomness or learning)

**- Severity Assessment**
Each diagnosis is categorized into one of the following levels:
  - Low
  - Medium
  - High
  - Emergency
Emergency cases explicitly advise immediate medical attention.

**- Medical Specialty Recommendation**
Depending on symptoms and severity, the system recommends relevant specialties, including:
  - General Practitioner
  - Emergency Medicine
  - Cardiology
  - Neurology
  - Pulmonology
  - Gastroenterology
    -Pediatrics (age-based)

**- Age-Based Adjustment**
  - Automatically adapts recommendations for patients aged 18 or below
  - Applies pediatric referral logic where appropriate

**- Patient Record Logging**
Each session is logged in a persistent text file (patient_records.txt) containing:
  - Timestamp (Pakistan Standard Time)
  - Patient demographics
  - Symptom responses
  - Diagnosis outcome
  - Severity and specialty
  - Optional user feedback

**- Weekly Case Summary**
The system can generate a weekly analytical summary, including:
  - Total number of cases
  - Distribution by severity
  - Distribution by medical specialty
  - Helpfulness feedback statistics

System Architecture

**Component	**                     **Description**
Knowledge Base	                   Hard-coded medical rules and conditions
Inference Engine	                 Recursive decision tree traversal
User Interface	                   Command Line Interface (CLI)
Data Storage	                     Text-based logging system

Technologies Used

- Programming Language: Python 3
- Standard Libraries:
  - datetime
  - collections
  - copy
  - os
No external dependencies are required.

Artificial Intelligence Concepts Applied

- Expert Systems
- Rule-Based Reasoning
- Decision Trees
- Knowledge-Based Systems
- Inference Mechanisms

Limitations

- The system is purely rule-based and does not learn from data
- Symptom coverage is limited to predefined rules
- Not suitable for real-world medical diagnosis
- Text-based interface only

Future Improvements

- Graphical User Interface (GUI)
- Web-based deployment
- Database integration (SQLite/MySQL)
- Expanded medical knowledge base
- Hybrid rule + machine learning approach

Disclaimer

- This project is developed strictly for educational purposes as part of an academic course.
- It should not be used as a substitute for professional medical consultation or diagnosis.
