import cv2
import pytesseract

def perform_text_recognition(image_filename, text_filename):
    # Read the captured image
    image = cv2.imread(image_filename)

    # Apply image preprocessing (resizing and converting to grayscale)
    preprocessed_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    preprocessed_image = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2GRAY)

    # Perform text recognition using Pytesseract with adjusted parameters
    recognized_text = pytesseract.image_to_string(
        preprocessed_image,
        lang='eng',               # Specify the language (English in this case)
        config='--psm 6'          # Adjust page segmentation mode (PSM)
    )

    # Save the recognized text in a new text file in the specified directory
    text_file_path = "/home/nvidia/my_project/" + text_filename
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(recognized_text)
    print(f"Recognized text saved in {text_file_path}")

if __name__ == "__main__":
    # Specify the filename of the captured image
    image_filename = "/home/nvidia/my_project/captured_image.jpg"
    # Specify the filename for the text output
    text_filename = "/home/nvidia/my_project/captured_text.txt"

    # Perform text recognition on the captured image and save the result in the text file
    perform_text_recognition(image_filename, text_filename)
