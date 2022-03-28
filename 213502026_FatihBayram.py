import string


def word_meter(text):
    try:
        empty=[]
        newtext=""
        for i in text:
            if i not in string.punctuation:
                newtext += i

        t1=newtext.split()
        t2=list(t1)
        for x in t2:
            empty.append(len(x))
            empty.sort(reverse=True)
        print(f"'{max(t2, key=len)}'",empty[0])    
    except UnboundLocalError:
        print("-"*40)
        print("Lütfen geçerli bir değer giriniz .")    
        print("-"*40)
    except ValueError:
        print("-"*40)
        print("Lütfen geçerli bir değer giriniz .")    
        print("-"*40)



word_meter("Buyrun Hocam :)")        




