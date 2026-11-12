# RegisterPrivateNameserverResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PrivateNameserverMutationData**](PrivateNameserverMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.register_private_nameserver_response_content import RegisterPrivateNameserverResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterPrivateNameserverResponseContent from a JSON string
register_private_nameserver_response_content_instance = RegisterPrivateNameserverResponseContent.from_json(json)
# print the JSON string representation of the object
print(RegisterPrivateNameserverResponseContent.to_json())

# convert the object into a dict
register_private_nameserver_response_content_dict = register_private_nameserver_response_content_instance.to_dict()
# create an instance of RegisterPrivateNameserverResponseContent from a dict
register_private_nameserver_response_content_from_dict = RegisterPrivateNameserverResponseContent.from_dict(register_private_nameserver_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


