#COMMENT HELLO
import json

def process_user_query(h):
    retrn = ''
    code =  h.split("**")
    if len(code) == 1:
        return h
    for i in range(0,len(code)-1,2):
        text = code[i].split("*"+code[i+1]+"*")[1]
        retrn+=STH(text, code[i+1])
    return retrn

def test(h):
    complete = ''
    code = h.split("*")
    for i,c in enumerate(code):
        if i !=len(code)-1:
            if c.strip(" ") == "":
                continue
        else:
            c = c.strip()
            key = c[0]
            print(c.strip() , end="\n")

    return complete

##### SCRIPT TO HTML
def STH(C , k):
    if k == 'b':
        return "<b>"+C+"</b>"
    if k == 'i':
        return "<i>"+C+"</i>"
    if k == 'u':
        return "<u>"+C+"</u>"
    if k == 'c':
        return "</br><code style='background-color:#eff0f1;color:black;'>"+C+"</code>"
    if k == 'l':
        return "<p style='text-align: left;'>"+C+"</p>"
    if k == 'e':
        return "<p style='text-align: center;'>"+C+"</p>"
    if k == 'r':
        return "<p style='text-align: right;'>"+C+"</p>"
    if k == 'd':
        return "<img style='width:600px' src='"+C+"'></img>"

#print(test("*d your_d_text *e your_e_text e*     d*   *e your_e_here *e"))
