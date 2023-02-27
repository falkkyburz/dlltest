from ctypes import *

my = CDLL("mydll.dll")

# Create function argument and return types
class STRUCT_DLL(Structure):
    _fields_ = [("count_int", c_int), 
                ("ints", POINTER(c_int))]

my.func_dll.argtypes = [c_int, c_char_p, STRUCT_DLL]
my.func_dll.restype = c_int

# Prepare struct and parameters
my_int = 42
my_str = create_string_buffer(b"Test", 64)
my_struct_dll = STRUCT_DLL()
my_struct_dll.count_int = 3
my_struct_dll.ints = (c_int * 3)(1, 2, 3)

# Call function
print(my.func_dll(21, create_string_buffer(b"Test", 64), my_struct_dll))

print(my.func_dll(my_int, my_str, my_struct_dll))
