import os
import sys

os.chdir(os.path.dirname(__file__))
print(sys.platform)
print(os.getcwd())


def dir_operation(action):
    for i in range(1, 10):
        name = 'dir_{}'.format(i)
        new_path = os.path.join(os.getcwd(), name)
        action(new_path)

# dir_operation(os.rmdir)
