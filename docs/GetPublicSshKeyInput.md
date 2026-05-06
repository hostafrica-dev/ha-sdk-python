# GetPublicSshKeyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.get_public_ssh_key_input import GetPublicSshKeyInput

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicSshKeyInput from a JSON string
get_public_ssh_key_input_instance = GetPublicSshKeyInput.from_json(json)
# print the JSON string representation of the object
print(GetPublicSshKeyInput.to_json())

# convert the object into a dict
get_public_ssh_key_input_dict = get_public_ssh_key_input_instance.to_dict()
# create an instance of GetPublicSshKeyInput from a dict
get_public_ssh_key_input_from_dict = GetPublicSshKeyInput.from_dict(get_public_ssh_key_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


