import faker
import psycopg2
import random
from datetime import datetime

fake = faker.Fake()

def generate_transaction():
    user= fake.simple_profile()


    return   {
        "transactionId": fake.uuid4(),
        "userId": user['username'],
        "timestamp": datetime.utcnow().timestamp(),
        "amount": round(random.uniform(10, 1000),2),
        "currency": random.choice(['USD','GBP']),
        "merchantName": fake.compute(),
        "paymentMethod": random.choice(['credit_card', 'debit_card','online_transfer']),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(['','DISCOUNT10','']),
        "afiiliated Id": fake.uuid4()
    }

def create_table(conn):
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id VARCHAR(255),
            user_id VARCHAR(255),
            timestamp TIMESTAMP,
            amount DECIMAL,
            currency VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            merchant_name VARCHAR(255),
            payment_method VARCHAR(255),
            ip_adress VARCHAR(255),
            voucher_code VARCHAR(255),
            affiliateId VARCHAR(255)
        )
        """
    )

    cursor.close()
    conn.commit()

