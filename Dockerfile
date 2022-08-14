FROM python:3.9.11

# Install default requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install PyTorch module.
RUN pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio===0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

# Install requirements for the Yolov5x6 reCAPTCHA solver.
COPY requirements_yolov5x6.txt .
RUN pip install -r requirements_yolov5x6.txt

ENTRYPOINT ["python", "main.py"]
