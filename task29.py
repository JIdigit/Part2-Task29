def function():
    text=input()
    final=[]
    fnl=""
    text_list=list(text)
    signs=[',','.','!','?',':',';','-']
    i=0
    j=0
    for word in text:
        if word  in signs:
            final.append(' ')
        else:
            final.append(word)

    final=fnl.join(final)
        
    return final
print(function())