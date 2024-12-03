import gradio as gr

def step1(input_text):
    return input_text.upper()

def step2(processed_text):
    return f"Reversed: {processed_text[::-1]}"

with gr.Blocks() as demo:
    input_text = gr.Textbox(label="Input Text")
    final_output = gr.Textbox(label="Final Output")
    
    # Combine both steps into a single flow
    step_chain = gr.Button("Run All")
    step_chain.click(lambda text: step2(step1(text)), inputs=input_text, outputs=final_output)

demo.launch()
