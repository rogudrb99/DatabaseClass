import tkinter as tk
import tkinter.ttk
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
#트리뷰

#트리뷰
treeview=tkinter.ttk.Treeview(frm1, columns=["one", "two","three"], displaycolumns=["one","two","three"])


# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview.column("#0", width=100,)
treeview.heading("#0", text="index")

treeview.column("#1", width=100, anchor="center")
treeview.heading("one", text="고객 이름", anchor="center")

treeview.column("#2", width=100, anchor="center")
treeview.heading("two", text="고객 ID", anchor="center")

treeview.column("#3", width=70, anchor="center")
treeview.heading("three", text="계좌 정보", anchor="center")

# 표에 삽입될 데이터
treelist=[("Tom", 80, 3), ("Bani", 71, 5), ("Boni", 90, 2), ("Dannel", 78, 4), ("Minho", 93, 1)]

# 표에 데이터 삽입
for i in range(len(treelist)):
    treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i)+"번")

# 슴겨진 항목
top=treeview.insert('', 'end', text="비밀 고객(VIP) LIST", iid="5번")
top_mid1=treeview.insert(top, 'end', text="5", values=["Timy", 0, 8], iid="5번-1")
top_mid2=treeview.insert(top, 0, text="6", values=["Ann", 35, 7], iid="5번-0")
top_mid3=treeview.insert(top, 'end', text="7", values=["Sany", 60, 6], iid="5번-2")


# 레이블
lbl1 = tk.Label(frm1, text='Customer Name')
lbl2 = tk.Label(frm1, text='가입 날짜')
lbl3 = tk.Label(frm1, text='현재 날짜')
# 리스트박스
widget = tk.Listbox(frm1, width=15, height=15)





widget.insert(0, f'고객 별 조회') 
widget.insert(0, f'출금 조회')
widget.insert(0, f'ACCOUNT 리스트')
widget.insert(0, f'ACCOUNT') 
widget.insert(0, f'고객 리스트') 
widget.insert(0, f'고객 가입')
#텍스트
text1 = tk.Text(frm1, width=30, height=2)
# 버튼
btn1 = tk.Button(frm2, text="저장", width=8)

btn0 = tk.Button(frm2, text="불러오기", width=8)
# 스크롤바 - 기능 연결

'''3. 요소 배치'''
# 상단 프레임

lbl3.grid(row=2, column=1, sticky="w", padx=100)
widget.grid(row=1, column=0, pady=3)


btn0.grid(row=0, column=0, sticky="w", padx=100)
btn1.grid(row=0, column=1, sticky="w")
treeview.grid(row=1, column=1, sticky="w", padx=50)

# 상단프레임 grid (2,1)은 창 크기에 맞춰 늘어나도록
frm1.rowconfigure(2, weight=1)          
frm1.columnconfigure(1, weight=1)   
# 하단 프레임

'''실행'''
root.mainloop()