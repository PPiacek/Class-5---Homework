# Class-5---Homework

Save housing.csv to your Desktop

Open Terminal to run Python3, once inside type the code found below

```
python3 dataset-processor.py
```

This will run the housing data set, it will display the data in a table,
it will describe the data, and it will plot graphs for you.

```
print(housing_df) -> This prints the data in a Table
```

```
print(housing_df.describe()) -> This describes the data by providing statistics
```

The Plotting code will graph a line & a Scatter Plot Grap 

```
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
```



Thank you for viewing my code.
