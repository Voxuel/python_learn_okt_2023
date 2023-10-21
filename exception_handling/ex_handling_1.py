# Try/catch/except

inp = ''
valid = False
log = []
while(valid != True):
    try:
        inp = int(input('Enter a nubmber'))
        print(inp)
    except ValueError as err:
        print('are you daft?')
        log.append(err)
    else:
        print('good job')
        break
        


print(log)


# Handle multiple type errors
"""
def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'something went wrong, see: {err}')

print(sum(1,'e'))

print(sum(1,0))

"""