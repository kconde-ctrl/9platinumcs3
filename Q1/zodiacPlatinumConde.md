# Chinese Zodiac Coding Exercise

**Name:** Kyle Christopher A. Conde  
**Section:** Platinum  
**Last Name:** Conde  
**Date:** August 12, 2026  

---

## Exercise Requirements

1. Prompt the user for their birth year (Baseline year: 1900).
2. Validate that the input is not earlier than 1900.
3. If invalid, display an error message and abort.
4. Calculate the corresponding Chinese Zodiac sign based on a 12-year cycle starting from 1900.

---

## Python Code Solution (`zodiacPlatinumConde.py`)

```python
zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    index = (birth_year - 1900) % 12
    print(f"Your Chinese Zodiac Sign is: {zodiac_signs[index]}")
