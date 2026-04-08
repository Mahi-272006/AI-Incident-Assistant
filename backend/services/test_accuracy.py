import json
from services.classifier import classify_ticket
from services.priority_service import detect_priority
from services.assignment_service import assign_team

TEST_FILE = "knowledge/test_incidents.json"

with open(TEST_FILE, "r") as f:
    test_data = json.load(f)

total = len(test_data)
correct_category = 0
correct_priority = 0
correct_team = 0

for ticket in test_data:
    text = ticket["ticket"]
    
    predicted_category = classify_ticket(text)
    predicted_priority = detect_priority(text)
    predicted_team = assign_team(text, predicted_category)
    
    if predicted_category == ticket["category"]:
        correct_category += 1
    if predicted_priority == ticket["priority"]:
        correct_priority += 1
    if predicted_team == ticket["assigned_team"]:
        correct_team += 1

print(f"Category Accuracy: {correct_category}/{total} = {correct_category/total*100:.2f}%")
print(f"Priority Accuracy: {correct_priority}/{total} = {correct_priority/total*100:.2f}%")
print(f"Assigned Team Accuracy: {correct_team}/{total} = {correct_team/total*100:.2f}%")