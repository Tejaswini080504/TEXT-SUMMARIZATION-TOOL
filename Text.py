from transformers import pipeline

def summarize_text(input_text):
    # Initialize the Hugging Face transformer summarization pipeline with a smaller model
    summarizer = pipeline("summarization", model="facebook/bart-small")
    # Generate the summary using the model
    summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
    # Return the concise summary
    return summary[0]['summary_text']

if _name_ == "_main_":
    # Input lengthy article text
    print("Please enter the text you want to summarize (end with an empty line):")
    input_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        input_lines.append(line)
    
    input_text = "\n".join(input_lines)

    # Get the concise summary
    summary = summarize_text(input_text)
    
    # Output the original text and its summary
    print("\nOriginal Text:")
    print(input_text)
    print("\nConcise Summary:")
    print(summary)
