def output_data_main(args):
    

    if len(args) == 0:
        print('Совпадений не найдено')
    if len(args) > 0:
        
        choice = input('Выбирите формат вывода информации: 1. В одну строку, 2. В несколько строк >>> ')
       
        while choice not in '12':
            print('Вы ввели некорректное значение!')
            choice = input('Выбирите формат вывода информации: 1. В одну строку, 2. В несколько строк >>> ')

        if choice == '1':
            for word in args:
                print(" ".join(word))
        if choice == '2':
            for word in args:
                print("\n".join(word))
                print()


    
   
     
    


    
    

