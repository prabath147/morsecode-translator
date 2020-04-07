import tkinter as tk


import string



class choice(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='blue')
 
        k1=tk.Button(self,text="Login", height="2", width="30", command=lambda: controller.show_frame('login'))

        k2=tk.Button(self,text="Register", height="2", width="30", command=lambda: controller.show_frame("register"))
        k2.place(relx = 0.425, rely = 0.3) 
        k1.place(relx = 0.425, rely = 0.4)

class login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='blue')
        
        r1=tk.Label(self, text="User Name :")
        r2=tk.Label(self, text="Password :")
        username_login_entry = tk.Entry(self,bd=5)
 
        password_login_entry = tk.Entry(self, show= '*',bd=5)
       
        r1.place(x=550,y=150)
        r2.place(x=550,y=225)
        username_login_entry.place(relx=0.48,rely=0.175)
        password_login_entry.place(relx=0.48,rely=0.265)
        b= tk.Button(self,text='submit',width=10, height=1,bg='red', command =lambda:controller.show_frame("StartPage"))
        b.place(relx = 0.435, rely = 0.4) 
        k2=tk.Button(self,text="home", height="2", width="30", command=lambda: controller.show_frame("choice"))
        k2.place(relx = 0.4, rely = 0.8)
       
class register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='blue')
        
     
        
        username_lable = tk.Label(self, text="Username : ")
        username_lable.place(x=550,y=200)
        username_entry = tk.Entry(self,bd=5)
        username_entry.place(relx=0.49,rely=0.23)
        password_lable = tk.Label(self, text="Password : ")
        password_lable.place(x=550,y=250)
        password_entry = tk.Entry(self,show='*',bd=5)
        password_entry.place(relx=0.49,rely=0.288)
        g1=tk.Label(self,text='gender : ')
        g1.place(x=550,y=350)
        s1=tk.Radiobutton(self,text='male',value=1)
        s1.place(relx=0.49,rely=0.415)
        s2=tk.Radiobutton(self,text='female',value=2)
        s2.place(relx=0.58,rely=0.415)
        g1=tk.Label(self,text='email : ')
        g1.place(x=550,y=300)
        u1 = tk.Entry(self,bd=5)
        u1.place(relx=0.49,rely=0.35)
        k2=tk.Button(self, text="Register", width=10, height=1, bg='red')
        k2.place(relx = 0.445, rely = 0.54)
        
        k2=tk.Button(self,text="home", height="2", width="30", command=lambda: controller.show_frame("choice"))
        k2.place(relx = 0.4, rely = 0.8) 
class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,Pagethree,Pagefour,login,register,choice):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

           
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("choice")
         
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    #def get_page(self, page_class):
        #frame= self.frames[page_class]
        #frame.tkraise()
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.geometry('3000x2700')
        self.config(bg='blue')

        label = tk.Label(self, text="MORSE CODE TRANSLATOR",font=("Arial", 26),bg='blue',fg='red')
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="encrypt",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="decrypt",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="encrypt & decrypt",
                            command=lambda: controller.show_frame("Pagethree"))
        
        button1.place(relx=0.48, rely=0.2) 
        button2.place(relx = 0.48, rely = 0.3) 
        button3.place(relx = 0.48, rely = 0.4) 

