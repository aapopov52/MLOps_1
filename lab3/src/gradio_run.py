import gradio as gr
import app_model


with gr.Blocks() as demo:
    with gr.Column(scale=2):
        t_p1 = gr.Text("1", label="Параметр 1")
        t_p2 = gr.Text("2", label="Параметр 2")
        t_p3 = gr.Text("3", label="Параметр 3")	
        t_p4 = gr.Text("4", label="Параметр 4")
        btn = gr.Button(value="Запуск модели")
        t_predict = gr.Text("", label="Прогноз:")

        btn.click(app_model.model_run_grad,
                  inputs=[t_p1, t_p2, t_p3, t_p4], outputs=[t_predict])


demo.launch(share=True)
