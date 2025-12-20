import tkinter as tk
import random

# 初始化分數
player_score = 0
computer_score = 0

choices = ["剪刀", "石頭", "布",]

def play(player_choice):
    global player_score, computer_score

    if player_score == 3 or computer_score == 3:
        return

    computer_choice = random.choice(choices)

    result_text = f"你出：{player_choice}\n電腦出：{computer_choice}\n"

    if player_choice == computer_choice:
        result_text += "結果：平手！"
    elif (
        (player_choice == "剪刀" and computer_choice == "布") or
        (player_choice == "布" and computer_choice == "石頭") or
        (player_choice == "石頭" and computer_choice == "剪刀")
    ):
        player_score += 1
        result_text += "結果：你贏了！"
    else:
        computer_score += 1
        result_text += "結果：你輸了！"

    result_label.config(text=result_text)
    score_label.config(text=f"比分 - 你：{player_score} | 電腦：{computer_score}")

    if player_score == 3:
        final_label.config(text="🎉 恭喜你獲得五戰三勝！")
    elif computer_score == 3:
        final_label.config(text="😢 電腦獲得五戰三勝！")

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="比分 - 你：0 | 電腦：0")
    final_label.config(text="")

# 建立視窗
root = tk.Tk()
root.title("剪刀・石頭・布（五戰三勝）")
root.geometry("350x300")

# 標題
title_label = tk.Label(root, text="剪刀・石頭・布", font=("Arial", 16))
title_label.pack(pady=10)

# 按鈕區
button_frame = tk.Frame(root)
button_frame.pack()

for choice in choices:
    btn = tk.Button(
        button_frame,
        text=choice,
        width=8,
        command=lambda c=choice: play(c)
    )
    btn.pack(side=tk.LEFT, padx=5)

# 結果顯示
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# 分數顯示
score_label = tk.Label(root, text="比分 - 你：0 | 電腦：0", font=("Arial", 12))
score_label.pack()

# 最終結果
final_label = tk.Label(root, text="", font=("Arial", 14), fg="red")
final_label.pack(pady=10)

# 重來按鈕
reset_button = tk.Button(root, text="重新開始", command=reset_game)
reset_button.pack()

root.mainloop()