# write a program to fill in letter tampalte  given below with name and  that name and date 
# ''' leeter = dear <|name|>
#  your are sellceted
#  <||date|>'''

letter ='''dear <|name|>
 your are sellceted
 <||date|>'''
print(letter.replace("<|name|>" , "sameer").replace("<|date|>" , "2/22/2050"))
 
