from operator import truediv


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        return False
    user_in_group = None
    users = group.get_users()
    if users is None:
        user_in_group = find_user(user, group.get_groups())
    if user in users:
        user_in_group = True
    else:
        user_in_group = find_user(user, group.get_groups())
    return user_in_group == True


def find_user(user, groups):
    for group in groups:
        users = group.get_users()
        if user in users:
            return True
        else:
            return find_user(user, group.get_groups())
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

def test_function(test_case):
    output = is_user_in_group(test_case[0],parent)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

## Test Case 1
test_case_1 = ["sub_child_user",True]
test_function(test_case_1)
## Test Case 2
test_case_1 = ["no_child",False]
test_function(test_case_1)
## Test Case 3
parent = None
test_case_1 = ["no_child",False]
test_function(test_case_1)


