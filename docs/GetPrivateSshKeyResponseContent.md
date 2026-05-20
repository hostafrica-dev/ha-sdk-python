# GetPrivateSshKeyResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PublicSshKeyResponseData**](PublicSshKeyResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_private_ssh_key_response_content import GetPrivateSshKeyResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrivateSshKeyResponseContent from a JSON string
get_private_ssh_key_response_content_instance = GetPrivateSshKeyResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetPrivateSshKeyResponseContent.to_json())

# convert the object into a dict
get_private_ssh_key_response_content_dict = get_private_ssh_key_response_content_instance.to_dict()
# create an instance of GetPrivateSshKeyResponseContent from a dict
get_private_ssh_key_response_content_from_dict = GetPrivateSshKeyResponseContent.from_dict(get_private_ssh_key_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


