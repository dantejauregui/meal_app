import os

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2

channel = ClarifaiChannel.get_json_channel()
channel = ClarifaiChannel.get_insecure_grpc_channel()

stub = service_pb2_grpc.V2Stub(channel)
key = os.getenv('API_KEY')

metadata = (('authorization', f'Key {key}'),)

def classification(img):
    #with open(img, "rb") as f:
    file_bytes = img.read()

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            model_id="bd367be194cf45149e75f01d59f77ba7",
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=file_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )

    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    output = post_model_outputs_response.outputs[0]

    consolidate = []
    print("Predicted concepts:")
    for concept in output.data.concepts:
        #print("%s %.2f" % (concept.name, concept.value))
        consolidate.append( (concept.name, concept.value) )

    return consolidate

#solucion = classification()
#print(solucion)