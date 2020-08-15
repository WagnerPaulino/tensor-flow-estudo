FROM tensorflow/tensorflow:latest-gpu-jupyter
COPY . .
RUN pip install -r requirements.txt
CMD jupyter notebook --allow-root