":~Input a file ~:"
"\nFile does not exist."

"\n{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}"
"{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}"
"{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}"

#user_input=input(":~Input a file ~:")


lines = []

while True:
    user_input = input(":~Input a file ~:")
    try:
        fp = open(user_input, 'r')  #opens file
        for line in fp:
            lines.append(line.strip())   #transfers data from list to lines[]
        fp.close()                       #closes list here
        break
    except FileNotFoundError:       #will loop until error isnt hit
        print("\nFile does not exist.")





students = []

for line in lines:
    name = line[:20].strip()             # first 20 characters = name
    grades = line[20:].split()      # other text gets split into strings
    scores = []

    for s in grades:      #scores are saved as int inside scores[]
        scores.append(int(s))

    average = sum(scores) / 4
    student_tuple = (name, scores[0], scores[1], scores[2], scores[3], average)
    students.append(student_tuple)    #converts ewch line into a tuple
                                    #and then adds each tuple back into students[]


print("\n{:<20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))

students.sort()


for student in students:
    print("{:<20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(student[0], student[1], student[2], student[3], student[4], student[5]))




num_students = 5
exam_totals = [0, 0, 0, 0]

for student in students:
    for i in range(4):
        exam_totals[i] += student[i + 1]  # sum of each exam score

exam_averages = [total / num_students for total in exam_totals]

print("{:<20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean", *exam_averages))







