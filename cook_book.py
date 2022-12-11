with open ('ingridients.txt', encoding='utf-8') as file:
    cook_book={}
    for line in file:
        dish_name=line.strip()
        ingr_count=int(file.readline().strip())
        ingridients=[]
        for i in range(ingr_count):
            ingridient=file.readline().strip()
            prod, count, ed=ingridient.split(' | ')
            ingridients.append({
                'ingridient_name':prod,
                'quantity': count,
                'measure':ed
            })
        
        file.readline()
        cook_book[dish_name]=ingridients
    print(cook_book) 
    

        

