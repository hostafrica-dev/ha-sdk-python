# GetPrivateSshKeyOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**PublicSshKeyResponseData**](PublicSshKeyResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_private_ssh_key_output import GetPrivateSshKeyOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrivateSshKeyOutput from a JSON string
get_private_ssh_key_output_instance = GetPrivateSshKeyOutput.from_json(json)
# print the JSON string representation of the object
print(GetPrivateSshKeyOutput.to_json())

# convert the object into a dict
get_private_ssh_key_output_dict = get_private_ssh_key_output_instance.to_dict()
# create an instance of GetPrivateSshKeyOutput from a dict
get_private_ssh_key_output_from_dict = GetPrivateSshKeyOutput.from_dict(get_private_ssh_key_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


