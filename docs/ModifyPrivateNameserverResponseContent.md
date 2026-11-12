# ModifyPrivateNameserverResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ModifyPrivateNameserverData**](ModifyPrivateNameserverData.md) |  | 

## Example

```python
from ha_sdk_python.models.modify_private_nameserver_response_content import ModifyPrivateNameserverResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPrivateNameserverResponseContent from a JSON string
modify_private_nameserver_response_content_instance = ModifyPrivateNameserverResponseContent.from_json(json)
# print the JSON string representation of the object
print(ModifyPrivateNameserverResponseContent.to_json())

# convert the object into a dict
modify_private_nameserver_response_content_dict = modify_private_nameserver_response_content_instance.to_dict()
# create an instance of ModifyPrivateNameserverResponseContent from a dict
modify_private_nameserver_response_content_from_dict = ModifyPrivateNameserverResponseContent.from_dict(modify_private_nameserver_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


