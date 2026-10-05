import numpy as np
student_ages=np.array([15, 16, 17, 18, 19])
ages_in_2_years=student_ages+2
print(ages_in_2_years) #student ages in 2years  time.  
student_ages=np.append(student_ages,22)
print(student_ages)
student_ages=np.insert(student_ages,1,26)
print(student_ages)
student_ages=np.delete(student_ages,0)
print(student_ages)
student_ages=np.sort(student_ages)
print(student_ages)
student_ages[2]=30
print(student_ages)