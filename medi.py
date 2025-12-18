# MediAssist - Clinical Expert System
# Course: CT-262 | Introduction to Artificial Intelligence
# Developers: Alizah Baig, Neha Salman

import os
import copy
from datetime import datetime, timezone, timedelta
from collections import Counter

class Result:
    """Stores structured information for each diagnosis outcome."""
    def __init__(self, message, severity="Low", specialty="General Practitioner", notes=""):
        self.message = message
        self.severity = severity
        self.specialty = specialty
        self.notes = notes

    def copy(self):
        return copy.deepcopy(self)

class Node:
    """Binary decision tree node."""
    def __init__(self, question=None, yes=None, no=None, result=None):
        self.question = question
        self.yes = yes
        self.no = no
        self.result = result

ambulance = Node(result=Result(
    "Call an ambulance immediately!",
    severity="Emergency",
    specialty="Emergency Medicine",
    notes="Critical condition: shortness of breath or chest pain"
))
doctor_flu = Node(result=Result("You might have flu or an infection. Visit the doctor.", severity="Medium"))
doctor_injury = Node(result=Result("You might have a physical injury. Consult the doctor.", severity="Medium"))
doctor_food = Node(result=Result("Possible food poisoning. Visit the doctor.", severity="Medium", specialty="Gastroenterology"))
doctor_migraine = Node(result=Result("You may have a migraine. Consult your doctor.", severity="Medium", specialty="Neurology"))
doctor_dehydration = Node(result=Result("Possible dehydration. Drink fluids and visit doctor if persists.", severity="Medium"))
doctor_bp = Node(result=Result("Possible blood pressure issue. Visit the doctor soon.", severity="High", specialty="Cardiology"))
doctor_infection = Node(result=Result("Possible bacterial infection. Visit the doctor soon.", severity="Medium", specialty="Urology"))

home_allergy = Node(result=Result("Allergy detected. Avoid triggers and take antihistamines.", severity="Low", specialty="Allergy"))
home_cold = Node(result=Result("Common cold detected. Stay hydrated and rest well.", severity="Low"))
home_fatigue = Node(result=Result("Fatigue detected. Sleep, rest, and maintain a healthy diet.", severity="Low"))
fine = Node(result=Result("No serious symptoms detected. You're fine for now!", severity="Low"))
home_sore_throat = Node(result=Result(
    "Mild sore throat: try warm honey-lemon water and rest; monitor for 3 days. Visit a doctor if worsens.",
    severity="Low",
    specialty="Home Remedy",
    notes="Home remedy suggested; monitor for 3 days."
))
pulmonology_referral = Node(result=Result(
    "Cough lasting more than 3 weeks — refer to Pulmonology for evaluation.",
    severity="High",
    specialty="Pulmonology",
    notes="Prolonged cough referral (>= 3 weeks)."
))

cough_duration = Node("Has your cough lasted more than 3 weeks?", yes=pulmonology_referral, no=doctor_flu)
breathing = Node("Do you have shortness of breath or chest pain?", yes=ambulance, no=doctor_flu)
sore_throat = Node("Do you have a sore throat or dry cough?", yes=home_sore_throat, no=breathing)
body_ache = Node("Do you feel muscle pain or body ache?", yes=sore_throat, no=home_cold)
itchy_eyes = Node("Do you have itchy eyes or runny nose?", yes=home_allergy, no=home_cold)
rashes = Node("Do you have skin rashes or redness?", yes=home_allergy, no=itchy_eyes)
vomiting = Node("Are you vomiting or have diarrhea?", yes=doctor_food, no=doctor_injury)
stomach_pain = Node("Do you have stomach pain or cramps?", yes=vomiting, no=fine)
injury = Node("Were you hit or injured recently?", yes=doctor_injury, no=stomach_pain)
infection = Node("Do you have burning sensation while urinating?", yes=doctor_infection, no=injury)
headache = Node("Do you have a severe headache?", yes=doctor_migraine, no=home_fatigue)
dizziness = Node("Do you feel dizzy or lightheaded?", yes=doctor_bp, no=headache)
ask_cough = Node("Do you have a cough?", yes=cough_duration, no=body_ache)
flu = Node("Do you have flu-like symptoms (fever, cough, cold)?", yes=ask_cough, no=rashes)
fever = Node("Do you have a fever?", yes=flu, no=dizziness)
root = fever

def get_yes_no(question):
    while True:
        ans = input(question + " (yes/no): ").strip().lower()
        if ans in ("yes", "y"):
            return "yes"
        if ans in ("no", "n"):
            return "no"
        print("Please answer with 'yes' or 'no' (or 'y'/'n').")

def traverse_tree(node, symptoms):
    if node.result:
        return node.result.copy()
    ans = get_yes_no(node.question)
    symptoms.append(f"{node.question} -> {ans}")
    next_node = node.yes if ans == "yes" else node.no
    if next_node is None:
        return Result("Insufficient data to decide. Please consult a healthcare professional.", severity="Medium")
    return traverse_tree(next_node, symptoms)

