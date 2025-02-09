!pip install transformers
!pip install torch
from transformers import pipeline
def summarize_text(input_text):
    # Initialize the Hugging Face transformer summarization pipeline
    summarizer = pipeline("summarization")

    # Generate the summary using the model
    summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)

    # Return the concise summary
    return summary[0]['summary_text']

if __name__ == "__main__":
    # Input lengthy article text
    input_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.
    Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving". As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.
    The term "artificial intelligence" had been used to describe machines that could perform any task a human could perform, such as problem-solving, pattern recognition, and understanding natural language. The field of AI research was founded at a conference in 1956 at Dartmouth College in Hanover, New Hampshire, where the term was first coined.
    Early AI research focused on symbolic methods and problem-solving, and the goal was to simulate the way humans think. As AI has advanced, many different methods of artificial intelligence have emerged, including machine learning, deep learning, neural networks, and natural language processing.
    """

    # Get the concise summary
    summary = summarize_text(input_text)

    # Output the original text and its summary
    print("Original Text:")
    print(input_text)
    print("\nConcise Summary:")
    print(summary)
