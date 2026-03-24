import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="lead_intelligence",
        user="postgres",
        password="your_password"
    )

    print("✅ Connection successful!")

    conn.close()

except Exception as e:
    print("❌ Connection failed")
    print(e)