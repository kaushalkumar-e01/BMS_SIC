'''
read size of the list from the user, say N
read N number of elements of the list
read the search elements from the user
ask the function sequentially_search() to do the job!
else -1
'''
def sequentially_search(search_element, elements):
    for i in range(len(elements)):
        if elements[i]==search_element:
            return i
    return -1

input_size = int (input('enter size of the list: '))
elements =[]
print(f'enter the {input_size} elements of the list')
for i in range(input_size):
    element = float(input(f'element{i+1}: '))
    elements.append(element)

print('user given elements are are \n', elements)
search_element = float(input("enter the element to be searched: "))

search_index = sequentially_search(search_element, elements)

if search_index == -1:
    print(f'the search element {search_element} is not found')
else:
    print(f'search element {search_element} is found at position {search_index+1}')