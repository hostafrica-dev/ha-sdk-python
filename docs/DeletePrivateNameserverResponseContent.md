# DeletePrivateNameserverResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PrivateNameserverMutationData**](PrivateNameserverMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.delete_private_nameserver_response_content import DeletePrivateNameserverResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePrivateNameserverResponseContent from a JSON string
delete_private_nameserver_response_content_instance = DeletePrivateNameserverResponseContent.from_json(json)
# print the JSON string representation of the object
print(DeletePrivateNameserverResponseContent.to_json())

# convert the object into a dict
delete_private_nameserver_response_content_dict = delete_private_nameserver_response_content_instance.to_dict()
# create an instance of DeletePrivateNameserverResponseContent from a dict
delete_private_nameserver_response_content_from_dict = DeletePrivateNameserverResponseContent.from_dict(delete_private_nameserver_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


