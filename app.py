import gradio as gr
from script import predict_ceo_approval

def classify(image, description):
    return predict_ceo_approval(image, description)

with gr.Blocks() as demo:
    gr.Markdown("# 👔 CEO Approval Classifier")

    with gr.Row():
        image_input = gr.Image(type="filepath", label="Upload Image")
        text_input = gr.Textbox(label="Or enter a description")

    result = gr.Label(label="CEO Verdict")

    btn = gr.Button("Check Approval")
    btn.click(fn=classify, inputs=[image_input, text_input], outputs=result)

demo.launch()
