import json
import os
from datetime import datetime

# Pythagorean Numerology Alphabet Values
letter_values = {
    'A': 1, 'J': 1, 'S': 1,
    'B': 2, 'K': 2, 'T': 2,
    'C': 3, 'L': 3, 'U': 3,
    'D': 4, 'M': 4, 'V': 4,
    'E': 5, 'N': 5, 'W': 5,
    'F': 6, 'O': 6, 'X': 6,
    'G': 7, 'P': 7, 'Y': 7,
    'H': 8, 'Q': 8, 'Z': 8,
    'I': 9, 'R': 9
}

# Real Vedic Numerology Data Based on Radical (Day) Number (1-9)
numerology_data = {
    1: {
        "evil_num": "6, 8", "fav_color": "Red, Yellow", "fav_day": "Sunday, Monday",
        "fav_god": "Surya (Sun God)", "fav_mantra": "|| Om Hram Hreem Hroum Sah Suryaya Namah ||",
        "fav_metal": "Gold, Copper", "fav_stone": "Ruby", "fav_substone": "Garnet, Red Spinel",
        "friendly_num": "2, 3, 9", "neutral_num": "4, 5, 7", "radical_ruler": "Sun"
    },
    2: {
        "evil_num": "5, 8", "fav_color": "White, Silver", "fav_day": "Monday, Friday",
        "fav_god": "Parvati / Shiva", "fav_mantra": "|| Om Shram Shreem Shroum Sah Chandraya Namah ||",
        "fav_metal": "Silver", "fav_stone": "Pearl", "fav_substone": "Moonstone",
        "friendly_num": "1, 3", "neutral_num": "4, 6, 7, 9", "radical_ruler": "Moon"
    },
    3: {
        "evil_num": "6", "fav_color": "Yellow, Orange", "fav_day": "Thursday, Tuesday",
        "fav_god": "Vishnu / Brihaspati", "fav_mantra": "|| Om Gram Greem Groum Sah Gurave Namah ||",
        "fav_metal": "Gold", "fav_stone": "Yellow Sapphire", "fav_substone": "Topaz, Citrine",
        "friendly_num": "1, 2, 9", "neutral_num": "4, 5, 7, 8", "radical_ruler": "Jupiter"
    },
    4: {
        "evil_num": "1, 2, 9", "fav_color": "Blue, Gray", "fav_day": "Saturday, Sunday",
        "fav_god": "Ganesha", "fav_mantra": "|| Om Bhram Bhreem Bhroum Sah Rahave Namah ||",
        "fav_metal": "Alloy / Mixed", "fav_stone": "Hessonite (Gomed)", "fav_substone": "Agate",
        "friendly_num": "5, 6, 8", "neutral_num": "3, 7", "radical_ruler": "Rahu"
    },
    5: {
        "evil_num": "2", "fav_color": "Green", "fav_day": "Wednesday, Friday",
        "fav_god": "Ganesha / Vishnu", "fav_mantra": "|| Om Bram Breem Broum Sah Budhaya Namah ||",
        "fav_metal": "Gold, Platinum", "fav_stone": "Emerald", "fav_substone": "Peridot, Green Tourmaline",
        "friendly_num": "1, 4, 6", "neutral_num": "3, 7, 8, 9", "radical_ruler": "Mercury"
    },
    6: {
        "evil_num": "1, 2", "fav_color": "White, Pink", "fav_day": "Friday, Wednesday",
        "fav_god": "Devi / Lakshmi", "fav_mantra": "|| Om Dram Dreem Droum Sah Shukraya Namah ||",
        "fav_metal": "Silver", "fav_stone": "Diamond, Opal", "fav_substone": "Zircon, White Sapphire",
        "friendly_num": "4, 5, 8", "neutral_num": "3, 7, 9", "radical_ruler": "Venus"
    },
    7: {
        "evil_num": "1, 2, 9", "fav_color": "Multi-color, Smoky", "fav_day": "Monday, Wednesday",
        "fav_god": "Ganesha / Shiva", "fav_mantra": "|| Om Sram Sreem Sroum Sah Ketave Namah ||",
        "fav_metal": "Silver, Iron", "fav_stone": "Cat's Eye", "fav_substone": "Tiger's Eye",
        "friendly_num": "6, 8", "neutral_num": "3, 4, 5", "radical_ruler": "Ketu"
    },
    8: {
        "evil_num": "1, 2, 9", "fav_color": "Black, Dark Blue", "fav_day": "Saturday, Friday",
        "fav_god": "Shani / Hanuman", "fav_mantra": "|| Om Pram Preem Proum Sah Shanaishcharaya Namah ||",
        "fav_metal": "Iron", "fav_stone": "Blue Sapphire", "fav_substone": "Amethyst, Lapis Lazuli",
        "friendly_num": "4, 5, 6", "neutral_num": "3, 7", "radical_ruler": "Saturn"
    },
    9: {
        "evil_num": "4, 8", "fav_color": "Red", "fav_day": "Tuesday, Thursday",
        "fav_god": "Hanuman / Kartikeya", "fav_mantra": "|| Om Kram Kreem Kroum Sah Bhaumaya Namah ||",
        "fav_metal": "Copper", "fav_stone": "Red Coral", "fav_substone": "Bloodstone, Carnelian",
        "friendly_num": "1, 2, 3", "neutral_num": "5, 6, 7", "radical_ruler": "Mars"
    }
}

