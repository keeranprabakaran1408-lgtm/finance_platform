import numpy as np
from faker import Faker
import datetime as dt

START_DATE = dt.datetime(2025, 10, 1)
END_DATE = dt.datetime(2026, 9, 30)
FRAUD_RATE = 0.015
MESS_RATE = 0.014
SEED = 12345
fake = Faker("en_GB")
fake.seed_instance(SEED)
print(fake.name())
NUM_CUSTOMERS = 300
rng = np.random.default_rng(SEED)
rints = rng.integers(low=0, high=10, size=3)
print(rints)
print(type(rints[0]))
print(END_DATE - START_DATE)

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
print(CATEGORIES.keys())

def main():
    pass
if __name__ == "__main__":
    main()