

import grpc
from concurrent import futures

# Import the generated classes from the updated proto files
from proto import llm_service_pb2_grpc as llm_grpc
from proto import llm_service_pb2 as llm_pb2

# Import your LLM logic (this is assumed to be implemented somewhere in your project)
from core.llmservice import generate_llm_response  # Assumed to be part of your LLM SERVICE logic


class LLMServicer(llm_grpc.LLMServiceServicer):
    def GenerateText(self, request, context):
        input_text = request.input_text

        # Get the streamed response from OpenAI's API
        for response_chunk in generate_llm_response(input_text):
            yield llm_pb2.TextResponse(generated_text=response_chunk)

    def HealthCheck(self, request, context):
        return llm_pb2.HealthCheckResponse(status="Healthy")

def serve():
    # Initialize the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    llm_grpc.add_LLMServiceServicer_to_server(LLMServicer(), server)
    server.add_insecure_port('[::]:50051')  # Bind to port 50051
    server.start()
    print("gRPC server is running on port 50051...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
