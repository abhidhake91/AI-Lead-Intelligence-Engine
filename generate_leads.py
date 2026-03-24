import pandas as pd
import numpy as np
import random

# SETTINGS
NUM_LEADS = 1000

industries = ["SaaS", "FinTech", "Ecommerce", "Healthcare", "EdTech"]

data = []

for i in range(NUM_LEADS):

    company_size = random.randint(10, 1000)
    industry = random.choice(industries)
    website_visits = random.randint(1, 30)
    email_opens = random.randint(0, 10)
    budget = random.randint(1000, 50000)
    decision_maker = random.choice([0, 1])

    # Conversion Logic
    
    score = 0

    if website_visits > 15:
        score += 1

    if email_opens > 5:
        score += 1

    if budget > 20000:
        score += 1

    if decision_maker == 1:
        score += 1

    if company_size > 200:
        score += 1

    # Probability-based conversion
    conversion_probability = score / 5
    converted = 1 if random.random() < conversion_probability else 0

    data.append([
        company_size,
        industry,
        website_visits,
        email_opens,
        budget,
        decision_maker,
        converted
    ])

# CREATE DATAFRAME
columns = [
    "company_size",
    "industry",
    "website_visits",
    "email_opens",
    "budget",
    "decision_maker",
    "converted"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("leads_dataset.csv", index=False)

print("✅ leads_dataset.csv created successfully!")