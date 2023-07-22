import cv2

def set_camera_properties(camera):
    # Increase brightness and contrast (you can adjust these values as needed)
    camera.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
    camera.set(cv2.CAP_PROP_CONTRAST, 0.5)

def save_image(image, filename):
    cv2.imwrite(filename, image)
    print(f"Image saved as {filename}")

def capture_images():
    while True:
        # Open the USB webcam inside the loop to reinitialize for each capture
        camera = cv2.VideoCapture(0)

        # Check if the camera is opened successfully
        if not camera.isOpened():
            print("Error: Unable to access the webcam.")
            return

        # Set camera properties for better brightness
        set_camera_properties(camera)

        # Wait for user input (y or n to continue capturing)
        user_input = input("Do you want to capture an image? (y/n): ").lower()

        if user_input == 'y':
            # Capture a frame from the webcam
            ret, frame = camera.read()

            # Check if the frame was captured successfully
            if not ret:
                print("Error: Unable to capture image from the webcam.")
                camera.release()  # Release the camera before continuing
                continue

            # Specify the full path to save the image inside "/home/nvidia/my_project/"
            image_filename = "/home/nvidia/my_project/captured_image.jpg"

            # Save the captured frame as a .jpg image file (overwriting the same file each time)
            save_image(frame, image_filename)

        elif user_input == 'n':
            # Release the camera before exiting the loop
            camera.release()
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

        # Release the camera before continuing to the next iteration
        camera.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()
