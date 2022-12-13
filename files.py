

files={}
with open('text/t1.txt', 'rt', encoding='utf-8') as f1, open('text/t2.txt', encoding='utf-8') as f2, open('text/t3.txt', encoding='utf-8') as f3:
    files['t1.txt']=f1.readlines()
    files['t2.txt']=f2.readlines()
    files['t3.txt']=f3.readlines()

d1 = (sorted(files.items(), key=lambda item: len(item[1])))

with open('text.txt', 'w', encoding='utf-8') as f:
    
    for el in d1:
        f.write('\n')
        f.write(str(el[0]))
        f.write('\n')
        f.write(str(len(el[1])))
        f.write('\n')
        f.write(str(el[1]))
       
        

    
