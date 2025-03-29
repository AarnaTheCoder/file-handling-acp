
def manage_student_info(file_name, student_name, favorite_subject):
    try:
        
        with open(file_name, 'a') as file:
            file.write(f"{student_name}: {favorite_subject}\n")
        print(f"Added/Updated: {student_name} - {favorite_subject}")
    except Exception as e:
        print(f"Error: {e}")


file_name = "student_records.txt"
student_name = "Roy"
favorite_subject = "Science"

manage_student_info(file_name, student_name, favorite_subject)