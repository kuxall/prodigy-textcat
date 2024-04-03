import spacy
import gradio as gr

# Load the trained model
model_path = "/home/kushal/Documents/textcat/2023-02-27_textcat_model/model-best"
nlp = spacy.load(model_path)

# Define the function to classify text
def classify_text(text):
    doc = nlp(text)
    labels, scores = zip(*doc.cats.items())
    result = {}
    for label, score in zip(labels, scores):
        result[label] = score
    return result

# Create the Gradio interface
input_text = gr.inputs.Textbox(lines=5, label="Input Text")
output_text = gr.outputs.Label(num_top_classes=4)
interface = gr.Interface(fn=classify_text, inputs=input_text, outputs=output_text)

# Launch the interface
interface.launch(share=True)
