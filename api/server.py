import grpc
from concurrent import futures
import sys

# List of paths to add
paths = ['../proto']

sys.path.extend(paths)

from core.langchain_interface import generate_langchain_response  # Assumed to be part of your LangChain logic
from proto.langchain_service_pb2 import QueryResponse
from proto.langchain_service_pb2_grpc import LangChainServiceServicer, add_LangChainServiceServicer_to_server


class LangChainServicer(LangChainServiceServicer):
    def GenerateResponse(self, request, context):
        # Use LangChain to process the query and generate a response
        query = request.query
        response = generate_langchain_response(query)
        return QueryResponse(response=response)


def serve():
    # Initialize the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_LangChainServiceServicer_to_server(LangChainServicer(), server)
    server.add_insecure_port('[::]:50051')  # Bind to port 50051
    server.start()
    print("gRPC server is running on port 50051...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
