#################################import part################################
############################################################################

from tkinter import Tk,Label,Button,Entry ,StringVar , PhotoImage ,Menubutton,Menu

#################################window part################################
############################################################################

calculator = Tk()
calculator.geometry("320x450+500+130")
calculator.resizable(False, False)
calculator.maxsize(320, 450)
calculator.minsize(320, 450)
calculator.iconbitmap('data\\photos\\icon.ico')
calculator.title("calculator")
calculator.state("normal")

###############################some variables###############################
############################################################################

runing = ''
total = StringVar()
total.set("")
ans = StringVar()
num1 = ''
num2 = ''
ANS = 0

##################################style 1###################################
############################################################################

st1_num0            = PhotoImage(file='data\\photos\\style1\\0.png')
st1_num1            = PhotoImage(file='data\\photos\\style1\\1.png')
st1_num2            = PhotoImage(file='data\\photos\\style1\\2.png')
st1_num3            = PhotoImage(file='data\\photos\\style1\\3.png')
st1_num4            = PhotoImage(file='data\\photos\\style1\\4.png')
st1_num5            = PhotoImage(file='data\\photos\\style1\\5.png')
st1_num6            = PhotoImage(file='data\\photos\\style1\\6.png')
st1_num7            = PhotoImage(file='data\\photos\\style1\\7.png')
st1_num8            = PhotoImage(file='data\\photos\\style1\\8.png')
st1_num9            = PhotoImage(file='data\\photos\\style1\\9.png')
st1_backgrond      = PhotoImage(file='data\\photos\\style1\\bg.png')
st1_del           = PhotoImage(file='data\\photos\\style1\\del.png')
st1_dot           = PhotoImage(file='data\\photos\\style1\\dot.png')
st1_ans           = PhotoImage(file='data\\photos\\style1\\ans.png')
st1_plus         = PhotoImage(file='data\\photos\\style1\\plus.png')
st1_menu_image   = PhotoImage(file='data\\photos\\style1\\menu.png')
st1_clear       = PhotoImage(file='data\\photos\\style1\\clear.png')
st1_Equal       = PhotoImage(file='data\\photos\\style1\\Equal.png')
st1_minus       = PhotoImage(file='data\\photos\\style1\\minus.png')
st1_ac_menu   = PhotoImage(file='data\\photos\\style1\\ac_menu.png')
st1_Dividing = PhotoImage(file='data\\photos\\style1\\Dividing.png')
st1_Multiply = PhotoImage(file='data\\photos\\style1\\Multiply.png')

##################################style 2###################################
############################################################################

st2_num0            = PhotoImage(file='data\\photos\\style2\\0.png')
st2_num1            = PhotoImage(file='data\\photos\\style2\\1.png')
st2_num2            = PhotoImage(file='data\\photos\\style2\\2.png')
st2_num3            = PhotoImage(file='data\\photos\\style2\\3.png')
st2_num4            = PhotoImage(file='data\\photos\\style2\\4.png')
st2_num5            = PhotoImage(file='data\\photos\\style2\\5.png')
st2_num6            = PhotoImage(file='data\\photos\\style2\\6.png')
st2_num7            = PhotoImage(file='data\\photos\\style2\\7.png')
st2_num8            = PhotoImage(file='data\\photos\\style2\\8.png')
st2_num9            = PhotoImage(file='data\\photos\\style2\\9.png')
st2_backgrond      = PhotoImage(file='data\\photos\\style2\\bg.png')
st2_del           = PhotoImage(file='data\\photos\\style2\\del.png')
st2_dot           = PhotoImage(file='data\\photos\\style2\\dot.png')
st2_ans           = PhotoImage(file='data\\photos\\style2\\ans.png')
st2_plus         = PhotoImage(file='data\\photos\\style2\\plus.png')
st2_menu_image   = PhotoImage(file='data\\photos\\style2\\menu.png')
st2_clear       = PhotoImage(file='data\\photos\\style2\\clear.png')
st2_Equal       = PhotoImage(file='data\\photos\\style2\\Equal.png')
st2_minus       = PhotoImage(file='data\\photos\\style2\\minus.png')
st2_ac_menu   = PhotoImage(file='data\\photos\\style2\\ac_menu.png')
st2_Dividing = PhotoImage(file='data\\photos\\style2\\Dividing.png')
st2_Multiply = PhotoImage(file='data\\photos\\style2\\Multiply.png')

