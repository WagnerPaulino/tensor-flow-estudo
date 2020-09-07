FROM tensorflow/tensorflow:latest-gpu-jupyter
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
COPY kaggle.json /root/.kaggle/kaggle.json
RUN chmod 600 /root/.kaggle/kaggle.json
CMD jupyter notebook --allow-root
