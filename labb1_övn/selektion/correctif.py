# Är det någon skillnad i hur de båda if-satserna nedan fungerar?
# Vad är det i så fall för skillnad mellan dem?
# För vilka värden på n ger de olika utskrifter?

# if n < 0:
#     print('Negative')
# elif n < 1000:
#     print('Small')
# elif n > 1000:
#     print('Large')
# else:
#     print('Medium')


# if n > 1000:
#     print('Large')
# elif n < 1000:
#     print('Small')
# elif n < 0:
#     print('Negative')
# else:
#     print('Medium')

# 1. ja, men resultat är den samma, 2. skillnaden är
# att de förhållandet av n med ett annat värde olika 
# 3. negativa tal == Negative tal mellan 0 o 1000 == Small 
# tal större än 1000 == large 
# andra tal == Medium 
# 