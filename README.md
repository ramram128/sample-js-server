sending_data :
      This file is only used to represent the camera, sending data to the server like a real camera would.

      
py_server :
      It receives multipart-form JSON data (mimicking a camera or external device), processes it, and sends the extracted JSON to a secondary service (listening on port 9090) for further handling.
      This setup is useful for applications where multiple services need to interact with and process JSON data sequentially.

js_server :
    This script listens for JSON data on port 9090, extracts specific information (a name field), and returns it. 
    This setup could be part of a pipeline where data from an initial request is processed to identify specific fields for further action.
    split method is simple but we can't use data again . but this type we can use data in future.
