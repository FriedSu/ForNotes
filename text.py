# stop = int(input())
# result = 0
# for a in range(2):
#     print(a, end=': ')
#     for b in range(4):
#         result += a + b
#         if result > stop:
#             print('-', end=' ')
#             continue
#         print(result, end=' ')
#     print()

# import string library function 

# from string import punctuation

# # An input string.
# Sentence = ['A#@!', 'Dog', 'yu!']
  
# for i in Sentence:
      
#     # checking whether the char is punctuation.
#     if i in punctuation:
          
#         # Printing the punctuation values 
#         print(i)
# print('done')

male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }

# Use set methods to create sets all_names, neutral_names, and specific_names.

# male_names_set = set(male_names)
# female_names_set = set(female_names)
# all_names = set()
# neutral_names = set()
# specific_names = set()


# monsters = {'Gorgon', 'Medusa'}
# trolls = {'William', 'Bert', 'Tom'}
# horde = {'Gorgon', 'Bert', 'Tom'}

# all_monsters = set()
# x = set()
# x = all_monsters.update(monsters, trolls)

# print(x)

# --------------------------------------------

# "New" means new compared to previous level
provincial_capitals = {
    'Alberta': 'Edmonton',
    'Manitoba': 'Winnipeg',
    'Yukon': 'Whitehorse',
    'BC': 'Victoria'
}

province_name = input()
while province_name != 'exit':
    if province_name in provincial_capitals:
        print(provincial_capitals[province_name])
        del provincial_capitals[province_name] # New line
    else:
        print('x')
    province_name = input()