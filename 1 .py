import tkinter as tk
from tkinter import messagebox

# ------------------
# 遊戲設定
# ------------------
ANSWER = "WORLD"
MAX_TRIES = 6
current_try = 0

# ------------------
# 主視窗
# ------------------
root = tk.Tk()
root.title("Wordle - Tkinter Version")
root.geometry("420x500")
root.resizable(False, False)

# ------------------
# 標題
# ------------------
title = tk.Label(root, text="WORDLE", font=("Arial", 24, "bold"))
title.pack(pady=10)

rule = tk.Label(
    root,
    text="Guess the Wordle in 6 tries\nAnswer: WORLD",
    font=("Arial", 12)
)
rule.pack(pady=5)

# ------------------
# 顯示區（6 行 × 5 格）
# ------------------
board_frame = tk.Frame(root)
board_frame.pack(pady=20)

labels = []

for row in range(MAX_TRIES):
    row_labels = []
    for col in range(5):
        lbl = tk.Label(
            board_frame,
            text=" ",
            font=("Arial", 18, "bold"),
            width=4,
            height=2,
            relief="solid",
            bg="white"
        )
        lbl.grid(row=row, column=col, padx=5, pady=5)
        row_labels.append(lbl)
    labels.append(row_labels)

# ------------------
# 檢查答案
# ------------------
def check_word():
    global current_try

    guess = entry.get().upper()

    if len(guess) != 5 or not guess.isalpha():
        messagebox.showwarning("錯誤", "請輸入 5 個英文字母")
        return

    entry.delete(0, tk.END)

    # 逐字母比對
    for i in range(5):
        letter = guess[i]
        lbl = labels[current_try][i]
        lbl.config(text=letter)

        if letter == ANSWER[i]:
            lbl.config(bg="green", fg="white")
        elif letter in ANSWER:
            lbl.config(bg="gold", fg="black")
        else:
            lbl.config(bg="light gray", fg="black")

    # 勝利判定
    if guess == ANSWER:
        messagebox.showinfo("🎉 恭喜", "你猜對了！")
        root.destroy()
        return

    current_try += 1

    # 失敗判定
    if current_try >= MAX_TRIES:
        messagebox.showinfo("😢 遊戲結束", f"正確答案是：{ANSWER}")
        root.destroy()

# ------------------
# 輸入區
# ------------------
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=10)
entry.focus()

submit_btn = tk.Button(
    root,
    text="Submit",
    font=("Arial", 14),
    command=check_word
)
submit_btn.pack(pady=10)

# Enter 鍵提交
root.bind("<Return>", lambda event: check_word())

root.mainloop()
