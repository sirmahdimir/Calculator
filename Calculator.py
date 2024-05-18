from customtkinter import *


class Calculator(CTk):
    def __init__(self):
        super().__init__()
        self._fg_color = '#708090'

        self.title('Calculator')
        self.minsize(450, 600)
        self.maxsize(450, 600)
        self.geometry("450x600+450+50")
        self._set_appearance_mode("dark")

        def add_num(value):    
            self.lbl.configure(text=self.lbl._text + value)
            
        def clear():    
            self.lbl.configure(text='') 

        def delete():
            self.lbl.configure(text=self.lbl._text[:-1]) 

        def answer():
            phrase = self.lbl._text
            result = eval(phrase)
            self.lbl.configure(text=str(result)) 

        
        font = CTkFont(family='Segoe Print',
                    size=30,
                    weight='bold')



        self.lbl = CTkLabel(self,
               text='',
               font=font,
               width=440,
               height=100,
               corner_radius=20,
               bg_color="silver"
               )
        self.lbl.grid(row=1, column=0, padx=5, pady=(15,10), sticky="ew", columnspan=4)

        self.btn_open_parentheses = CTkButton(self,
                text="(",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('('),
                textvariable='(' 
                )
        self.btn_open_parentheses.grid(row=2, column=0, padx=5, pady=(10,20), sticky="w")

        self.btn_close_parentheses = CTkButton(self,
                text=")",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num(')'),
                textvariable=')' 
                )
        self.btn_close_parentheses.grid(row=2, column=1, padx=5, pady=(10,20), sticky="w")

        self.btn_delete = CTkButton(self,
                text="←",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#696969",
                hover_color='#A9A9A9',
                font=font,
                bg_color="transparent", 
                command= delete,
                textvariable='←' 
                )
        self.btn_delete.grid(row=2, column=2, padx=5, pady=(10,20), sticky="w" )

        self.btn_minus = CTkButton(self,
                text="-",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#D2691E",
                hover_color='#F4A460',
                font=font,
                bg_color="transparent", 
                command= lambda: add_num('-'),
                textvariable='-' 
                )
        self.btn_minus.grid(row=2, column=3, padx=5, pady=(10,20), sticky="w" )

        self.btn_7 = CTkButton(self,
                text="7",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('7'),
                textvariable='7' 
                )
        self.btn_7.grid(row=3, column=0, padx=5, pady=(10,20), sticky="w")

        self.btn_8 = CTkButton(self,
                text="8",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('8'),
                textvariable='8' 
                )
        self.btn_8.grid(row=3, column=1, padx=5, pady=(10,20), sticky="w")

        self.btn_9 = CTkButton(self,
                text="9",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('9'),
                textvariable='9' 
                )
        self.btn_9.grid(row=3, column=2, padx=5, pady=(10,20), sticky="w")

        self.btn_division = CTkButton(self,
                text="/",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#D2691E",
                hover_color='#F4A460',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('/'),
                textvariable='/' 
                )
        self.btn_division.grid(row=3, column=3, padx=5, pady=(10,20), sticky="w")

        self.btn_4 = CTkButton(self,
                text="4",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('4'),
                textvariable='4' 
                )
        self.btn_4.grid(row=4, column=0, padx=5, pady=(10,20), sticky="w")

        self.btn_5 = CTkButton(self,
                text="5",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('5'),
                textvariable='5' 
                )
        self.btn_5.grid(row=4, column=1, padx=5, pady=(10,20), sticky="w")

        self.btn_6 = CTkButton(self,
                text="6",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('6'),
                textvariable='6' 
                )
        self.btn_6.grid(row=4, column=2, padx=5, pady=(10,20), sticky="w")

        self.btn_multiplication = CTkButton(self,
                text="×",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#D2691E",
                hover_color='#F4A460',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('*'),
                textvariable='*' 
                )
        self.btn_multiplication.grid(row=4, column=3, padx=5, pady=(10,20), sticky="w")

        self.btn_1 = CTkButton(self,
                text="1",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('1'),
                textvariable='1' 
                )
        self.btn_1.grid(row=5, column=0, padx=5, pady=(10,20), sticky="w")

        self.btn_2 = CTkButton(self,
                text="2",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('2'),
                textvariable='2' 
                )
        self.btn_2.grid(row=5, column=1, padx=5, pady=(10,20), sticky="w")

        self.btn_3 = CTkButton(self,
                text="3",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('3'),
                textvariable='3' 
                )
        self.btn_3.grid(row=5, column=2, padx=5, pady=(10,20), sticky="w")

        self.btn_sum = CTkButton(self,
                text="+",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#D2691E",
                hover_color='#F4A460',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('+'),
                textvariable='+' 
                )
        self.btn_sum.grid(row=5, column=3, padx=5, pady=(10,20), sticky="w")

        self.btn_clear = CTkButton(self,
                text="C",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#FF3232",
                hover_color='#FF5454',
                font=font,
                bg_color="transparent", 
                command= clear,
                textvariable='C' 
                )
        self.btn_clear.grid(row=6, column=0, padx=5, pady=(10,20), sticky="w")

        self.btn_0 = CTkButton(self,
                text="0",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('0'),
                textvariable='0' 
                )
        self.btn_0.grid(row=6, column=1, padx=5, pady=(10,20), sticky="w")

        self.btn_dot = CTkButton(self,
                text=".",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#6495ED",
                hover_color='#4169E1',
                font=font,
                bg_color="transparent", 
                command=lambda: add_num('.'),
                textvariable='.' 
                )
        self.btn_dot.grid(row=6, column=2, padx=5, pady=(10,20), sticky="w")

        self.btn_equal = CTkButton(self,
                text="=",
                width=100,
                corner_radius=20,
                border_width=5,
                border_color='#2F4F4F',
                fg_color="#006400",
                hover_color='#228B22',
                font=font,
                bg_color="transparent", 
                command= answer,
                textvariable='=' 
                )
        self.btn_equal.grid(row=6, column=3, padx=5, pady=(10,20), sticky="w")




app = Calculator()
app.mainloop()

