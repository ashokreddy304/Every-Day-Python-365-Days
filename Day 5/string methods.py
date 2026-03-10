# s = 'Embeddings convert text into numerical vectors so machines can understand semantic meaning.'

# print(s)
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# #count
# s  = 'abcabcde'
# print(s.count('a'))

# #replace
# print(s.replace('a','z'))

s = 'Embeddings convert text into numerical vectors so machines can understand semantic meaning.'
# print(s.startswith('E')) #True
# print(s.startswith('Embeddings')) #True
# print(s.startswith('b')) #False

# print(s.endswith('m')) #False
# print(s.endswith('meaning.')) #True
# print(s.endswith('.')) #False

s = 'Embeddings convert text into numerical vectors so machines can understand semantic meaning.'
# print(s.index('so'))
# #print(s.index('bus'))

# print(s.find('can'))
# print(s.find('hello')) 

s = 'Embeddings,convert text into numerical vectors so machines can understand semantic meaning.'
s = s.replace('.',',')
s1 = s.split(' ')
print(s1)
print(" ".join(s1))