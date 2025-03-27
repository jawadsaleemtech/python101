def new_decorator(orig_func):

    def wrap_func():
        print("some extra code, Before")

        orig_func()

        print("some extra code, After")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("i want decorated")
    

func_needs_decorator()