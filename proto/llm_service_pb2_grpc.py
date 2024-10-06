# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from proto import llm_service_pb2 as llm__service__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in llm_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LLMServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateText = channel.unary_stream(
                '/llm.LLMService/GenerateText',
                request_serializer=llm__service__pb2.TextRequest.SerializeToString,
                response_deserializer=llm__service__pb2.TextResponse.FromString,
                _registered_method=True)
        self.HealthCheck = channel.unary_unary(
                '/llm.LLMService/HealthCheck',
                request_serializer=llm__service__pb2.HealthCheckRequest.SerializeToString,
                response_deserializer=llm__service__pb2.HealthCheckResponse.FromString,
                _registered_method=True)


class LLMServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HealthCheck(self, request, context):
        """Health check method
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LLMServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateText': grpc.unary_stream_rpc_method_handler(
                    servicer.GenerateText,
                    request_deserializer=llm__service__pb2.TextRequest.FromString,
                    response_serializer=llm__service__pb2.TextResponse.SerializeToString,
            ),
            'HealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=llm__service__pb2.HealthCheckRequest.FromString,
                    response_serializer=llm__service__pb2.HealthCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'llm.LLMService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('llm.LLMService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LLMService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/llm.LLMService/GenerateText',
            llm__service__pb2.TextRequest.SerializeToString,
            llm__service__pb2.TextResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def HealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/llm.LLMService/HealthCheck',
            llm__service__pb2.HealthCheckRequest.SerializeToString,
            llm__service__pb2.HealthCheckResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
