import tkinter as tk
import mss
from PIL import Image, ImageTk
from screeninfo import get_monitors

# Tkinter 메인 윈도우 생성
root = tk.Tk()
root.title("Screen Capture Tool")

# 메뉴바 생성
menubar = tk.Menu(root)
root.config(menu=menubar)

# 드래그 상태 관리 변수
is_dragging = False
start_x, start_y = 0, 0
rect = None  # 사각형 저장 변수
transparent_windows = []

# 화면 캡처를 위한 객체 생성
sct = mss.mss()

# 캡처할 영역의 정보를 담을 변수
left = top = width = height = 0
selected_area = False

# 실시간 화면 캡처가 이미 실행 중인지 여부 확인
capturing = False
label = None  # 캡처된 이미지를 표시할 라벨

# 투명한 창에서 사각형을 그릴 캔버스 생성 함수
def create_transparent_window():
    monitors = get_monitors()
    for monitor in monitors:
        transparent_window = tk.Toplevel(root)
        transparent_window.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")
        transparent_window.attributes("-alpha", 0.3)  # 투명도 설정
        transparent_window.attributes("-topmost", True)  # 최상위 창으로 설정
        transparent_window.overrideredirect(True)  # 테두리 제거

        # 캔버스 생성
        canvas = tk.Canvas(transparent_window, bg="black", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        # 마우스 이벤트 바인딩
        canvas.bind("<ButtonPress-1>", lambda event, m=monitor, c=canvas: on_start_drag(event, c, m))
        canvas.bind("<B1-Motion>", lambda event, c=canvas: on_drag(event, c))
        canvas.bind("<ButtonRelease-1>", lambda event, c=canvas, w=transparent_window: on_end_drag(event, c, w))

        # ESC 키 눌렀을 때 비활성화
        canvas.bind("<Escape>", lambda event, w=transparent_window: on_esc_press(event, w))

        transparent_windows.append(transparent_window)

# 드래그 시작
def on_start_drag(event, canvas, monitor):
    global start_x, start_y, rect, current_monitor
    current_monitor = monitor  # 현재 드래그 중인 모니터를 저장
    start_x, start_y = event.x + monitor.x, event.y + monitor.y  # 모니터의 절대 좌표로 변환
    if rect is not None:
        canvas.delete(rect)  # 이전 사각형 삭제
    rect = canvas.create_rectangle(event.x, event.y, event.x, event.y, outline="red", width=2)

# 드래그 중
def on_drag(event, canvas):
    global rect
    if current_monitor:
        # 시작 좌표와 현재 좌표를 비교하여 사각형 크기 업데이트
        canvas.coords(rect, start_x - current_monitor.x, start_y - current_monitor.y, event.x, event.y)

# 드래그 종료
def on_end_drag(event, canvas, window):
    global left, top, width, height, selected_area, is_dragging, transparent_windows, capturing, label

    # 좌표 계산 (절대 좌표로 계산)
    end_x = event.x + window.winfo_x()
    end_y = event.y + window.winfo_y()
    left = min(start_x, end_x)
    top = min(start_y, end_y)
    width = abs(start_x - end_x)
    height = abs(start_y - end_y)
    selected_area = True
    is_dragging = False

    # 투명 창 닫기
    for win in transparent_windows:
        win.destroy()
    transparent_windows.clear()

    # 새로운 영역이 선택되었으므로, 이전 캡처를 중단하고 새로운 캡처를 시작
    if capturing:
        label.destroy()
        capturing = False

    # 선택한 영역을 메인 윈도우에 실시간 표시
    capture_and_show()

# ESC 키로 투명 창 닫기
def on_esc_press(event, window):
    global transparent_windows
    window.destroy()
    transparent_windows.clear()

# 실시간 화면 캡처 및 표시
def capture_and_show():
    global left, top, width, height, capturing, label

    if selected_area:
        def update_capture():
            monitor = {"top": top, "left": left, "width": width, "height": height}
            screenshot = sct.grab(monitor)

            # Pillow로 이미지 변환
            img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
            img_tk = ImageTk.PhotoImage(img)

            # Tkinter 윈도우에 이미지 표시
            label.config(image=img_tk)
            label.image = img_tk  # Garbage collection 방지
            
            # 100ms마다 다시 화면을 캡처
            root.after(100, update_capture)

        # 캡처 이미지를 보여줄 라벨
        label = tk.Label(root)
        label.pack()

        capturing = True  # 실시간 캡처가 실행 중임을 표시
        update_capture()

# 메뉴에 "Drag Start" 버튼 추가
def on_drag_start():
    create_transparent_window()

# F2 키 입력 시 메인 윈도우를 최상단에 고정
def on_f2_press(event):
    root.attributes("-topmost", True)

# F3 키 입력 시 메인 윈도우의 최상단 고정 해제
def on_f4_press(event):
    root.attributes("-topmost", False)

# 키 입력 이벤트 바인딩 추가
root.bind("<F2>", on_f2_press)
root.bind("<F4>", on_f4_press)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Drag Start", command=on_drag_start)

# Tkinter 윈도우 실행
root.mainloop()
