


#### **Project Setup for LangChain with gRPC**

This document provides step-by-step instructions on how to set up the development environment, manage dependencies, generate gRPC files, and run the gRPC server for LangChain-based AI projects.

---

### ** Commands**

1. Activate venv
```bash
. venv\scripts\activate
```

Start Server
```bash
python server.py
```

2. Generate grpc proto files
```bash
python -m grpc_tools.protoc -I=proto/ --python_out=./proto --grpc_python_out=./proto proto/llm_service.proto
```

3. When generating modify the llm_service_pb2.py file to import the correct path
```bash
from proto import llm_service_pb2 as llm__service__pb2
```

3. 






