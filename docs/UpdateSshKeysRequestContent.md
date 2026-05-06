# UpdateSshKeysRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**ssh_keys** | **str** | SSH public key in OpenSSH format (must start with ssh-rsa, ssh-dss, ssh-ed25519, or ssh-ecdsa) | 

## Example

```python
from hostafrica_sdk_python.models.update_ssh_keys_request_content import UpdateSshKeysRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSshKeysRequestContent from a JSON string
update_ssh_keys_request_content_instance = UpdateSshKeysRequestContent.from_json(json)
# print the JSON string representation of the object
print(UpdateSshKeysRequestContent.to_json())

# convert the object into a dict
update_ssh_keys_request_content_dict = update_ssh_keys_request_content_instance.to_dict()
# create an instance of UpdateSshKeysRequestContent from a dict
update_ssh_keys_request_content_from_dict = UpdateSshKeysRequestContent.from_dict(update_ssh_keys_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


