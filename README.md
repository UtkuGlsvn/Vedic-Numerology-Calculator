# 🔮 Vedic Numerology Calculator

A precise, terminal-based Python tool that calculates core numerology numbers (Destiny, Radical, and Name) based on the Pythagorean alphabet and matches them with authentic Vedic Astrology data. 

Unlike random generators, this script uses strict numerological formulas to produce 100% deterministic and accurate results in a clean JSON format.

## ✨ Features

* **Accurate Calculations:** Calculates Destiny Number, Radical (Root/Day) Number, and Name Number using standard numerological reduction rules (reducing numbers to a single digit 1-9).
* **Pythagorean Alphabet System:** Accurately converts names to numbers using the traditional Pythagorean letter-value chart.
* **Authentic Vedic Data:** Returns authentic astrological correspondences for each radical number, including:
    * Ruling Planet / Entity (e.g., Sun, Moon, Jupiter)
    * Favorable Colors, Days, Metals, and Stones
    * Friendly, Neutral, and "Evil" (Incompatible) Numbers
    * Vedic Deities and Specific Mantras
* **JSON Output:** Outputs the final profile in a clean, professional JSON structure, making it easy to integrate into larger applications or APIs.

## 🚀 Getting Started

### Prerequisites

This script requires **Python 3.x**. No external libraries or API keys are needed! It runs completely locally.

### Installation & Usage

1.  Clone this repository or download the script:
    ```bash
    git clone [https://github.com/your-username/vedic-numerology-calculator.git](https://github.com/your-username/vedic-numerology-calculator.git)
    cd vedic-numerology-calculator
    ```
2.  Run the script in your terminal:
    ```bash
    python numerology.py
    ```
3.  Enter your Full Name and Date of Birth when prompted:
    ```text
    Enter your full name (e.g., Demo): John Doe
    Enter your date of birth (DD-MM-YYYY, e.g., 06-12-2014): 25-08-1995
    ```

## 📊 Example Output

The script will instantly calculate your data and return a JSON payload like this:

```json
{
    "name": "John Doe",
    "date": "25-8-1995",
    "destiny_number": 3,
    "radical_number": 7,
    "name_number": 8,
    "evil_num": "1, 2, 9",
    "fav_color": "Multi-color, Smoky",
    "fav_day": "Monday, Wednesday",
    "fav_god": "Ganesha / Shiva",
    "fav_mantra": "|| Om Sram Sreem Sroum Sah Ketave Namah ||",
    "fav_metal": "Silver, Iron",
    "fav_stone": "Cat's Eye",
    "fav_substone": "Tiger's Eye",
    "friendly_num": "6, 8",
    "neutral_num": "3, 4, 5",
    "radical_num": "7",
    "radical_ruler": "Ketu"
}
