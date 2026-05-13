from pyscript import document, display

class Classmate:
    def __init__(self, name, section, subject):
        self.name = name
        self.section = section
        self.subject = subject

    def intro(self):
        return (f"Hello! I am {self.name} from {self.section} and my favourite subject is {self.subject}!")


class_list = [
    Classmate("Zipporah", "Ruby", "TLE"),
    Classmate("Jai", "Ruby", "ICT"),
    Classmate("Dwayne", "Ruby", "PE"),
    Classmate("Amanda", "Ruby", "ICT"),
    Classmate("Marie", "Ruby", "TLE")
  ]

def add(a):
    document.getElementById('res').innerHTML = ""
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    added = Classmate(name, section, subject)
    class_list.append(added)
    display(f"{name} added successfully!", target="res")



def show(a):
    document.getElementById('output').innerHTML = ""

    for student in class_list:
        intro = student.intro()
        display(intro, target="output")