##################################style 3###################################
############################################################################

st3_num0            = PhotoImage(file='data\\photos\\style3\\0.png')
st3_num1            = PhotoImage(file='data\\photos\\style3\\1.png')
st3_num2            = PhotoImage(file='data\\photos\\style3\\2.png')
st3_num3            = PhotoImage(file='data\\photos\\style3\\3.png')
st3_num4            = PhotoImage(file='data\\photos\\style3\\4.png')
st3_num5            = PhotoImage(file='data\\photos\\style3\\5.png')
st3_num6            = PhotoImage(file='data\\photos\\style3\\6.png')
st3_num7            = PhotoImage(file='data\\photos\\style3\\7.png')
st3_num8            = PhotoImage(file='data\\photos\\style3\\8.png')
st3_num9            = PhotoImage(file='data\\photos\\style3\\9.png')
st3_backgrond      = PhotoImage(file='data\\photos\\style3\\bg.png')
st3_del           = PhotoImage(file='data\\photos\\style3\\del.png')
st3_dot           = PhotoImage(file='data\\photos\\style3\\dot.png')
st3_ans           = PhotoImage(file='data\\photos\\style3\\ans.png')
st3_plus         = PhotoImage(file='data\\photos\\style3\\plus.png')
st3_menu_image   = PhotoImage(file='data\\photos\\style3\\menu.png')
st3_clear       = PhotoImage(file='data\\photos\\style3\\clear.png')
st3_Equal       = PhotoImage(file='data\\photos\\style3\\Equal.png')
st3_minus       = PhotoImage(file='data\\photos\\style3\\minus.png')
st3_ac_menu   = PhotoImage(file='data\\photos\\style3\\ac_menu.png')
st3_Dividing = PhotoImage(file='data\\photos\\style3\\Dividing.png')
st3_Multiply = PhotoImage(file='data\\photos\\style3\\Multiply.png')

###############################window methods###############################
############################################################################

def one ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('1')
    else:
        total.set(t+"1")

def two ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('2')
    else:
        total.set(t+"2")

def three ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('3')
    else:
        total.set(t+"3")

def four ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('4')
    else:
        total.set(t+"4")

def five ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('5')
    else:
        total.set(t+"5")

def six ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('6')
    else:
        total.set(t+"6")

def seven ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('7')
    else:
        total.set(t+"7")

def eight ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('8')
    else:
        total.set(t+"8")

def nine ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('9')
    else:
        total.set(t+"9")

def zero ():
    t = total.get()
    if len(t)==15 :
        pass
    elif len(t) == 1 and t[-1]== '0' :
        total.set('0')
    else:
        total.set(t+"0")

def Multiply ():
    global num1 , num2 ,runing
    t = total.get()
    if len(t)==0 :
        pass
    elif len(t)==15 :
        if num1 == '' :
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = 'm'
        elif num1 != '':
            if runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
            elif runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'm'
            elif runing == 'p':
                num2 = float(t)
                r = num1 + num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'm'
            elif runing == 'd':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                    runing = ''
                    num1, num2 = '', ''
                    total.set("")
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
                    runing = 'm'
    elif len(t) != 15 and len(t) != 0:
        if num1 == '' :
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = 'm'
        elif num1 != '':
            if runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
            elif runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'm'
            elif runing == 'p':
                num2 = float(t)
                r = num1 + num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'm'
            elif runing == 'd':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                    runing = ''
                    num1, num2 = '', ''
                    total.set("")
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
                    runing = 'm'

def Dividing ():
    global num1, num2, runing
    t = total.get()
    if len(t) == 0:
        pass
    elif len(t) == 15:
        if num1 == '':
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = 'd'
        elif num1 != '':
            if  runing == 'd':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
            elif runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'd'
            elif runing == 'p':
                num2 = float(t)
                r = num1 + num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'd'
            elif runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'd'
    elif len(t) != 15 and len(t) != 0:
        if num1 == '':
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = 'd'
        elif num1 != '':
            if runing == 'd':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                    runing = ''
                    num1, num2 = '', ''
                    total.set("")
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
            elif runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'd'
            elif runing == 'p':
                num2 = float(t)
                r = num1 + num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'd'
            elif runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'd'

