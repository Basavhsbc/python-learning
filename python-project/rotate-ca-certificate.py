from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from google.oauth2 import service_account
import os

# instances_rotate_server_ca_request_body = {
#   "rotateServerCaContext": {
#     "kind": "sql#rotateServerCaContext",
#     "nextVersion": ""
#   }
# }
# request = service.instances().rotateServerCa(project=project, instance=instance, body=instances_rotate_server_ca_request_body)
# response = request.execute()
# TODO: Change code below to process the `response` dict:
# version_to_rotate=response["activeVersion"]
# pprint(version_to_rotate)
# To rotate server ca

def list_server_certificate(project, instance):
    '''
    This function accepts a nested dictionary as argument
    and iterate over all values of nested dictionaries
    '''
    # To list server certificates from cloud sql instance database.
    request = service.instances().listServerCas(project=project, instance=instance)
    # request = service.instances().addServerCa(project=project, instance=instance)
    response = request.execute()
    sha = []
    my_dict={}
    for key, value in response.items():
        # Check if value is of dict type
        # pprint("Inside first for loop..!")
        # Define empty list to store "sha1Fingerprint" value
        if isinstance(value, list):
            for item in value:
                if isinstance(item,dict):
                    # sha.append(item["sha1Fingerprint"])
                    my_dict[item["sha1Fingerprint"]]=item["createTime"]
            # pprint(sha)
            # If value is dict then iterate over all its values
            # for pair in nested_dict_pairs_iterator(value):
            #     pprint(f" {pair}")
        else:
            # To print other key and value from dictionary !!
            if key=="activeVersion":
                result=value

    for k,v in my_dict.items():
        if k == result:
            pprint(f"{k} : {v}")

if __name__ == '__main__':
    # Below parameter required to make call to google apis via google discovery builder.
    scopes = ['https://www.googleapis.com/auth/cloud-platform']
    sa_file = "service-account.json"
    credentials = service_account.Credentials.from_service_account_file(sa_file, scopes=scopes)
    service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="igneous-mason-306611-18e3d5ea00a2.json"
    # Project ID of the project that contains the instance.
    project = 'igneous-mason-306611'  # TODO: Update placeholder value.
    # Cloud SQL instance ID. This does not include the project ID.
    instance = 'tls-certificate-instance'  # TODO: Update placeholder value.
    # Call list_server_certificates() function to check if active certificate cross 335 days
    list_server_certificate(project, instance)
