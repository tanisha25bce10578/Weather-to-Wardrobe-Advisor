Project Overview: Choosing what to wear can be tricky when the temperature differs from the actual number. This project solves that by:

1. Calculating a heat index based on humidity and temperature.
   
2. Analyzing historical data to find the most similar weather days in the past.
   
3. Learning from previous run feedback to improve its future suggestions.
   
 Key Features:-
 
a) Smart Calculation: Uses the formula for humidity when the temperature is above 26°C.

b) k-NN Algorithm: It looks at the 3 nearest historical data points (based on temperature and wind) to suggest an outfit.

c) Storage: Saves your preferences in a commute_log.json file so it remembers your choices even after you close the program.

d) Interactive Learning: If the preffered clothes are uncomfortable, it will update to your more preffered clothes.

 How to Run:-
 
Requirement: Check you have Python installed.

Run the script: Bashpython wardrobe_advisor.py( any name you want)

Input data: Enter the temperature, humidity, and wind speed.

Feedback: Type yes if the suggestion is good, or no to teach the program a better option.

Future Scope:-

API Integration: Automatically fetch weather data from the internet.

Features: it includes UV Index (for sunglasses) or Rain Probability (for umbrellas).