def plus ():
    global num1, num2, runing
    t = total.get()
    if len(t) == 0:
        pass
    elif len(t) == 15:
        if num1 == '':
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = 'p'
        elif num1 != '':
            if  runing == 'p':
                num2 = float(t)
                r = num1 + num2
                num1 = r
                ans.set(str(r))
                total.set('')
            elif runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'p'
            elif runing == 'd':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                    runing = ''
                    num1, num2 = '', ''
                    total.set("")
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
                    runing = 'p'
            elif runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'p'
    elif len(t) != 15 and len(t) != 0:
        if num1 == '':
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = 'p'
        elif num1 != '':
            if runing == 'p':
                num2 = float(t)
                r = num1 + num2
                num1 = r
                ans.set(str(r))
                total.set('')
            elif runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'p'
            elif runing == 'd':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                    runing = ''
                    num1, num2 = '', ''
                    total.set("")
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
                    runing = 'p'
            elif runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = 'p'

def minus ():
    global num1, num2, runing
    t = total.get()
    if len(t) == 0:
        pass
    elif len(t) == 15:
        if num1 == '':
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = '-'
        elif num1 != '':
            if runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
            elif runing == 'p':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                    runing = ''
                    num1, num2 = '', ''
                    total.set("")
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
                    runing = '-'
            elif runing == 'd':
                num2 = float(t)
                r = num1 / num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = '-'
            elif runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = '-'
    elif len(t) != 15 and len(t) != 0:
        if num1 == '':
            num1 = float(t)
            ans.set(t)
            total.set('')
            runing = '-'
        elif num1 != '':
            if runing == '-':
                num2 = float(t)
                r = num1 - num2
                num1 = r
                ans.set(str(r))
                total.set('')
            elif runing == 'p':
                num2 = float(t)
                r = num1 + num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = '-'
            elif runing == 'd':
                num2 = float(t)
                if num2 == 0.0:
                    ans.set('Math ERROR')
                    runing = ''
                    num1, num2 = '', ''
                    total.set("")
                else:
                    r = num1 / num2
                    num1 = r
                    ans.set(str(r))
                    total.set('')
                    runing = '-'
            elif runing == 'm':
                num2 = float(t)
                r = num1 * num2
                num1 = r
                ans.set(str(r))
                total.set('')
                runing = '-'

def Equal ():
    global ANS , num1, num2, runing
    t = total.get()
    if runing == '' :
        pass
    elif runing == 'p':
        num2 = float(t)
        r = num1 + num2
        if r % 1 != 0 :
            ans.set(str(r))
            total.set('')
            runing = ''
            ANS = ans.get()
            num1=''
        elif r % 1 == 0:
            r = int(r)
            ans.set(str(r))
            total.set('')
            runing = ''
            ANS = ans.get()
            num1 = ''
    elif runing == '-':
        num2 = float(t)
        r = num1 - num2
        if r % 1 != 0 :
            ans.set(str(r))
            total.set('')
            runing = ''
            ANS = ans.get()
            num1=''
        elif r % 1 == 0:
            r = int(r)
            ans.set(str(r))
            total.set('')
            runing = ''
            ANS = ans.get()
            num1 = ''
    elif runing == 'd':
        num2 = float(t)
        if num2 == 0.0:
            ans.set('Math ERROR')
            num1, num2 = '', ''
        else:
            r = num1 / num2
            if r % 1 != 0:
                ans.set(str(r))
                total.set('')
                runing = ''
                ANS = ans.get()
                num1 = ''
            elif r % 1 == 0:
                r = int(r)
                ans.set(str(r))
                total.set('')
                runing = ''
                ANS = ans.get()
                num1 = ''
    elif runing == 'm':
        num2 = float(t)
        r = num1 * num2
        if r % 1 != 0 :
            ans.set(str(r))
            total.set('')
            runing = ''
            ANS = ans.get()
            num1=''
        elif r % 1 == 0:
            r = int(r)
            ans.set(str(r))
            total.set('')
            runing = ''
            ANS = ans.get()
            num1 = ''

