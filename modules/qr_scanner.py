import cv2
from pyzbar import pyzbar
import ctypes
import pygetwindow as gw
import win32gui
import win32con

def read_qr_code(page):
    page.go('/loading')
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Get screen resolution
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # Create a named window with fullscreen flag
    cv2.namedWindow("QR Code Scanner", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("QR Code Scanner", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    

    while True:
        # Read frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect QR codes in the frame
        qr_codes = pyzbar.decode(gray)

        # Loop over detected QR codes
        for qr_code in qr_codes:
            # Extract the decoded data
            data = qr_code.data.decode("utf-8")
            print("Decoded data:", data)

            # Close the camera window
            cv2.destroyAllWindows()
            cap.release()
            page.go('/menu')
            return data

        # Display the frame with QR code detection
        cv2.imshow("QR Code Scanner", frame)

        hWnd = win32gui.FindWindow(None, 'QR Code Scanner')
        win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    # Close the camera window
    cv2.destroyAllWindows()
    cap.release()
    page.go('/menu')

