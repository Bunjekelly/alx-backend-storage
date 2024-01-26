#!/ur/bin/env python3

"""a Python function that returns all students sorted by average score"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """function definition"""
    students = mongo_collection.find()
    student_averages = []
    for student in students:
        if 'scores' in student:
            average_score = sum(student['scores']) / len(student['scores'])
            student['averageScore'] = average_score
            student_averages.append(student)
    student_averages.sort(key=lambda x: x['averageScore'], reverse=True)
    return student_averages
