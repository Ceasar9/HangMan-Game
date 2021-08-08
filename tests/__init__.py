import sys
from os.path import dirname, abspath, join, sep
package = dirname(dirname(abspath(__file__)))
# print(mopy.split(sep)[-1].lower(), "***")
# assert package.split(sep)[-1].lower() == '1_print_debug_strmanipulation'
sys.path.append(package)
print('package folder appended to path: ', package)