# list is a variable that can have a sequence of values assigned to it.
stacks = ["MEAN", "MERN"];
print("welcome to " + stacks[1] + " stack");

#add the item at the end of list
stacks.append("FULLSTACK");
stacks = stacks + ["LAMP"];

#add the item at specifix index of list
stacks.insert(0, "WAMP");

#taking the slice out 
interested_stack = stacks[2:3];
interested_stack_till_index2 = stacks[:3];
interested_stack_from_index2 = stacks[2:];
print(stacks);
print(interested_stack);
print(interested_stack_till_index2);
print(interested_stack_from_index2);

#deleting element from list 
mobiles = ["Samsung", "Iphone", "Nokia" ];
del mobiles[0];
mobiles.remove("Iphone")
print(mobiles[:1]);

#popping Elements
home_tasks = ["email", "call", "meet"];
work_tasks = ["lecture", "code"];
work_tasks.append(home_tasks.pop(2))
print(home_tasks)
print(work_tasks)