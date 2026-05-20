# GetPublicSshKeyResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PublicSshKeyResponseData**](PublicSshKeyResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_public_ssh_key_response_content import GetPublicSshKeyResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicSshKeyResponseContent from a JSON string
get_public_ssh_key_response_content_instance = GetPublicSshKeyResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetPublicSshKeyResponseContent.to_json())

# convert the object into a dict
get_public_ssh_key_response_content_dict = get_public_ssh_key_response_content_instance.to_dict()
# create an instance of GetPublicSshKeyResponseContent from a dict
get_public_ssh_key_response_content_from_dict = GetPublicSshKeyResponseContent.from_dict(get_public_ssh_key_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


