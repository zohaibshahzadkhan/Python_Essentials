# functions with positional arguments where order of an argument matters
def add_int(num1, num2):
  return num1 + num2;
result = add_int(1.11,2.22);
print(result);

# functions with keyword arguments where order of an argument doesn't matters. All that matters is that the name of the key in the calling code argument
def greetings(reciever, sender):
  print("To "+reciever+" from"+ sender);
greetings(sender=" Khan", reciever="Faizan")

#Assigning a default value to a parameter
def calc_tax(salary, tax = 0.4):
  print(salary * tax);
calc_tax(100)
calc_tax(salary = 100, tax = 0.3);

# function to find value of key in given dictionary 

customers = {
 0: {
  "first name":"John",
  "last name": "Ogden",
  "address": "301 Arbor Rd.",
 },
 1: {
  "first name":"Ann",
  "last name": "Sattermyer",
  "address": "PO Box 1145",
 },
}
def find_something(dictionary, index, key):
  return dictionary[index][key]

result = find_something(customers, 1, "last name");
print(result);

#Dealing with an unknown number of arguments
def personal_info(name,age=15, **otherinfo ):
  print("Your name is " + name);
  print("Your age is " + str(age));

  for key, value in otherinfo.items():
    print(key+":"+value)

personal_info("Zohaib Shahzad", age=25, designation = " Software Engnineer" );
personal_info("Zohaib Shahzad", designation = " Software Engnineer", Stack = "MERN" );

# nested functions
def print_result(value):
  print(value);
def additon(num1 = 5, num2 = 10):
    result = num1 + num2 ;
    print_result(result) 
additon();