def Ans ():
    global ANS
    t = total.get()
    if len(t)==15 :
        pass
    elif ANS ==0:
        pass
    else:
        total.set(t + ANS)

def c ():
    t = total.get()
    if len(t) == 0:
        pass
    elif len(t) == 1:
        e = t[-1]
        t = t.rstrip(e)
        total.set(t)
    elif len(t) == 2:
        if t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+e)
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 3:
        if t[-1]== t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e+e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+e)
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 4:
        if t[-1]== t[-2]==t[-3]==t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e+e+e)
        elif t[-1] == t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+e+e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e )
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 5:
        if t[-1] == t[-2] == t[-3] == t[-4]== t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e + e + e+e)
        elif t[-1]== t[-2]==t[-3]==t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e+e+e)
        elif t[-1] == t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+e+e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e )
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 6:
        if t[-1] == t[-2] == t[-3] == t[-4]== t[-5]== t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e + e + e+e+e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e + e + e+e)
        elif t[-1]== t[-2]==t[-3]==t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e+e+e)
        elif t[-1] == t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+e+e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e )
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 7:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]== t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6*e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]== t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e + e + e+e+e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e + e + e+e)
        elif t[-1]== t[-2]==t[-3]==t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e+e+e)
        elif t[-1] == t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+e+e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e )
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 8:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]== t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6*e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]== t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5*e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4*e)
        elif t[-1]== t[-2]==t[-3]==t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3*e)
        elif t[-1] == t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+2*e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e )
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 9:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 8 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3 * e)
        elif t[-1] == t[-2] == t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 2 * e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e)
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 10:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 9 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 8 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3 * e)
        elif t[-1] == t[-2] == t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 2 * e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e)
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 11:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 10 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 9 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 8 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3 * e)
        elif t[-1] == t[-2] == t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 2 * e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e)
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 12:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11] == t[-12]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 11 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 10 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 9 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 8 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3 * e)
        elif t[-1] == t[-2] == t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 2 * e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e)
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 13:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11] == t[-12] == t[-13]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 12 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11] == t[
            -12]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 11 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 10 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 9 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 8 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3 * e)
        elif t[-1] == t[-2] == t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 2 * e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e)
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 14:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] ==t[-9] == t[-10]\
                == t[-11] == t[-12] == t[-13] == t[-14]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 13 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] ==t[-9] == t[-10] \
                == t[-11] == t[-12] == t[-13]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 12 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11] == t[
            -12]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 11 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11] :
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 10 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 9 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 8 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]== t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6*e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]== t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5*e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4*e)
        elif t[-1]== t[-2]==t[-3]==t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3*e)
        elif t[-1] == t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+2*e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e )
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    elif len(t) == 15:
        if t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] ==t[-9] == t[-10]\
                == t[-11] == t[-12] == t[-13] == t[-14] == t[-15]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 14 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] ==t[-9] == t[-10]\
                == t[-11] == t[-12] == t[-13] == t[-14]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 13 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] ==t[-9] == t[-10] \
                == t[-11] == t[-12] == t[-13]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 12 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11] == t[
            -12]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 11 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10] \
                == t[-11] :
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 10 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9] == t[-10]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 9 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8] == t[-9]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 8 * e)

        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6] == t[-7] == t[-8]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 7 * e)
        elif t[-1] == t[-2] == t[-3] == t[-4] == t[-5] == t[-6]== t[-7]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 6*e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]== t[-6]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 5*e)
        elif t[-1] == t[-2] == t[-3] == t[-4]== t[-5]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 4*e)
        elif t[-1]== t[-2]==t[-3]==t[-4]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + 3*e)
        elif t[-1] == t[-2]==t[-3]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t+2*e)
        elif t[-1] == t[-2]:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t + e )
        else:
            e = t[-1]
            t = t.rstrip(e)
            total.set(t)
    else:
        e = t[-1]
        t = t.rstrip(e)
        total.set(t)

def delete ():
    global num1 , runing
    runing = ''
    num1 = ''
    total.set("")
    ans.set("")

def dot ():
    t = total.get()
    if len(t)>= 14 :
        pass
    elif  '.' in t:
        pass
    else:
        total.set(t + ".")

