# PublicSshKeyResponseData

Response data for public SSH key retrieval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**data** | [**SshKeyDetails**](SshKeyDetails.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.public_ssh_key_response_data import PublicSshKeyResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSshKeyResponseData from a JSON string
public_ssh_key_response_data_instance = PublicSshKeyResponseData.from_json(json)
# print the JSON string representation of the object
print(PublicSshKeyResponseData.to_json())

# convert the object into a dict
public_ssh_key_response_data_dict = public_ssh_key_response_data_instance.to_dict()
# create an instance of PublicSshKeyResponseData from a dict
public_ssh_key_response_data_from_dict = PublicSshKeyResponseData.from_dict(public_ssh_key_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


