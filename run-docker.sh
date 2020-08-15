docker build -t tensor-flow-estudo .
docker rm -f tensor
docker run -p 8888:8888 --network host --name tensor tensor-flow-estudo