def about ():
    global info
    info = Tk()
    info.configure(bg='white')
    info.geometry("250x150+530+250")
    info.resizable(False, False)
    info.iconbitmap('data\\photos\\icon.ico')
    info.title("info")

    btclose = Button(info, text="ok", bg='black', font=('arial', 18, 'bold'), command=close,
                     relief='groove', fg='white')
    btclose.place(x=100, y=95)

    inf1 = Label(info, text='coding by : ', font=('arial', 20, 'bold'),
                 justify='center', bg='white')
    inf1.place(x=50, y=10)

    inf2 = Label(info, text='abdallah mabrouk', font=('arial', 20, 'bold'),
                 justify='center', bg='white')
    inf2.place(x=5, y=50)
    info.lift()

def close():
    info.destroy()

def close_w():
    calculator.destroy()

def style_1():
    menu.configure(image=st1_menu_image)
    menu.outI = st1_menu_image
    menu.inI = st1_ac_menu
    bg_label.configure(image =st1_backgrond)
    bt1.configure(image =st1_num1)
    bt2.configure(image =st1_num2)
    bt3.configure(image =st1_num3)
    bt4.configure(image =st1_num4)
    bt5.configure(image =st1_num5)
    bt6.configure(image =st1_num6)
    bt7.configure(image =st1_num7)
    bt8.configure(image =st1_num8)
    bt9.configure(image =st1_num9)
    bt0.configure(image =st1_num0)
    btplus.configure(image =st1_plus)
    btminus.configure(image =st1_minus)
    btMultiply.configure(image =st1_Multiply)
    btDividing.configure(image =st1_Dividing)
    bt_c.configure(image =st1_clear)
    btdelete.configure(image =st1_del)
    btdot.configure(image =st1_dot)
    btEqual.configure(image =st1_Equal)
    btans.configure(image =st1_ans)

def style_2():
    menu.configure(image=st2_menu_image)
    menu.outI = st2_menu_image
    menu.inI = st2_ac_menu
    bg_label.configure(image =st2_backgrond)
    bt1.configure(image =st2_num1)
    bt2.configure(image =st2_num2)
    bt3.configure(image =st2_num3)
    bt4.configure(image =st2_num4)
    bt5.configure(image =st2_num5)
    bt6.configure(image =st2_num6)
    bt7.configure(image =st2_num7)
    bt8.configure(image =st2_num8)
    bt9.configure(image =st2_num9)
    bt0.configure(image =st2_num0)
    btplus.configure(image =st2_plus)
    btminus.configure(image =st2_minus)
    btMultiply.configure(image =st2_Multiply)
    btDividing.configure(image =st2_Dividing)
    bt_c.configure(image =st2_clear)
    btdelete.configure(image =st2_del)
    btdot.configure(image =st2_dot)
    btEqual.configure(image =st2_Equal)
    btans.configure(image =st2_ans)

def style_3():
    menu.configure(image=st3_menu_image)
    menu.outI=st3_menu_image
    menu.inI = st3_ac_menu
    bg_label.configure(image =st3_backgrond)
    bt1.configure(image =st3_num1)
    bt2.configure(image =st3_num2)
    bt3.configure(image =st3_num3)
    bt4.configure(image =st3_num4)
    bt5.configure(image =st3_num5)
    bt6.configure(image =st3_num6)
    bt7.configure(image =st3_num7)
    bt8.configure(image =st3_num8)
    bt9.configure(image =st3_num9)
    bt0.configure(image =st3_num0)
    btplus.configure(image =st3_plus)
    btminus.configure(image =st3_minus)
    btMultiply.configure(image =st3_Multiply)
    btDividing.configure(image =st3_Dividing)
    bt_c.configure(image =st3_clear)
    btdelete.configure(image =st3_del)
    btdot.configure(image =st3_dot)
    btEqual.configure(image =st3_Equal)
    btans.configure(image =st3_ans)

