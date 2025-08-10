def test(word,letter):
    my_list = []
    for i in word:
        my_list.append(i)
    for index, j in enumerate(my_list):
        if j == letter:              
            print(f'{my_list[index]} - {index}') 
             
test('lubricant','i')              
