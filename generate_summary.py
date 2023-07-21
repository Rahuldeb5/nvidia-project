from transformers import pipeline

def summarize_text(input_file, output_file):
    # Read input text from the file
    with open(input_file, "r") as f:
        input_text = f.read()

    # Load the pre-trained summarization model
    summarizer = pipeline("summarization")

    # Use the model to summarize the input text
    summarized_text = summarizer(input_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

    # Save the summarized text to the output file
    with open(output_file, "w") as f:
        f.write(summarized_text)

if __name__ == "__main__":
    input_file = "/home/nvidia/my_project/captured_text.txt"  # Replace with the path to your input text file
    output_file = "/home/nvidia/my_project/text_summary.txt"  # Replace with the desired path for the output summary file
    summarize_text(input_file, output_file)
