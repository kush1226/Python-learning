"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 09.3 - course info
Date: 03/30/2025

Description:
    In this program, we create a nested dictionary with course details. Allow user input to fetch instructor, room, and time. Display info or show an error if the course number is invalid.
Contributors:    
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""

def get_course_data():
    # Creates and returns a nested dictionary with course information.
    course_dict = {
        "CS101": {"room": '1461', "instructor": "Django", "time": "9:00 a.m."},
        "CS102": {"room": '4815', "instructor": "Idle", "time": "11:00 a.m."},
        "AB203": {"room": '3634', "instructor": "Rich", "time": "10:00 a.m."},
        "NT110": {"room": '1188', "instructor": "Marshal", "time": "2:00 p.m."},
        "CM241": {"room": '2451', "instructor": "Pickle", "time": "12:00 p.m."}
    }
    return course_dict


def main():

    courses = get_course_data()
    course_number = str(input("Enter a course number: "))
    
    if course_number in courses:
        course_info = courses[course_number]  # Get course information from course number
        print(f"  The details for course {course_number} are:")   # Get course number
        print(f"    Instructor: {course_info['instructor']}")# Get course instructor
        print(f"          Room: {course_info['room']}") # Get course room
        print(f"          Time: {course_info['time']}")   # Get course time
    else:
        print(f"  {course_number} is an invalid course number.")

        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
