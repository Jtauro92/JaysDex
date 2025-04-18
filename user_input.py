


from sysconfig import get_path_names


def input_decorator(func, prompt:str = "Enter Name"):
    def wrapper():
        func(prompt)
            
    return wrapper
       
@input_decorator()
def get_name(prompt) -> str:
    name = input(prompt)
    return name
       

if __name__ == '__main__':
    name = get_name()
    print(name)