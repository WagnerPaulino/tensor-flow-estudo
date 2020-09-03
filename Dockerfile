FROM tensorflow/tensorflow:latest-gpu-jupyter
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD jupyter notebook --allow-root
