# meal-plan-generator

This project generates personalized meal plans based on user input and nutritional information from the Open Food Facts database.

## Project Overview

The project involves data cleaning, clustering using machine learning, and generating meal plans that meet specific macronutrient requirements.

## Notebooks Breakdown

### Notebook 1: Data Preparation and Clustering

- **Download and clean data from Open Food Facts**
- **Apply TF-IDF vectorization and KMeans clustering to group similar food items**
- **Manually name the resulting clusters**
- **Output the processed data into a CSV file for further use**

### Notebook 2: Meal Plan Generation

- **Take user input regarding dietary preferences and macronutrient goals**
- **Generate a meal plan that meets the specified requirements**
- **Adjust serving sizes to optimize the meal plan for the given macros**
- **Output the final suggested meal plan and total daily macronutrients**

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/jonathanli42/meal-plan-generator.git
   cd meal-plan-generator

2. Install dependencies:

pip install -r requirements.txt


## Usage
Open and run the Jupyter notebooks in the following order:

filter_data.ipynb
calculate_meal_plan.ipynb
Provide user input in calculate_meal_plan.ipynb to generate a personalized meal plan

## Data Source
This project uses data from Open Food Facts. Open Food Facts is a database of food products from around the world, with information on ingredients, nutrition facts, and more.
https://world.openfoodfacts.org/data

## Contributions
Feel free to fork the repository, create issues for bugs or feature requests, and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
