import cv2
import numpy as np

# (1) cloud.mp4から1フレーム目を読み込む
cap = cv2.VideoCapture("cloud.mp4")
ret, frame1 = cap.read()
if not ret:
    print("Error: Could not read video.")
    exit()

prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# オプティカルフロー（速度場）を描画するための関数
def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = img.copy()
    cv2.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    return vis

# (3) の変化を確認するための動画保存設定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
h, w = frame1.shape[:2]
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0 or np.isnan(fps):
    fps = 30.0
out = cv2.VideoWriter("velocity_field_changes.mp4", fourcc, fps, (w, h))

n = 2
while True:
    ret, frame_n = cap.read()
    if not ret:
        break
    
    next_gray = cv2.cvtColor(frame_n, cv2.COLOR_BGR2GRAY)
    
    # (2) & (3) 1フレーム目とnフレーム目の間の速度場（オプティカルフロー）を求める
    flow = cv2.calcOpticalFlowFarneback(prvs, next_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # 速度場を可視化
    vis = draw_flow(frame_n, flow)
    
    # (2) 1フレーム目と2フレーム目の間の速度場の結果を保存
    if n == 2:
        cv2.imwrite("velocity_field_frame2.png", vis)
        print("Saved optical flow between frame 1 and frame 2 to velocity_field_frame2.png")
    
    # 動画に書き込み
    out.write(vis)
    
    n += 1

cap.release()
out.release()
print(f"Processed up to frame {n-1}. Saved the change of velocity fields to velocity_field_changes.mp4")