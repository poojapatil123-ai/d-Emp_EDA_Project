# import modules
from src.load_data import load_data
from src.preprocessing import*
from src.analysis import*
from src.visualization import*
from src.report import generate_report

# create the required folder
os.makedirs("images",exist_ok=True)
os.makedirs("reports",exist_ok=True)

# load the dataset
print("\n" + "=" *60)
print("Loading Dataset")
print("=" *60)

df= load_data("data/employee_data.csv")

# Data Preprocessing
print("\n" + "=" *60)
print("DATA PREPROCESSING")
print("=" *60)

dataset_info(df)

check_missing_value(df)

df= remove_duplicates(df)

save_clean_data(df)

# Business Analyst

print("\n" + "=" *60)
print("BUSINESS ANALYSIS")
print("=" *60)

average_salary(df)

highest_salary(df)

lowest_salary(df)

department_salary(df)

city_salary(df)

gender_salary(df)

education_salary(df)

performance_count(df)

work_mode_count(df)

top_5_salary(df)

bottom_5_salary(df)

# Data Visulization
print("\n" + "=" *60)
print("GENERATING VISUALIZATION")
print("=" *60)

age_distrubution(df)

salary_distrubution(df)

department_count(df)

gender_count(df)

education_count(df)

work_mode_count(df)

performance_count(df)

salary_boxplot(df)

age_boxplot(df)

exeperiance_vs_salary(df)

department_salary(df)

city_salary(df)

# Genearte PDF Report

print("\n" + "="*60)
print("Generate pdf report")
print("=" *60)

generate_report(df)

# Project Completed

print("\n" + "="*60)
print("Project completed succesfully")
print("=" *60)