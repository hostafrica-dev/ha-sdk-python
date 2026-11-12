# ModifyPrivateNameserverRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**nameserver** | **str** | Existing child nameserver hostname to modify | 
**new_nameserver** | **str** | New hostname; unsupported for some registrars (COZA/COCCA) | [optional] 
**old_ip_address** | **str** | Current glue IP when the registrar requires it | [optional] 
**new_ip_address** | **str** | New glue IPv4 or IPv6 address | [optional] 

## Example

```python
from ha_sdk_python.models.modify_private_nameserver_request_content import ModifyPrivateNameserverRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyPrivateNameserverRequestContent from a JSON string
modify_private_nameserver_request_content_instance = ModifyPrivateNameserverRequestContent.from_json(json)
# print the JSON string representation of the object
print(ModifyPrivateNameserverRequestContent.to_json())

# convert the object into a dict
modify_private_nameserver_request_content_dict = modify_private_nameserver_request_content_instance.to_dict()
# create an instance of ModifyPrivateNameserverRequestContent from a dict
modify_private_nameserver_request_content_from_dict = ModifyPrivateNameserverRequestContent.from_dict(modify_private_nameserver_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


