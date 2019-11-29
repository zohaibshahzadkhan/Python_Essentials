user_name = input("Please enter your name \n");
monthly_income = input("Please enter your monthly income \n");
yearly_income = 12 * int(monthly_income);
print(user_name.title());
print( "Your Yearly income is " + str(yearly_income));

cities = ["karachi", "lahore", "islamabad"];
input_city = input("Enter city name \n");
for city in cities:
  if input_city.lower() == city:
    print(input_city + " is a clean city");
    break;
  else: 
    print(input_city + " is not a clean city");