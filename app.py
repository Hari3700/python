import pandas as pd
import json

# Step 1: Load your business data
df = pd.read_csv("11.csv")

# Step 2: Define question templates
intents = []
for i, row in df.iterrows():
    biz = row['business_name']
    
    qas = [
        (f"Who is the owner of {biz}?", row['owner_name']),
        (f"What is the designation of the owner of {biz}?", row['owner_designation']),
        (f"What is the gender of the owner of {biz}?", row['owner_gender']),
        (f"What is the category of the owner of {biz}?", row['owner_category']),
        (f"What is the contact of {biz}?", row['business_contact']),
        (f"What is the email of {biz}?", row['business_email']),
        (f"What is the business industry of {biz}?", row['business_industry']),
        (f"What is the business activity of {biz}?", row['business_activity']),
        (f"What is the address of {biz}?", row['business_address']),
        (f"What is the district of {biz}?", row['business_district']),
        (f"What is the state of {biz}?", row['business_state']),
        (f"What is the pincode of {biz}?", row['business_pincode'])
    ]
    
    for j, (question, answer) in enumerate(qas):
        intents.append({
            "tag": f"business_{i}_{j}",
            "patterns": [question],
            "responses": [str(answer)]
        })

# Step 3: Save to chatbot-friendly JSON format
chatbot_data = {"intents": intents}
with open("business_chatbot_data.json", "w", encoding="utf-8") as f:
    json.dump(chatbot_data, f, indent=4)

print("✅ Business chatbot data saved to business_chatbot_data.json")
