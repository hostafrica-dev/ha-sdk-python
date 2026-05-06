# GetPublicSshKeyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PublicSshKeyResponseData**](PublicSshKeyResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_public_ssh_key_output import GetPublicSshKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicSshKeyOutput from a JSON string
get_public_ssh_key_output_instance = GetPublicSshKeyOutput.from_json(json)
# print the JSON string representation of the object
print(GetPublicSshKeyOutput.to_json())

# convert the object into a dict
get_public_ssh_key_output_dict = get_public_ssh_key_output_instance.to_dict()
# create an instance of GetPublicSshKeyOutput from a dict
get_public_ssh_key_output_from_dict = GetPublicSshKeyOutput.from_dict(get_public_ssh_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


