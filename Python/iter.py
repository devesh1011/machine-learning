import pickle as pk 

student_names = ['Alice','Bob','Elena','Jane','Kyle']

# with open('student.pkl', 'wb') as f:
#     pk.dump(student_names, f)
    
with open('student.pkl', 'rb') as f:

    student_names_loaded = pk.load(f) # deserialize using load()
    print(type(student_names_loaded))
    print(student_names_loaded) # print student names