FROM tensorflow/tensorflow:latest-gpu-jupyter
ARG RUN_FILE=primeiro_contato_tensor_flow.py
ENV FILE_NAME=$RUN_FILE
COPY . .
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
CMD python $FILE_NAME