import numpy as np
rng = np.random.default_rng(12345)
rints = rng.integers(low=0, high=10, size=3)
print(rints)
print(type(rints[0]))

CATEGORIES = {
    "groceries":{
         "businesses": ["Tesco", "Morrisons", "Sainsbury's"],
            "amount_range": (1, 200),
            

    },
    "entertainment":{
        "businesses": ["Netflix", "Spotify", "Disney+"],
        "amount_range": (1, 30),
    },
    "utilities":{
        "businesses": ["British Gas", "EDF Energy", "Thames Water"],
        "amount_range": (50, 300),
    },
    "transportation":{
        "businesses": ["Uber", "TFL", "Trainline"],
        "amount_range": (5, 100),
    },
    "eating Out":{
        "businesses": ["McDonald's", "KFC", "Costa Coffee"],
        "amount_range": (1, 200),
    },
    "travel":{
        "businesses": ["Expedia", "Booking.com", "Airbnb"],
        "amount_range": (50, 2000),
    },
    "healthcare":{
        "businesses": ["Boots", "Superdrug", "NHS"],
        "amount_range": (5, 500),
    },
    "education":{
        "businesses": ["OneDrive", "Pmt", "Duolingo"],
        "amount_range": (10, 500),
    },
    

   
}
print(CATEGORIES.keys())

def main():
    pass
if __name__ == "__main__":
    main()