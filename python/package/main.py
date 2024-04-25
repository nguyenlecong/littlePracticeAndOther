from pkg.module import add  # Cannot import 'add' function if not have '__init__.py' file
from pkg.module import *  # Only export add function due to '__all__' variable in 'module.py' file
from pkg.module import sub  # But can import like this

print(add(1, 2))
print(sub(1, 2))
