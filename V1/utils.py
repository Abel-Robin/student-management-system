def is_valid_age(age):
    return age.isdigit() and 1 <= int(age) <= 100


def is_valid_id(student_id):
    return student_id.isdigit()
