docker build --build-arg RUN_FILE=primeira_rede_neural_tensor_flow.py -t tensor-flow-estudo .
docker rm -f tensor
docker run --name tensor tensor-flow-estudo
docker logs -f tensor