def adjust_for_age(result, age):
    if result.severity == "Emergency":
        return result
    if age <= 18:
        result.specialty = "Pediatrics"
        if result.notes:
            result.notes += " | Age-based referral applied."
        else:
            result.notes = "Age-based referral applied."
    return result

# create a PST tz object (UTC+5)
_PST_TZ = timezone(timedelta(hours=5))

def save_to_txt(name, age, gender, symptoms, result, feedback):
    """Append full patient record to a text file."""
    # Use timezone-aware current time in PST
    pakistan_now = datetime.now(timezone.utc).astimezone(_PST_TZ)
    # Format with 12-hour hour and AM/PM and append literal 'PST' for label
    timestamp_str = pakistan_now.strftime("%d-%m-%Y %I:%M:%S %p") + " PST"

    with open("patient_records.txt", "a") as f:
        f.write("=== Patient Record ===\n")
        f.write(f"Timestamp: {timestamp_str}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Gender: {gender}\n")
        f.write("Symptoms and Answers:\n")
        for s in symptoms:
            f.write(f"  - {s}\n")
        f.write("\n--- Diagnosis Result ---\n")
        f.write(f"Recommendation: {result.message}\n")
        f.write(f"Severity: {result.severity}\n")
        f.write(f"Specialty: {result.specialty}\n")
        if result.notes:
            f.write(f"Notes: {result.notes}\n")
        if feedback:
            f.write(f"Feedback: {feedback}\n")
        f.write("=========================\n\n")

def weekly_summary():
    """Print summary by reading the text log."""
    if not os.path.exists("patient_records.txt"):
        print("\nNo patient records found for this week yet.")
        return

    # use PST local now for weekly calculation
    now_pst = datetime.now(timezone.utc).astimezone(_PST_TZ)
    year, week, _ = now_pst.isocalendar()

    # Counters
    total_cases = 0
    severity_counter = Counter()
    specialty_counter = Counter()
    helpful_count = 0
    total_feedback = 0

    with open("patient_records.txt") as f:
        record_lines = []
        for line in f:
            line = line.strip()
            if line == "=== Patient Record ===":
                record_lines = []
            elif line.startswith("Severity:"):
                sev = line.split("Severity:")[1].strip()
                severity_counter[sev] += 1
            elif line.startswith("Specialty:"):
                spec = line.split("Specialty:")[1].strip()
                specialty_counter[spec] += 1
            elif line.startswith("Feedback:"):
                fb = line.split("Feedback:")[1].strip().lower()
                total_feedback += 1
                if fb in ("yes", "y", "true", "1"):
                    helpful_count += 1
            elif line.startswith("Timestamp:"):
                total_cases += 1

    print(f"\n--- Weekly Summary (Week {week}, {year}) ---")
    print(f"Total Cases Logged: {total_cases}")
    print("By Severity:", severity_counter)
    print("By Specialty:", specialty_counter)
    if total_feedback:
        print(f"Feedback: {helpful_count}/{total_feedback} marked helpful.")
    else:
        print("Feedback: No feedback entries this week.")
    print()

def main():
    print("\n--- MediAssist: Clinical Expert System ---")
    name = input("Enter patient's name: ").strip() or "Unknown"

    while True:
        try:
            age = float(input("Enter patient's age in years (e.g., 29 or 0.5): ").strip())
            if age <= 0:
                print("please enter correct age")
                continue
            break
        except ValueError:
            print("Please enter a numeric age (e.g., 29 or 0.5).")

    print("\nSelect Gender:")
    print("1. Male")
    print("2. Female")
    print("3. Other")
    print("4. Prefer not to say")

    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            gender = "Male"
            break
        elif choice == "2":
            gender = "Female"
            break
        elif choice == "3":
            gender = "Other"
            break
        elif choice == "4" or choice == "":
            gender = "Prefer not to say"
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print("\nPlease answer the following yes/no questions carefully.\n")
    symptoms = []
    result = traverse_tree(root, symptoms)
    result = adjust_for_age(result, age)

    print("\n--- Diagnosis Result ---")
    print(f"Severity: {result.severity}")
    print(f"Recommendation: {result.message}")
    print(f"Specialty: {result.specialty}")
    if result.notes:
        print(f"Notes: {result.notes}")

    feedback = input("\nWas this advice helpful? (yes/no) [optional]: ").strip().lower()
    save_to_txt(name, age, gender, symptoms, result, feedback)
    print("Patient record saved to 'patient_records.txt'.")

    if get_yes_no("Would you like to view the weekly summary?") == "yes":
        weekly_summary()

    print("\n--- End of Diagnosis ---\n")

if __name__ == "__main__":
    main()