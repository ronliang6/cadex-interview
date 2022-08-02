class Student:
    """A student."""

    def __init__(self, average_grade):
        self.average_grade = average_grade
        self.name = "stu_name" + str(self.average_grade)
        self.other_details = "other_details"


class BinaryTreeNode:
    """A binary_tree_node in a binary tree."""

    def __init__(self, student: Student, left_node=None, right_node=None):
        self.student = student
        self.left_node = left_node
        self.right_node = right_node


class StudentBinarySearchTree:
    def __init__(self, student_list):
        """
        Init a StudentBinaryTree.

        :param student_list: a list of students. Students cannot have the same grade.
        """
        # assert students dont have duplicate grades, incompatible with BST
        # sort list to convert to BST
        self.student_list = sorted(student_list, key=lambda stu: stu.average_grade)
        self.root_node = self.initialize_tree(self.student_list)

    def initialize_tree(self, student_list):
        if len(student_list) == 0:
            return None
        student_list_left_node = self.initialize_tree(student_list[0: max((len(student_list) - 1) // 2, 0)])
        student_list_right_node = self.initialize_tree(student_list[(len(student_list) - 1) // 2 + 1:])
        return BinaryTreeNode(student_list[(len(student_list) - 1) // 2],
                              student_list_left_node, student_list_right_node)

    @staticmethod
    def print_tree(binary_tree_node, depth=0):
        if binary_tree_node.left_node:
            StudentBinarySearchTree.print_tree(binary_tree_node.left_node, depth + 1)
        print('    ' * depth + str(binary_tree_node.student.average_grade) + '<')
        if binary_tree_node.right_node:
            StudentBinarySearchTree.print_tree(binary_tree_node.right_node, depth + 1)

    def print_self(self):
        studentBinarySearchTree.print_tree(self.root_node)


if __name__ == "__main__":
    students = []
    for i in range(30):
        students.append(Student(i))
    studentBinarySearchTree = StudentBinarySearchTree(students)
    studentBinarySearchTree.print_self()
