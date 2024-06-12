user_input = input("Enter a Python expression to evaluate: ")
try:
    result = eval(user_input)
    print(f"Result:\n{result}")
except Exception as e:
    print(f"Error:\n{e}")
