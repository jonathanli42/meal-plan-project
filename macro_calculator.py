# miffin st jeor equation

macro_ratios = {
    # For Losing Weight
    ('Lose', 'Balanced'): {'Carbohydrates': 40, 'Protein': 30, 'Fat': 30},
    ('Lose', 'Keto'): {'Carbohydrates': 5, 'Protein': 25, 'Fat': 70},
    ('Lose', 'High Protein'): {'Carbohydrates': 30, 'Protein': 40, 'Fat': 30},
    ('Lose', 'Low Fat'): {'Carbohydrates': 50, 'Protein': 30, 'Fat': 20},
    ('Lose', 'Vegetarian'): {'Carbohydrates': 40, 'Protein': 30, 'Fat': 30},
    ('Lose', 'Vegan'): {'Carbohydrates': 45, 'Protein': 30, 'Fat': 25},
    ('Lose', 'Paleo'): {'Carbohydrates': 30, 'Protein': 40, 'Fat': 30},

    # For Maintaining Weight
    ('Maintain', 'Balanced'): {'Carbohydrates': 50, 'Protein': 25, 'Fat': 25},
    ('Maintain', 'Keto'): {'Carbohydrates': 5, 'Protein': 20, 'Fat': 75},
    ('Maintain', 'High Protein'): {'Carbohydrates': 40, 'Protein': 35, 'Fat': 25},
    ('Maintain', 'Low Fat'): {'Carbohydrates': 60, 'Protein': 20, 'Fat': 20},
    ('Maintain', 'Vegetarian'): {'Carbohydrates': 50, 'Protein': 25, 'Fat': 25},
    ('Maintain', 'Vegan'): {'Carbohydrates': 55, 'Protein': 20, 'Fat': 25},
    ('Maintain', 'Paleo'): {'Carbohydrates': 40, 'Protein': 30, 'Fat': 30},

    # For Gaining Weight
    ('Gain', 'Balanced'): {'Carbohydrates': 50, 'Protein': 20, 'Fat': 30},
    ('Gain', 'Keto'): {'Carbohydrates': 5, 'Protein': 15, 'Fat': 80},
    ('Gain', 'High Protein'): {'Carbohydrates': 40, 'Protein': 30, 'Fat': 30},
    ('Gain', 'Low Fat'): {'Carbohydrates': 55, 'Protein': 25, 'Fat': 20},
    ('Gain', 'Vegetarian'): {'Carbohydrates': 50, 'Protein': 20, 'Fat': 30},
    ('Gain', 'Vegan'): {'Carbohydrates': 60, 'Protein': 15, 'Fat': 25},
    ('Gain', 'Paleo'): {'Carbohydrates': 35, 'Protein': 35, 'Fat': 30},
}


def basic_metabolic_rate(age, gender, weight, height, metric_type):
    BMR = 0
    # miffin st jeor equation
    # basic metabolic rate
    if metric_type == 'Imperial':
        weight = 0.45359237 * weight
        height = height * 2.54
    elif metric_type == 'International System':
        weight = weight
        height = height
    if gender == 'male':
        BMR = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        BMR = 10 * weight + 6.25 * height - 5 * age - 161

    return BMR


def total_daily_energy_expenditure(activity_level, BMR):
    TDEE = 0
    # harris benedict equation
    # TDEE - Total Daily Energy Expenditure
    if activity_level == 'Sedentary':
        TDEE = BMR * 1.2
    elif activity_level == 'Lightly Active':
        TDEE = BMR * 1.375
    elif activity_level == 'Moderately Active':
        TDEE = BMR * 1.55
    elif activity_level == 'Very Active':
        TDEE = BMR * 1.725
    elif activity_level == 'Super Active':
        TDEE = BMR * 1.9

    return TDEE


def diet_goals(goal, diet_type):
    return macro_ratios.get((goal, diet_type))


def macro_converter(TDEE, macro_breakdown):
    carbs = macro_breakdown['Carbohydrates'] / 100
    fats = macro_breakdown['Fat'] / 100
    protein = macro_breakdown['Protein'] / 100

    tdee_carbs = TDEE * carbs
    tdee_fats = TDEE * fats
    tdee_protein = TDEE * protein

    macro_breakout = {
        'Carbohydrates': tdee_carbs / 4,
        'Protein': tdee_protein / 4,
        'Fats': tdee_fats / 9
    }

    return macro_breakout


BMR = basic_metabolic_rate(27, 'male', 185, 72, 'Imperial')
tdee = total_daily_energy_expenditure('Very Active', BMR)
macro_breakdown = diet_goals('Maintain', 'Balanced')

print(f"BMR: {BMR}")
print(f"TDEE: {tdee}")
print(f"Macro Breakdown: {macro_breakdown}")
print(macro_converter(tdee, macro_breakdown))
