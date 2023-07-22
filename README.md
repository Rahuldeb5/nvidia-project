# TextScan Summary Generator

This project combines image-to-text conversion, text summarization, and digitalize documents This system enables users to extract insights, generate concise summaries, and digitize documents for enhanced productivity and information retrieval.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The image showcases the Visual Studio Code (VSCode) interface, connected to a Jetson Nano device via SSH. In the VSCode window, three tabs are open:
1) The first tab displays an image, captured using a webcam.
2) In the second tab, there is a text-recognition file and it was responsible for extracting text from the captured image.
3) The third tab shows a summary generated using the contents of the text recognition file.
![image](https://github.com/Rahuldeb5/nvidia_project/assets/110701518/844a0e0a-7993-49f7-968a-e6be06374997)

## The Algorithm

The first file, capture_image.py utilizes the OpenCV library to interact with a USB webcam and capture images.
![image](https://github.com/Rahuldeb5/nvidia_project/assets/110701518/204c8d4c-1b1b-49b5-8639-e9ae2d9a4887)


The second file, text_recognition.py involves reading the image, preprocessing it to optimize OCR accuracy, and then utilizing the Pytesseract library to interact with the Tesseract OCR engine to perform the text recognition process. The extracted text is finally saved in a text file.
![image](https://github.com/Rahuldeb5/nvidia_project/assets/110701518/2e8fa729-1af9-48a4-b80b-bb000a2a3cb2)


The third file, generate_summary.py uses a pre-trained model from the Transformers library to perform text summarization. It reads input text from a file, processes it through the summarization model, and saves the resulting summary in another file.
![image](https://github.com/Rahuldeb5/nvidia_project/assets/110701518/d9058b5b-fe97-41be-b474-afbd65202a73)


## Running this project

Steps to run:
1) Run capture_image.py and input 'y' to capture a frame from the webcam. The frame will be saved in captured_image.jpg.
2) Run text_recognition.py. This will run text recognition on captured_image.jpg and save the text to captured_text.txt.
3) Run generate_summary.py. This will use the transformers module to summarize the text in captured_text.txt and upload the summary to text_summary.txt.

Required libraries: CV2, Pytesseract, Transformers

[[[View a video explanation here]([video link](https://youtu.be/1-qha4tH1B0))]
