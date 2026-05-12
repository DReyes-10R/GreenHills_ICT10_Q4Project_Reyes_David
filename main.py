from pyscript import display, document, HTML
import matplotlib.pyplot as plt
import logging

logging.getLogger('matplotlib').setLevel(logging.WARNING)

# ================= CLASSMATES =================

class Classmate:
    def __init__(self, name, section, favourite_subject):
        self.name = name
        self.section = section
        self.favourite_subject = favourite_subject

    def introduce(self):
        return f"Hello! I am {self.name} from {self.section}. My favorite subject is {self.favourite_subject}."


students = [
    Classmate('Joaquin Oliveros', 'Ruby', 'Science'),
    Classmate('Bryce Ong', 'Ruby', 'Math'),
    Classmate('Zakari Dimaculangan', 'Ruby', 'Social Studies'),
    Classmate('Dweyen Evangelista', 'Ruby', 'PE'),
    Classmate('Kobe Baylon', 'Ruby', 'Science')
]


def show_list(e):
    document.getElementById("output").innerHTML = ""
    for s in students:
        display(s.introduce(), target="output")


def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name == "":
        return

    new_student = Classmate(name, section, subject)
    students.append(new_student)

    display(new_student.introduce(), target="output")


# ================= ATTENDANCE =================

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']


def plot_graph(data):
    plt.clf()
    plt.plot(days, data)
    plt.title("Weekly Attendance"from pyscript import display, document
import matplotlib.pyplot as plt
import logging

logging.getLogger('matplotlib').setLevel(logging.WARNING)

# ================= CLASSMATES =================

class Classmate:
    def __init__(self, name, section, favourite_subject):
        self.name = name
        self.section = section
        self.favourite_subject = favourite_subject

    def introduce(self):
        return f"Hello! I am {self.name} from {self.section}. My favorite subject is {self.favourite_subject}."


students = [
    Classmate('Joaquin Oliveros', 'Ruby', 'Science'),
    Classmate('Bryce Ong', 'Ruby', 'Math'),
    Classmate('Zakari Dimaculangan', 'Ruby', 'Social Studies'),
    Classmate('Dweyen Evangelista', 'Ruby', 'PE'),
    Classmate('Kobe Baylon', 'Ruby', 'Science')
]


def show_list(e):
    document.getElementById("output").innerHTML = ""
    for s in students:
        display(s.introduce(), target="output")


def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name == "":
        return

    new_student = Classmate(name, section, subject)
    students.append(new_student)

    display(new_student.introduce(), target="output")


# ================= ATTENDANCE =================

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']


def plot_graph(data):
    plt.clf()
    plt.plot(days, data)
    plt.title("Weekly Attendance")
    plt.xlabel("Days")
    plt.ylabel("Absences")
    display(plt, target="output2")


def displaying_output(e):
    selected_day = document.getElementById("input1").value
    absence_value = document.getElementById("input2").value

    if absence_value.isdigit():
        absence_value = int(absence_value)
    else:
        absence_value = 0

    day_index_map = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4
    }

    values = [0, 0, 0, 0, 0]
    values[day_index_map.get(selected_day, 0)] = absence_value

    plot_graph(values)
    plt.xlabel("Days")
    plt.ylabel("Absences")
    display(plt, target="output2")


def displaying_output(e):
    values = [
        0,
        int(document.getElementById("input2").value) if document.getElementById("input2").value.isdigit() else 0,
        0, 0, 0
    ]

    plot_graph(values)
