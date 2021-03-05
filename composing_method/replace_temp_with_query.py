
def send(self, students):
    print("Students' contact info were sent to", self.name + ".")


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    def __init__(self, students) -> None:
        self.students = students

    def print_student(self, passed_students):

        print("*** Student who graduated *** ")
        for s in passed_students:
            print(s.name)

        print("****************************")

        # Send congrat emails to them.
        for s in passed_students:
            s.send_congrat_email()

    def find_top_10(self):
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [
            Employer("Microsoft"),
            Employer("Free Software Foundation"),
            Employer("Google"),
        ]
        for e in top_employers:
            e.send(top_10_percent)

    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        min_gpa = 2.5  # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)

        # print student's name who graduated.
        print_student(self, passed_students)

        # Find the top 10% of them and send their contact to the top employers


students = [
    Student(2.1, "Pinocchio"),
    Student(2.3, "goku"),
    Student(2.7, "toro"),
    Student(3.9, "naruto"),
    Student(3.2, "kami"),