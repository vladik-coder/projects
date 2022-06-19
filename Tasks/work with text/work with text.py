def sep(text_1, max_len):
    text_2 = ''  
    count = 0  
    for i in text_1.split():  
        count += len(i)  
        if count > (int(max_len)-1):  
            text_2 += '\n'  
            count = len(i)  
        elif text_2 != '':  
            text_2 += " "  
            count += 1  
        text_2 += i  
    return text_2 

def add_spaces(str_1, max_len_1, numb_spaces_1):
    numb_replace = max_len_1 - len(str_1)
    str_add_spaces = str_1.replace(numb_spaces_1 * " ", ((numb_spaces_1 + 1) * " "), numb_replace)
    return str_add_spaces

def equalize(text_2):
    text_3=[] 
    for line_2 in text_2.split('\n'): 
        count_space=line_2.count(" ")
        if count_space==0 and len(line_2)!=max_len:
            line_2+=" "
            count_space+=1 
        if len(line_2)<max_len:
            numb_spaces=round((max_len-len(line_2))//count_space)+1 
            if numb_spaces>1:
               str_spaces=line_2.replace(" ",(numb_spaces*" ")) 
               if len(str_spaces)<max_len:
                  str_spaces=add_spaces(str_spaces,max_len,numb_spaces) 
            else:
               str_spaces=line_2 
               if len(str_spaces)<max_len:
                  str_spaces=add_spaces(str_spaces,max_len, numb_spaces) 
        else:
           str_spaces=line_2
        text_3.append(str_spaces) 
    final_txt = '\n'.join(text_3)
    return final_txt


file=open('text.txt','r',encoding='utf-8') 
text_1=file.read()
file.close()
max_len=int(input('Enter the maximum number of characters per line, more than 35  '))
while max_len<=35: 
   max_len=int(input('Enter the maximum number of characters per line, more than 35  '))   


final_txt=equalize(sep(text_1, max_len))
print(final_txt)
print("Text formatted")
f= open ('final_text.txt', 'w', encoding='utf-8')
f.write(final_txt) 
f.close() 