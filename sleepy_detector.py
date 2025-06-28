import cv2
import mediapipe as mp
import winsound
import math

# Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Fungsi jarak
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Indeks mata dan mulut
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
MOUTH_TOP = 13
MOUTH_BOTTOM = 14
MOUTH_LEFT = 78
MOUTH_RIGHT = 308

EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.6
SLEEP_FRAMES = 30
YAWN_FRAMES = 15

sleep_counter = 0
yawn_counter = 0

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face in result.multi_face_landmarks:
            lm = face.landmark

            # Eye Aspect Ratio (EAR)
            left_ear = (dist(lm[385], lm[380]) + dist(lm[387], lm[373])) / (2 * dist(lm[362], lm[263]))
            right_ear = (dist(lm[160], lm[144]) + dist(lm[158], lm[153])) / (2 * dist(lm[33], lm[133]))
            ear = (left_ear + right_ear) / 2

            # Mouth Aspect Ratio (MAR)
            mar = dist(lm[MOUTH_TOP], lm[MOUTH_BOTTOM]) / dist(lm[MOUTH_LEFT], lm[MOUTH_RIGHT])

            # Tampilkan nilai
            cv2.putText(frame, f'EAR: {ear:.2f}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
            cv2.putText(frame, f'MAR: {mar:.2f}', (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

            # Deteksi kantuk
            if ear < EAR_THRESHOLD:
                sleep_counter += 1
            else:
                sleep_counter = 0

            if sleep_counter > SLEEP_FRAMES:
                cv2.putText(frame, "ALERT: MENGANTUK!", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
                winsound.Beep(1000, 500)

            # Deteksi menguap
            if mar > MAR_THRESHOLD:
                yawn_counter += 1
            else:
                yawn_counter = 0

            if yawn_counter > YAWN_FRAMES:
                cv2.putText(frame, "ALERT: MENGUAP!", (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
                winsound.Beep(800, 500)

    cv2.imshow("Deteksi Kantuk + Menguap", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
