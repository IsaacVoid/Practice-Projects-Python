# List practice
# Comma code
spam = ['apples', 'bannanas', 'tofu', 'lemmons', 'grapes', 'pinaple']
text = ''

if not spam:
    print(f'lista vacia')
else: 
    for i in range(len(spam) -1):
        text = text + spam[i] + ', '
    text = text + 'and ' + spam[(len(spam) -1)]
    print(text)