import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# STEP 1: Load the dataset
df = pd.read_csv('titanic_cleaned.csv')
print("✅ Dataset loaded!\n")

# STEP 2: Summary statistics
print("📊 Summary:")
print(df.describe())

# STEP 3: Histograms
df.hist(bins=20, figsize=(12, 8))
plt.suptitle("📉 Histograms")
plt.tight_layout()
plt.show()

# STEP 4: Boxplots
sns.boxplot(data=df[['Age', 'Fare']])
plt.title("📦 Boxplot of Age & Fare")
plt.show()

# STEP 5: Pairplot
sns.pairplot(df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']], hue='Survived')
plt.suptitle("🔗 Pairplot", y=1.02)
plt.show()

# STEP 6: Correlation heatmap
numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("🔍 Correlation Matrix")
plt.show()

# STEP 7: Countplots
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("👨‍👩 Survival by Sex")
plt.show()

sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("🛳️ Survival by Class")
plt.show()

# Pause so graphs stay open
input("✅ Press Enter to close...")
