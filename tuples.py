def display_courses(course_tuple):
    print("\nProgramming Courses:")
    for index, course in enumerate(course_tuple, 1):
        print(f"{index}. {course}")

def calculate_course_stats(course_tuple):
    total = len(course_tuple)
    shortest = min(course_tuple, key=len)
    longest = max(course_tuple, key=len)
    return total, shortest, longest

def main():
    # courses
    programming_classes = (
        'Intro to Python',
        'Advanced Python',
        'Database Essentials',
        'Web Development Basics',
        'Data Structures in Python',
        'Web Design Fundamentals'
    )
    
    display_courses(programming_classes)

    # statistics
    total, shortest, longest = calculate_course_stats(programming_classes)
    print(f"\nTotal classes offered: {total}")
    print(f"Shortest course name: {shortest}")
    print(f"Longest course name: {longest}")
    
    # tuple features
    print("\nAdditional Tuple Operations:")
    print(f"First course: {programming_classes[0]}")
    print(f"Last course: {programming_classes[-1]}")
    print(f"Middle courses: {programming_classes[2:4]}")
    
    # immutability
    try:
        programming_classes[0] = "New Course"
    except TypeError as error:
        print("\nTuple Immutability Demonstration:")
        print(f"Cannot modify tuple: {error}")

if __name__ == "__main__":
    main()