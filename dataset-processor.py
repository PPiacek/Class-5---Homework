import pandas as pd
import os
import matplotlib.pyplot as plt

# Creating Dataframe from Files
housing_df = pd.read_csv(filepath_or_buffer='~/Desktop/housing.csv',
                     sep='\s+',
                     header=None)

#Adding Header
housing_df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

#Print as Table & Describe
print(housing_df)
print(housing_df.describe())

os.makedirs('plots', exist_ok=True)

#Ploting line
plt.plot(housing_df['TAX'], color='Black')
plt.title('Tax by Index')
plt.xlabel('index')
plt.ylabel('Tax')
plt.savefig(f'plots/tax_by_index.png', format='png')
plt.clf()

#Plotting Scatter
plt.scatter(housing_df['RM'], housing_df['TAX'], color='Blue')
plt.title('Rooms to Tax')
plt.xlabel('Rooms')
plt.ylabel('Tax')
plt.savefig(f'plots/rooms_to_tax.png', format='png')

plt.close()

