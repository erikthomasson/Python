# f = open('text.py')
# print(f.read())
# print(f.readline(2, 3)) # tar ett argument
# print(f.readline(2 and 3 and 4))

# for x in f:
#     #print(x)            #ANVÄND 'line' istället för 'x'.
    
#     #if 'hej' in x :
#     #    print(x)
#     #if x.startswith(''):
#     #   print(x)
#     print(x.rstrip())

# print("hej \npå \n dig")
# f.seek(0)       # börjar från 0de karaktären
# filetext = f.read(25)       #till 25 karaktärem
# print(filetext)





# f.close()
def sequence_filter(line):
    return 'n' not in line      #filter

with open('text.py') as text:       #istället för '''f = open(text.py)''' och '''f.close()''' filen är tillgänglig när vi är lokalt
    lines = text.readlines() 
    print(list(filter(sequence_filter, lines)))         #filtrerar bort alla lines som börjar på n