# Helper function to reduce numbers to a single digit (e.g., 28 -> 2+8=10 -> 1+0=1)
def reduce_to_single_digit(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

# Function to calculate name number
def calculate_name_number(name):
    total = sum(letter_values.get(char.upper(), 0) for char in name)
    return reduce_to_single_digit(total)

# Main Application Logic
os.system('cls' if os.name == 'nt' else 'clear')

print("╭───────────────────────────────────────────╮")
print("│          NUMEROLOGY CALCULATOR            │")
print("╰───────────────────────────────────────────╯\n")

user_name = input("Enter your full name (e.g., Demo): ")
user_date = input("Enter your date of birth (DD-MM-YYYY, e.g., 06-12-2014): ")

# Parse the date
try:
    day, month, year = map(int, user_date.split('-'))
    
    # 1. Destiny Number (Sum of all digits in the birth date)
    date_sum = sum(int(digit) for digit in f"{day}{month}{year}")
    destiny_number = reduce_to_single_digit(date_sum)
    
    # 2. Radical Number (Sum of the day of birth)
    radical_number = reduce_to_single_digit(day)
    
    # 3. Name Number (Sum of the letters)
    name_number = calculate_name_number(user_name)
    
    # Fetch properties based on the Radical Number
    props = numerology_data[radical_number]
    
    # Build the final dictionary in the EXACT format requested
    final_output = {
        "name": user_name,
        "date": f"{day}-{month}-{year}",
        "destiny_number": destiny_number,
        "radical_number": radical_number,
        "name_number": name_number,
        "evil_num": props["evil_num"],
        "fav_color": props["fav_color"],
        "fav_day": props["fav_day"],
        "fav_god": props["fav_god"],
        "fav_mantra": props["fav_mantra"],
        "fav_metal": props["fav_metal"],
        "fav_stone": props["fav_stone"],
        "fav_substone": props["fav_substone"],
        "friendly_num": props["friendly_num"],
        "neutral_num": props["neutral_num"],
        "radical_num": str(radical_number), # Keeping the string version to match your template
        "radical_ruler": props["radical_ruler"]
    }
    
    # Print the result in JSON format
    print("\n" + "="*45)
    print("✨ YOUR NUMEROLOGY API RESPONSE ✨")
    print("="*45 + "\n")
    
    print(json.dumps(final_output, indent=4, ensure_ascii=False))

except ValueError:
    print("\nError: Please enter the date exactly in DD-MM-YYYY format (e.g., 06-12-2014).")
