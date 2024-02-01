import cv2

def display_camera_stream(url):
    cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
            break

        cv2.imshow('Camera Stream', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_url = "https://video.raciborz24.pl/hls/rondo.m3u8"
    display_camera_stream(camera_url)
