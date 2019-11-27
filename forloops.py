first_names = ['Martin', 'Alberto', 'John', 'Nancy'];
last_names = ['Fix', 'Delrio', 'Smith', 'Percy'];
full_name = [];
for first_name in first_names:
  for last_name in last_names:
    full_name.append(first_name + last_name);
print(full_name) 