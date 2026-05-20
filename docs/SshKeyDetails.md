# SshKeyDetails

SSH key details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | The public SSH key in OpenSSH format | 
**type** | **str** | Type of SSH key configuration - &#39;sshkeys&#39; for KVM cloud-init or &#39;keypair&#39; for traditional SSH (LXC) | 

## Example

```python
from ha_sdk_python.models.ssh_key_details import SshKeyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyDetails from a JSON string
ssh_key_details_instance = SshKeyDetails.from_json(json)
# print the JSON string representation of the object
print(SshKeyDetails.to_json())

# convert the object into a dict
ssh_key_details_dict = ssh_key_details_instance.to_dict()
# create an instance of SshKeyDetails from a dict
ssh_key_details_from_dict = SshKeyDetails.from_dict(ssh_key_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


