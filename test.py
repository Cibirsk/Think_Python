def do_twice(f,str):
    f(str)
    f(str)

def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(f,str):
    do_twice(f,str)
    do_twice(f,str)

do_four(print_twice, 'test1')

#do_twice(print_twice, "spam")