class Teacher():
  def __init__(self, first_name,last_name):
    self.first_name = first_name
    self.last_name = last_name

  def print_fullname(self):
    print(self.first_name +" "+ self.last_name);
  def change_lastname(self, new_last_name):
    self.last_name = new_last_name;

teacher_one = Teacher("Zohaib","Shahzad");
teacher_one.change_lastname("Shahzad Khan")
teacher_one.print_fullname();
# print(teacher_one.first_name +" " + teacher_one.last_name);