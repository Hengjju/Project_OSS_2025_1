import tkinter as tk
from fractions import Fraction

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.is_fraction_display = False 

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['Frac', 'Dec', '='] # Frac (분수), Dec (소수) 변환 버튼 추가
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.is_fraction_display = False
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'Frac': # 분수 변환 버튼
            try:
                current_value = float(self.expression) 
                frac_value = Fraction(current_value).limit_denominator(1000000) 
                self.expression = str(frac_value)
                self.is_fraction_display = True
            except ValueError: # 숫자가 아닌 경우 (예: "에러" 상태)
                self.expression = "변환 불가"
            except ZeroDivisionError: # 0으로 나누기 에러가 발생한 경우 (예: eval에서)
                self.expression = "변환 불가"
            except Exception:
                self.expression = "변환 에러"

        elif char == 'Dec': # 소수 변환 버튼
            try:
                if self.is_fraction_display:
                   
                    dec_value = float(Fraction(self.expression)) 
                    self.expression = str(dec_value)
                    self.is_fraction_display = False
            except ValueError:
                self.expression = "변환 불가"
            except Exception:
                self.expression = "변환 에러"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



