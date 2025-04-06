def name_mark_age (which):
    while True:
            return float(input(f'Enter the {which} of a student'))
mark1 = name_mark_age("english mark")
mark2 = name_mark_age("maths mark")
mark3 = name_mark_age("chemistry mark")
mark4 = name_mark_age("physics mark")
mark5 = name_mark_age("biology mark")
marks = [mark1, mark2, mark3, mark4, mark5]

markav = sum(marks) / len(marks)
def markaverage (which):
    while True:
        return print(f'{which}')
if markav > 4.5:
    av = markaverage("A")
elif markav > 3.5:
    av = markaverage("B")
elif markav > 2.5:
    av = markaverage("C")
elif markav > 2.0:
    av = markaverage("D")
elif markav < 2.0:
    av = markaverage("F")    