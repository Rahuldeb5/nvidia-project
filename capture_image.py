import cv2

def save_image(image, filename):
    cv2.imwrite(filename, image)
    print(f"Image saved as {filename}")

def capture_single_image():
    # Open the USB webcam
    camera = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not camera.isOpened():
        print("Error: Unable to access the webcam.")
        return

    # Wait for user input (wait for the Enter key to be pressed)
    input("Press Enter to capture an image: ")

    # Capture a frame from the webcam
    ret, frame = camera.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Unable to capture image from the webcam.")
        return

    # Save the captured frame as a .jpg image file
    image_filename = "captured_image.jpg"
    save_image(frame, image_filename)

    # Release the camera
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_single_image()