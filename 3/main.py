students = ['Brenda Lewis Rivera', 'Julia Stewart Turner', 'Uma Robinson Davidson', 'Mia Garcia Parker',
            'Zach White Hughes', 'Rachel Scott Clark', 'Xavier Jackson Murray', 'Vincent Jackson Gonzalez',
            'Dave Edwards Rodriguez', 'Cathy Brown Young', 'Nina Murray Hughes', 'Una Johnson Moore',
            'Rachel Foster Martinez', 'Fred Cooper Wilson', 'Molly Edwards Sanchez', 'Frank Hughes Anderson',
            'Fred Miller Turner', 'Vincent Wright Adams', 'Nathan Mitchell Baker', 'George Robinson Sanchez',
            'Oscar Miller Cooper', 'Kevin Allen Lewis', 'Kate Perez Adams', 'Uma Foster Lopez',
            'Ellie Baker Hernandez', 'Zoe Murray Jackson', 'Sarah Murray Rivera', 'Peter Gonzalez Lewis',
            'Quinn King Foster', 'Charlie Garcia Bryant', 'Cathy Baker Clark', 'Olivia Clark Martinez',
            'Quentin Hill Taylor', 'Grace King Perez', 'Charlie Carter Anderson', 'Samantha Sanchez Collins',
            'Una Hill Robinson', 'Trevor King Parker', 'Ivy Rivera Collins', 'Kate Brown Butler',
            'Linda Sanchez Brownstone', 'Molly Anderson Hill', 'Cathy Gonzalez Rivera', 'Isaac Wright Green',
            'Ellie Rivera Turner', 'Derek Taylor Lopez', 'Frank Williams Reed', 'Henry Baker Brown',
            'Adam Foster Ward', 'Molly Green Green']

option = input(f"Choose option: \n1. Fill by user \n2. Fill by default \n")

if option == '1':
    students = []
    while True:
        text = input(f"Enter new student name (to end write 'end'): ")
        if text == 'end':
            break
        else:
            students.append(text)

for index, student in enumerate(students):
    print("Ask theory for", student, f"({index + 1})")
    print("Pass part of questions for", students[index], f"({index + 2})")

print("\n\n\n\n\n\n")

for index, student in enumerate(students):
    print("Practice task for", student, f"({index + 1})")
    print("Pass part of practice tasks for", students[index], f"({index + 2})")
