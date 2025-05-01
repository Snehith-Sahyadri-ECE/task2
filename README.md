# Task 2 - Exploratory Data Analysis (EDA)

## 🎯 Objective
Use EDA techniques to explore the Titanic dataset using statistics and visualizations.

## 🛠️ Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn

## 📁 Dataset
- Used cleaned dataset from Task 1: `titanic_cleaned.csv`

## 🔍 What I Did
1. Loaded cleaned data
2. Displayed summary statistics (mean, std, median, etc.)
3. Created:
   - Histograms for Age, Fare
   - Boxplots for Age and Fare
   - Pairplot to explore relationships between features
   - Correlation heatmap
   - Countplots for Survived vs Sex & Pclass

## 📈 How to Run

### Install dependencies:
```bash
pip install pandas seaborn matplotlib
✅ Dataset loaded!

📊 Summary:
       PassengerId    Survived  ...       Parch          Fare
count   889.000000  889.000000  ...  889.000000  8.890000e+02
mean    446.000000    0.382452  ...    0.382452  1.478632e-16
std     256.998173    0.486260  ...    0.806761  1.000563e+00
min       1.000000    0.000000  ...    0.000000 -6.462044e-01
25%     224.000000    0.000000  ...    0.000000 -4.872378e-01
50%     446.000000    0.000000  ...    0.000000 -3.551972e-01
75%     668.000000    1.000000  ...    0.000000 -2.207954e-02
max     891.000000    1.000000  ...    6.000000  9.668551e+00

[8 rows x 8 columns]
