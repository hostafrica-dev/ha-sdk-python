# GetPrivateSshKeyRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.get_private_ssh_key_request_content import GetPrivateSshKeyRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrivateSshKeyRequestContent from a JSON string
get_private_ssh_key_request_content_instance = GetPrivateSshKeyRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetPrivateSshKeyRequestContent.to_json())

# convert the object into a dict
get_private_ssh_key_request_content_dict = get_private_ssh_key_request_content_instance.to_dict()
# create an instance of GetPrivateSshKeyRequestContent from a dict
get_private_ssh_key_request_content_from_dict = GetPrivateSshKeyRequestContent.from_dict(get_private_ssh_key_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


