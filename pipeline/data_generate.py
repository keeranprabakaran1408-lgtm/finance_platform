import numpy as np
from faker import Faker
import datetime as dt

START_DATE = dt.datetime(2025, 10, 1)
END_DATE = dt.datetime(2026, 10, 1)
FRAUD_RATE = 0.015
MESS_RATE = 0.014
SEED = 12345
fake = Faker("en_GB")
fake.seed_instance(SEED)
NUM_CUSTOMERS = 300
rng = np.random.default_rng(SEED)
CATEGORIES = {
    "groceries":{
         "businesses": ["Tesco", "Morrisons", "Sainsbury's","Asda", "Aldi" ],
            "amount_range": (10, 120),
            "recurring": False,

    },
    "entertainment":{
        "businesses": ["Netflix", "Spotify", "Disney+"],
        "amount_range": (1, 30),
        "recurring": True,
    
    },
    "utilities":{
        "businesses": ["British Gas", "EDF Energy", "Thames Water"],
        "amount_range": (50, 300),
        "recurring": True,
    },
    "transportation":{
        "businesses": ["Uber", "TFL", "Trainline"],
        "amount_range": (5, 100),
        "recurring": False,
    },
    "eating_out":{
        "businesses": ["McDonald's", "KFC", "Costa Coffee"],
        "amount_range": (3, 40),
        "recurring": False,
    },
    "travel":{
        "businesses": ["Expedia", "Booking.com", "Airbnb"],
        "amount_range": (50, 600),
        "recurring": False,
    },
    "healthcare":{
        "businesses": ["Boots", "Superdrug", "NHS"],
        "amount_range": (3, 40),
        "recurring": False,
    },
    "education":{
        "businesses": ["Waterstones", "WHSmith", "Duolingo"],
        "amount_range": (5, 60),
        "recurring": False,
    },
    

   
}
def generate_customer_data(num_customers):
    customers = []
    for _ in range(num_customers):
        favourite = {}

        for category, details in CATEGORIES.items():
            quantity = int(rng.integers(1,3))
            shops = rng.choice(details["businesses"], size=quantity, replace=False).tolist()
            favourite[category] = shops
        customer = {
            "customer_id": fake.uuid4(),
            "name": fake.name(),
            "home_country": str(rng.choice(["GB", "US", "FR"], p=[0.9,0.05, 0.05])),
            "spend_multiplier": round(rng.uniform(0.6,1.6),2),
            "favourite_businesses": favourite
        }
        customers.append(customer)
    return customers

def main():
    customers = generate_customer_data(NUM_CUSTOMERS)
    print(len(customers))
    for customer in customers[0:3]:
        print(customer)
if __name__ == "__main__":
    main()