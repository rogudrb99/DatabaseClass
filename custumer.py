import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames
from tkinter import messagebox
root = tk.Tk()
root.title('Customer')
root.minsize(400, 200)   # 최소 사이즈


# 상단 프레임 (LabelFrame) 
frm1 = tk.LabelFrame(root, text="고객", pady=15, padx=15)   # pad 내부
frm1.grid(row=0, column=0, pady=10, padx=10, sticky="nswe") # pad 내부
root.columnconfigure(0, weight=1)   # 프레임 (0,0)은 크기에 맞춰 늘어나도록
root.rowconfigure(0, weight=1)      
# 하단 프레임 (Frame)
frm2 = tk.Frame(root, pady=10)
frm2.grid(row=1, column=0, pady=10)
'''2. 요소 생성'''
# 레이블
lbl1 = tk.Label(frm1, text='Customer Name')
lbl2 = tk.Label(frm1, text='가입 날짜')
lbl3 = tk.Label(frm1, text='현재 날짜')
# 리스트박스

#텍스트
text1 = tk.Text(frm1, width=30, height=2)
# 버튼
btn1 = tk.Button(frm2, text="저장", width=8)

btn0 = tk.Button(frm2, text="new", width=8)
# 스크롤바 - 기능 연결

'''3. 요소 배치'''
# 상단 프레임
lbl1.grid(row=0, column=0, sticky="w")
lbl2.grid(row=2, column=0, sticky="w")
lbl3.grid(row=2, column=1, sticky="w", padx=100)

text1.grid(row=0, column=1)

btn0.grid(row=0, column=0, sticky="w", padx=100)
btn1.grid(row=0, column=1, sticky="w")

# 상단프레임 grid (2,1)은 창 크기에 맞춰 늘어나도록
frm1.rowconfigure(2, weight=1)          
frm1.columnconfigure(1, weight=1)   
# 하단 프레임

'''실행'''
root.mainloop()