import tkinter as tk
from PIL import Image, ImageTk
import socketio
import random

# 소켓 클라이언트 설정
sio = socketio.Client()

# 서버
sio.connect('http://localhost:3000/')

# 이미지 흔들기 함수
def shake_carrot():
    # 흔들림 애니메이션 구현
    def shake(step):
        if step < 10:  # 10번 정도 흔듭니다.
            # 랜덤으로 이미지 위치를 좌우로 약간 이동
            x_offset = random.randint(-10, 10)
            y_offset = random.randint(-5, 5)
            label.place(x=original_x + x_offset, y=original_y + y_offset)
            root.after(50, shake, step + 1)  # 50밀리초마다 반복
        else:
            # 애니메이션이 끝나면 원래 위치로 되돌림
            label.place(x=original_x, y=original_y)
    
    shake(0)  # 애니메이션 시작

# 클릭 이벤트 발생 시 서버로 메시지 전송
def on_click(event):
    sio.emit('shakeCarrot')

# 서버에서 당근 흔들기 신호를 받으면 흔들기
@sio.event
def shakeCarrot():
    shake_carrot()

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("Carrot App")
root.geometry("300x300")  # 윈도우 크기


# 당근 이미지 불러오기
carrot_image = Image.open("carrot.png")
carrot_photo = ImageTk.PhotoImage(carrot_image)

# 라벨에 이미지 표시
label = tk.Label(root, image=carrot_photo)
label.place(x=0, y=0)  # 이미지 초기 위치 설정

# 이미지 원래 위치 저장
original_x, original_y = 0, 0

# 이미지 클릭 이벤트 바인딩
label.bind('<Button-1>', on_click)

# 윈도우 실행
root.mainloop()

# 소켓 종료 시 서버와 연결 해제
sio.disconnect()
