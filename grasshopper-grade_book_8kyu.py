def get_grade(s1, s2, s3):
    media = int((s1 + s2 + s3) / 3)
    grade = ''
    
    if media in range(90, 101):
        grade = 'A'
    elif media in range(80, 90):
        grade = 'B'
    elif media in range(70, 80):
        grade = 'C'
    elif media in range(60, 70):
        grade = 'D'
    else: # media in range(0, 60):
        grade = 'F'
      
    return grade
