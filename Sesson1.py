print("Welcome")

# Model: Data for your Problem Statement
# oneplusDay1Sales = 150  # A generic Programming Language Variable name declaration
oneplus_day1_sales = 150
oneplus_day2_sales = 150
oneplus_day3_sales = 150

profits_to_amazon_oneplus = 200.27

discounts_sbi_to_oneplus = 3000.12

homeappl_day1_sales = 120
homeappl_day2_sales = 120
homeappl_day3_sales = 120

profits_to_amazon_homeappl = 50

discounts_sbi_to_homeappl = 3000.12

# CONTROLLER : Mathematical Computation or Logical Processing on model

total_oneplus_sales = oneplus_day1_sales + oneplus_day2_sales + oneplus_day3_sales
total_homeappl_sales = homeappl_day1_sales + homeappl_day2_sales + homeappl_day3_sales

net_oneplus_profits = total_oneplus_sales + profits_to_amazon_oneplus
net_homeappl_profits = total_homeappl_sales + profits_to_amazon_homeappl

# View : User Interface to display the data as Text
print("One Plus Sale Profits Made by Amazon ", net_oneplus_profits)
print("Home Appl Sale Profits Made by Amazon ", net_homeappl_profits)