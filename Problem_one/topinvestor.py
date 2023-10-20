import pandas as pd

# Read the dataset
data = pd.read_csv('transaction_data.csv')

# Group the data by investor ID and count the unique syndicates for each investor
investors = data.groupby('Investor ID')['Syndicate ID'].nunique().reset_index()

# Sort the investors by the number of unique syndicates in descending order
investors = investors.sort_values('Syndicate ID', ascending=False)

# Get the top 5 investors
top_investors = investors.head(5)

# Get the total amount invested by each of the top investors
investments = data.groupby('Investor ID')['Transaction Amount'].sum().reset_index()
top_investors['Total Amount Invested'] = top_investors['Investor ID'].map(investments.set_index('Investor ID')['Transaction Amount'])

# Print the top 5 investors and their total investment amount
print(top_investors)
 