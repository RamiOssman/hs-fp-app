#COMMENT HELLO
import json

def process_user_query(h):
    if "*" not in h:
        return h
    t = ''
    cut1 = h[h.index("*")+1:len(h)]
    key  = cut1[0]
    cut2 = cut1[1:cut1.index(key+"*")]
    t+= STH(cut2 , key)
    h = h.replace("*"+key+cut2+key+"*" , "")
    return t+decode(h , 1)


def test(h):
    return h.index("your")

def decode(h, x):
    if "*" not in h:
        return h
    t = ''
    cut1 = h[h.index("*")+1:len(h)]
    key  = cut1[0]
    cut2 = cut1[1:cut1.index(key+"*")]
    t+= STH(cut2 , key)
    h = h.replace("*"+key+cut2+key+"*" , "")
    if x == 1:
        return t+decode(h , 1)
    if x == 2:
        return decode(h , 1)+t

#### SCRIPT TO HTML
def STH(C , k):
    C = decode(C , 2)
    att = ''
    while "@" in C:
        type = C[C.index("@")+1]
        if type == 's':
            att+='font-size:'+C[C.index("@")+3:C.index("@")+5]+'px;'
            C = C.replace(C[C.index("@"):C.index("@")+5] , '')
        if type == 'c':
            att+='color:#'+C[C.index("@")+3:C.index("@")+9]+';'
            C = C.replace(C[C.index("@"):C.index("@")+9] , '')
        if "@" not in C:
            att = " style='"+att+"' "
    if k == 'b':
        return "<b "+ att+" >"+C+"</b>"
    if k == 'i':
        return "<i "+ att+" >"+C+"</i>"
    if k == 'u':
        return "<u "+ att+" >"+C+"</u>"
    if k == 'c':
        return "</br><code  "+ att+" style='background-color:#eff0f1;'>"+C+"</code>"
    if k == 'l':
        return "<p  "+ att+" style='text-align: left;'>"+C+"</p>"
    if k == 'e':
        return "<p  "+ att+" style='text-align: center;'>"+C+"</p>"
    if k == 'r':
        return "<p "+ att+"  style='text-align: right;'>"+C+"</p>"
    if k == 'd':
        return "<img "+ att+"  style='width:600px' src='"+C+"'></img>"

text = "*b @s:13 @c:RRGGBB something else *i italic i* b* *b here b*"
print(process_user_query(text))
