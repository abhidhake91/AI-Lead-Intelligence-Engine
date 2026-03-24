import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

# LOAD CSV
df = pd.read_csv("leads_dataset.csv")

# CONNECT TO POSTGRES
conn = psycopg2.connect(
    host="localhost",
    database="lead_intelligence",
    user="postgres",
    password="your_password"
)

cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
DROP TABLE IF EXISTS leads;

CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    company_size INTEGER,
    industry TEXT,
    website_visits INTEGER,
    email_opens INTEGER,
    budget INTEGER,
    decision_maker INTEGER,
    converted INTEGER
);
""")

conn.commit()

# INSERT DATA (Optimized Way)
insert_query = """
INSERT INTO leads (
    company_size,
    industry,
    website_visits,
    email_opens,
    budget,
    decision_maker,
    converted
) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

execute_batch(cursor, insert_query, df.values)

conn.commit()

print("✅ Data inserted successfully!")

# VERIFY INSERTION
cursor.execute("SELECT COUNT(*) FROM leads;")
count = cursor.fetchone()

print("Total rows in database:", count[0])

cursor.close()
conn.close()