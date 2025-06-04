import gradio as gr

def handle_checkbox(selected):
    if selected:
        return "동의했습니다!"  # 변경값이 ture 인 경우 출력
    return "동의하지 않았습니다!" # 변경값이 false 인 경우 출력

with gr.Blocks() as demo:
    checkbox = gr.Checkbox(label='개인정보 사용에 동의하겠습니까?')
    output_checkbox = gr.Textbox(label='출력')
    checkbox.change(handle_checkbox, inputs=checkbox, outputs=output_checkbox)

demo.launch()