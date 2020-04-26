docker build --build-arg RUN_FILE=classificacao_texto_preprocessado.py -t tensor-flow-estudo .
docker rm -f tensor
docker run --name tensor tensor-flow-estudo
docker logs -f tensor