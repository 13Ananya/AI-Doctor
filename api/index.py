# api/index.py
from fastapi import FastAPI
from gradio.routes import mount_gradio_app
from gradio_app import build_interface

app = FastAPI()
gradio_interface = build_interface()
app = mount_gradio_app(app, gradio_interface, path="/")