class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='blue')
        r1=tk.Label(self, text="encrypt :")
        r1.place(x=550,y=200)
        ju=tk.Entry(self,bd=6)
        ju.pack()
        ju.place(relx=0.49,rely=0.231)
        hu=tk.Button(self,text='result',command=lambda:mai1(self))
        hu.place(relx = 0.465, rely = 0.4) 

        #Pagefour(self,controller)
        
        def mai1(self): 
           #global re
                #a=tk.StringVar()
                #self.dum=tk.StringVar()
           message1=tk.Entry.get(ju)
           result1 = encrypt(message1.upper()) 
                #self.dum.get(result1)
                #se=result1
           with open('mc.txt','w') as f:
              data=f.write('encoded format')
              data=f.write('\n')
              data=f.write(result1)
                    
           f.close()
                
           print(result1)
           def sr(self):
             rq=tk.Label(self,text=result1,height=2,width=5,font=("Arial", 16),bg='red')
             rq.place(relx = 0.465, rely = 0.5)
             w1=tk.Button(self,text='clear',command=lambda:rq.destroy())
             w1.place(relx = 0.465, rely = 0.6)
           q1=tk.Button(self,text='show result',command=lambda:sr(self))
           q1.place(relx = 0.465, rely = 0.4)
           
           q2=tk.Button(self, text="save result in file",
                            command=lambda: controller.show_frame("Pagefour"))
           q2.place(relx = 0.465, rely = 0.45)
           
          
        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                        'C':'-.-.', 'D':'-..', 'E':'.', 
                        'F':'..-.', 'G':'--.', 'H':'....', 
                        'I':'..', 'J':'.---', 'K':'-.-', 
                        'L':'.-..', 'M':'--', 'N':'-.', 
                        'O':'---', 'P':'.--.', 'Q':'--.-', 
                        'R':'.-.', 'S':'...', 'T':'-', 
                        'U':'..-', 'V':'...-', 'W':'.--', 
                        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                        '1':'.----', '2':'..---', '3':'...--', 
                        '4':'....-', '5':'.....', '6':'-....', 
                        '7':'--...', '8':'---..', '9':'----.', 
                        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                        '?':'..--..', '/':'-..-.', '-':'-....-', 
                        '(':'-.--.', ')':'-.--.-'} 
      
     
        def encrypt(message): 
                cipher = '' 
                for letter in message: 
                    if letter != ' ':          
                        cipher += MORSE_CODE_DICT[letter] + ' '
                    else:             
                        cipher += ' ' 
                    
                return cipher 
        def decrypt(message): 
              
                
                message += ' '
              
                decipher = '' 
                citext = '' 
                for letter in message: 
              
                  
                    if (letter != ' '): 
              
                         
                        i = 0
              
                        
                        citext += letter 
              
                    
                    else: 
                        
                        i += 1
              
                         
                        if i == 2 : 
              
                              
                            decipher += ' '
                        else: 
              
                           
                            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                            .values()).index(citext)] 
                            citext = '' 
                
                return decipher 
    
        button = tk.Button(self, text="Go to the start page",
                               command=lambda: controller.show_frame("StartPage"))
        button.place(relx = 0.445, rely = 0.9) 
            
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='blue')
        r2=tk.Label(self, text="decrypt :") 
        r2.place(x=550,y=250)
        lo=tk.Entry(self,bd=6)
        lo.pack()
        lo.place(relx=0.49,rely=0.29)
        hu=tk.Button(self,text='result',command=lambda:mai2())
        hu.place(relx = 0.465, rely = 0.4) 
        #l1=tk.Label(self,text=''A':'.-'\n 'B':'-...'\n'C':'-.-.'\n 'D':'-..'\n'E':'.'\n'F':'..-.'\n 'G':'--.'\n 'H':'....'\n'I':'..'\n 'J':'.---'\n 'K':'-.-'\n)
        w3=tk.Label(self,text='A : .-\n B :-...\n C : -.-.\n D : -..\n E : .\n F : ..-.\n G : --.\n H : ....\n I : ..\n J : .---\n K : -.-\n L : .-..\n M : --\n N : -.\n O : ---\n P : .--.\n Q : --.-\n R : .-.\n S : ...\n T : -\n U : ..-\n V : ...-\n W : .--\n X : -..-\n Y : -.--\n Z : --..\n 1 : .----\n 2 : ..---\n 3 : ...--\n 4 : ....-\n 5 : .....\n 6 : -....\n 7 : --...\n 8 : ---..\n 9 : ----.\n 0 : -----\n , : --..--\n . : .-.-.-\n ? : ..--..\n / : -..-.\n - : -....-\n ( : -.--.\n ) : -.--.-',bg='red')
        w3.place(relx=0,rely=0)
        def mai2(): 

            message2=tk.Entry.get(lo)
            result2 = decrypt(message2) 
        
            with open('dec.txt','w') as y:
               data1=y.write(result2)
               
            y.close()
        
            print(result2)
            def sr1(self):
              rq=tk.Label(self,text=result2,height=2,width=5,font=("Arial", 16),bg='red')
              rq.place(relx = 0.465, rely = 0.5)
              w1=tk.Button(self,text='clear',command=lambda:rq.destroy())
              w1.place(relx = 0.465, rely = 0.6)
            q1=tk.Button(self,text='show result',command=lambda:sr1(self))
            q1.place(relx = 0.465, rely = 0.4)

            q2=tk.Button(self, text="save result in file",
                            command=lambda: controller.show_frame("Pagefour"))
            q2.place(relx = 0.465, rely = 0.45)
            #rq=tk.Label(self,text=result2).pack()
           # b2=tk.Button(self,text='result2',command=lambda:de(result2))
            #b2.pack()
        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
 
        def encrypt(message): 
            cipher = '' 
            for letter in message: 
                if letter != ' ':          
                    cipher += MORSE_CODE_DICT[letter] + ' '
                else:             
                    cipher += ' ' 
            
            return cipher 
        def decrypt(message): 
          
            
            message += ' '
          
            decipher = '' 
            citext = '' 
            for letter in message: 
          
              
                if (letter != ' '): 
          
                     
                    i = 0
          
                    
                    citext += letter 
          
                
                else: 
                    
                    i += 1
          
                     
                    if i == 2 : 
          
                          
                        decipher += ' '
                    else: 
          
                       
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                        .values()).index(citext)] 
                        citext = '' 
            
            return decipher 
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.place(relx = 0.445, rely = 0.9) 
class Pagethree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='blue')
        r1=tk.Label(self, text="encrypt :")
        r2=tk.Label(self, text="decrypt :")    
        r1.place(x=550,y=200)
        r2.place(x=550,y=250)
        ju=tk.Entry(self,bd=6)
        ju.pack()
        lo=tk.Entry(self,bd=6)
        lo.pack()
        ju.place(relx=0.49,rely=0.23)
        lo.place(relx=0.49,rely=0.288)
        hu=tk.Button(self,text='start',command=lambda:mai())
        hu.place(relx = 0.465, rely = 0.4) 
        #hb=tk.Button(self,,command=self.quit).pack()
        w3=tk.Label(self,text='A : .-\n B :-...\n C : -.-.\n D : -..\n E : .\n F : ..-.\n G : --.\n H : ....\n I : ..\n J : .---\n K : -.-\n L : .-..\n M : --\n N : -.\n O : ---\n P : .--.\n Q : --.-\n R : .-.\n S : ...\n T : -\n U : ..-\n V : ...-\n W : .--\n X : -..-\n Y : -.--\n Z : --..\n 1 : .----\n 2 : ..---\n 3 : ...--\n 4 : ....-\n 5 : .....\n 6 : -....\n 7 : --...\n 8 : ---..\n 9 : ----.\n 0 : -----\n , : --..--\n . : .-.-.-\n ? : ..--..\n / : -..-.\n - : -....-\n ( : -.--.\n ) : -.--.-',bg='red')
        w3.place(relx=0,rely=0)

        def mai(): 
            message1=tk.Entry.get(ju)
            result1 = encrypt(message1.upper()) 
            message2=tk.Entry.get(lo)
            result2 = decrypt(message2) 
            
            with open('mc.txt','w') as f:
               data=f.write('encoded format')
               data=f.write('\n')
               data=f.write(result1)
                
            f.close()
            with open('dec.txt','w') as y:
               data1=y.write(result2)
               
            y.close()
            print(result1)
            print(result2)
            def sr2(self):
             rq=tk.Label(self,text=result1,height=2,width=5,font=("Arial", 16),bg='red')
             rq.place(relx = 0.465, rely = 0.5)
             rg=tk.Label(self,text=result2,height=2,width=5,font=("Arial", 16),bg='red')
             rg.place(relx = 0.465, rely = 0.6)
           
            q1=tk.Button(self,text='show result',command=lambda:sr2(self))
            q1.place(relx = 0.465, rely = 0.4)
            q2=tk.Button(self, text="save result in file",
                            command=lambda: controller.show_frame("Pagefour"))
            q2.place(relx = 0.465, rely = 0.45)
            
        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
 
        def encrypt(message): 
            cipher = '' 
            for letter in message: 
                if letter != ' ':          
                    cipher += MORSE_CODE_DICT[letter] + ' '
                else:             
                    cipher += ' ' 
            
            return cipher 
        def decrypt(message): 
          
            
            message += ' '
          
            decipher = '' 
            citext = '' 
            for letter in message: 
          
              
                if (letter != ' '): 
          
                     
                    i = 0
          
                    
                    citext += letter 
          
                
                else: 
                    
                    i += 1
          
                     
                    if i == 2 : 
          
                          
                        decipher += ' '
                    else: 
          
                       
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                        .values()).index(citext)] 
                        citext = '' 
            
            return decipher 

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.place(relx = 0.445, rely = 0.9) 
class Pagefour(tk.Frame):
     #print(ew)
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg='blue')
        li=tk.Label(self,text='result saved').pack()
       

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
