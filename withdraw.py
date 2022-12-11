import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename, askopenfilenames
from tkinter import messagebox
root = tk.Tk()
root.title('출금')
root.minsize(400, 200)   # 최소 사이즈

frm0 = tk.LabelFrame(root, text="출금 정보", pady=15, padx=15)   # pad 내부
frm0.grid(row=0, column=0, pady=10, padx=10, sticky="nswe") # pad 내부

# 상단 프레임 (LabelFrame) 
frm1 = tk.LabelFrame(root, text="출금", pady=15, padx=15)   # pad 내부
frm1.grid(row=1, column=0, pady=10, padx=10, sticky="nswe") # pad 내부
root.columnconfigure(0, weight=1)   # 프레임 (0,0)은 크기에 맞춰 늘어나도록
root.rowconfigure(0, weight=1)      
# 하단 프레임 (Frame)
frm2 = tk.Frame(root, pady=10)
frm2.grid(row=2, column=0, pady=10)
'''2. 요소 생성'''
# 레이블
lbl1 = tk.Label(frm0, text='출금ID')
lbl3 = tk.Label(frm0, text='100')
lbl9 = tk.Label(frm0, text='고객ID')
lbl10 = tk.Label(frm0, text='100')
lbl11 = tk.Label(frm0, text='날짜')
lbl12 = tk.Label(frm0, text='2022-11-11')

lbl2 = tk.Label(frm0, text='Customer Name')
lbl90 = tk.Label(frm0, text='홍길동')

lbl4 = tk.Label(frm1, text='생성 날짜')
lbl5 = tk.Label(frm1, text='현재 날짜')
lbl6 = tk.Label(frm1, text='잔액')
lbl7 = tk.Label(frm1, text='총 출금액')
# 리스트박스

widget = tk.Listbox(frm1, width=30, height=5)
widget2 = tk.Listbox(frm1, width=10, height=5)
widget3 = tk.Listbox(frm1, width=30, height=5)
widget4 = tk.Listbox(frm1, width=10, height=5)
for i in range(1, 6):
    widget.insert(0, f'{100+i*2}')
    widget2.insert(0, f'{50+i*2}')
for i in range(1, 6):
    widget4.insert(0, f'{100+i*2}')
    widget4.insert(0, f'{50+i*2}')

for i in range(1, 6):
    widget.insert(0, f'{i+i} 순번의 고객님')
widget.insert(0, f'김문수 고객님')
widget.insert(0, f'장문수 고객님')
widget.insert(0, f'금문수 고객님')
widget.insert(0, f'경문수 고객님')
widget.insert(0, f'순문기 고객님')
widget3.insert(0, f'김문수 고객님')
widget3.insert(0, f'장문수 고객님')
widget3.insert(0, f'금문수 고객님')
widget3.insert(0, f'경문수 고객님')
widget3.insert(0, f'순문기 고객님')
widget.grid(row=4, column=0, pady=3)
widget2.grid(row=4, column=1, pady=3)
widget3.grid(row=5, column=0, pady=3)
widget4.grid(row=5, column=1, pady=3)
#텍스트

text1 = tk.Text(frm1, width=20, height=2)
text2 = tk.Text(frm1, width=20, height=2)

# 버튼
btn1 = tk.Button(frm2, text="저장", width=8)

btn0 = tk.Button(frm2, text="new", width=8)
# 스크롤바 - 기능 연결

'''3. 요소 배치'''
# 상단 프레임
lbl1.grid(row=0, column=0, sticky="w")
lbl3.grid(row=0, column=1, sticky="w")
lbl9.grid(row=0, column=2, sticky="w")
lbl10.grid(row=0, column=3, sticky="w", padx=20)
lbl11.grid(row=0, column=4, sticky="w", padx=20)
lbl12.grid(row=0, column=5, sticky="w", padx=20)

lbl2.grid(row=2, column=2, sticky="w", pady=10)
lbl90.grid(row=2, column=4, sticky="w", pady=10)
#lbl4.grid(row=3, column=0, sticky="w", pady=10)
#lbl5.grid(row=3, column=1, sticky="w")
lbl6.grid(row=6, column=0, sticky="w", pady=10)
lbl7.grid(row=7, column=0, sticky="w")

text1.grid(row=6, column=1, sticky="w")
text2.grid(row=7, column=1, sticky="w")



btn0.grid(row=0, column=0, sticky="w", padx=100)
btn1.grid(row=0, column=1, sticky="w")

# 상단프레임 grid (2,1)은 창 크기에 맞춰 늘어나도록
frm1.rowconfigure(2, weight=1)          
frm1.columnconfigure(1, weight=1)   
# 하단 프레임

'''실행'''
root.mainloop()