import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames
from tkinter import messagebox
root = tk.Tk()
root.title('Customer List')
root.minsize(400, 200)   # 최소 사이즈


# 상단 프레임 (LabelFrame) 
frm1 = tk.LabelFrame(root, text="고객 리스트", pady=15, padx=15)   # pad 내부
frm1.grid(row=0, column=0, pady=10, padx=10, sticky="nswe") # pad 내부
root.columnconfigure(0, weight=1)   # 프레임 (0,0)은 크기에 맞춰 늘어나도록
root.rowconfigure(0, weight=1)      
# 하단 프레임 (Frame)
frm2 = tk.Frame(root, pady=10)
frm2.grid(row=1, column=0, pady=10)
'''2. 요소 생성'''
# 레이블
widget = tk.Listbox(frm1, width=50, height=10)

for i in range(1, 6):
    widget.insert(0, f'{i+i} 순번의 고객님')
widget.insert(0, f'김문수 고객님')
widget.insert(0, f'장문수 고객님')
widget.insert(0, f'금문수 고객님')
widget.insert(0, f'경문수 고객님')
widget.insert(0, f'순문기 고객님')
widget.grid(row=1, column=1)

# 스크롤바 - 기능 연결

'''3. 요소 배치'''
# 상단 프레임

# 상단프레임 grid (2,1)은 창 크기에 맞춰 늘어나도록
frm1.rowconfigure(2, weight=1)          
frm1.columnconfigure(1, weight=1)   
# 하단 프레임

'''실행'''
root.mainloop()