class ActiveMenubutton(Menubutton):
    def __init__(self, master,inimage=None, outimage=None):
        self.master = master
        self.inI  = PhotoImage(file='%s' % inimage)
        self.outI = PhotoImage(file='%s' % outimage)
        Menubutton.__init__(self, master, image=self.outI)
        self.configure(relief='flat', bd=0)

        self.bind('<Any-Enter>', lambda e, state=1, s=self:
                                              s.change(e, state))
        self.bind('<Any-Leave>', lambda e, state=0, s=self:
                                              s.change(e, state))

        self.menu = Menu(self, tearoff=0)
        self["menu"] = self.menu
    def change(self, event, state):
        if state:
            self.configure(image=self.inI)
        else:
            self.configure(image=self.outI)

################################widgets part################################
############################################################################

bg_label = Label(calculator,image=st1_backgrond,relief='flat' ,bd=0)
bg_label.place(x=0,y=0)

menu = ActiveMenubutton(calculator, inimage='data\\photos\\style1\\ac_menu.png',
                        outimage='data\\photos\\style1\\menu.png',)


menu.menu.add_cascade ( label="style1",command = style_1)
menu.menu.add_cascade ( label="style2",command = style_2)
menu.menu.add_cascade ( label="style3",command = style_3)
menu.menu.add_cascade ( label="about" ,command = about)
menu.menu.add_cascade ( label="Exit"  ,command = close_w)

menu.place(x=4,y=3)


up_result_entry = Entry(calculator,textvariable= ans,font=('arial',24,'bold'),width=16,
                        state = 'readonly')
up_result_entry.place(x=10,y=40)

down_result_entry = Entry(calculator,textvariable= total,font=('arial',24,'bold'),width=16,
                          state = 'readonly')
down_result_entry.place(x=10,y=80)

bt1 = Button(calculator,image = st1_num1, command = one, relief = 'flat', bd = 0)
bt1.place(x=10,y=320)

bt2 = Button(calculator,image = st1_num2, command = two, relief = 'flat', bd = 0)
bt2.place(x=90,y=320)

bt3 = Button(calculator,image = st1_num3, command = three, relief = 'flat', bd = 0)
bt3.place(x=170,y=320)

bt4 = Button(calculator,image = st1_num4, command = four, relief = 'flat', bd = 0)
bt4.place(x=10,y=260)

bt5 = Button(calculator,image = st1_num5, command = five, relief = 'flat', bd = 0)
bt5.place(x=90,y=260)

bt6 = Button(calculator,image = st1_num6, command = six, relief = 'flat', bd = 0)
bt6.place(x=170,y=260)

bt7 = Button(calculator,image = st1_num7, command = seven, relief = 'flat', bd = 0)
bt7.place(x=10,y=200)

bt8 = Button(calculator,image = st1_num8, command = eight, relief = 'flat', bd = 0,)
bt8.place(x=90,y=200)

bt9 = Button(calculator,image = st1_num9, command = nine, relief = 'flat', bd = 0)
bt9.place(x=170,y=200)

bt0 = Button(calculator,image = st1_num0, command = zero, relief = 'flat', bd = 0)
bt0.place(x=90,y=380)

btplus = Button(calculator,image = st1_plus, command = plus, relief = 'flat', bd = 0)
btplus.place(x=240,y=320)

btminus = Button(calculator,image = st1_minus, command = minus, relief = 'flat', bd = 0)
btminus.place(x=240,y=260)

btMultiply = Button(calculator,image = st1_Multiply, command = Multiply, relief = 'flat', bd = 0)
btMultiply.place(x=240,y=140)

btDividing = Button(calculator,image = st1_Dividing, command = Dividing, relief = 'flat', bd = 0)
btDividing.place(x=240,y=200)

bt_c = Button(calculator,image = st1_clear, command = c, relief = 'flat', bd = 0)
bt_c.place(x=10,y=140)

btdelete = Button(calculator,image = st1_del, command = delete, relief = 'flat', bd = 0)
btdelete.place(x=10,y=380)

btdot = Button(calculator,image = st1_dot, command = dot, relief = 'flat', bd = 0)
btdot.place(x=170,y=380)

btEqual = Button(calculator,image = st1_Equal, command = Equal, relief = 'flat', bd = 0)
btEqual.place(x=240,y=380)

btans = Button(calculator,image = st1_ans, command = Ans, relief = 'flat', bd = 0)
btans.place(x=90,y=140)


calculator.mainloop()
