def unordered_pairs(my_list):
    
    new_list= []
    index=0
    count = 1
    for num in my_list:
        
        while index < len(my_list):
            tupl= (num,my_list[index])
            new_list.append(tupl)
            index +=1
        index = 0
        index += count
        count += 1
    return new_list

unordered_pairs([1,5,9])