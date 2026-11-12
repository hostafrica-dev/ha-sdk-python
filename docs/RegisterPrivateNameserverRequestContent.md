# RegisterPrivateNameserverRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**nameserver** | **str** | Full child nameserver hostname (e.g. ns1.example.com) | 
**ip_address** | **str** | Glue IPv4 or IPv6 address for the nameserver | 

## Example

```python
from ha_sdk_python.models.register_private_nameserver_request_content import RegisterPrivateNameserverRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterPrivateNameserverRequestContent from a JSON string
register_private_nameserver_request_content_instance = RegisterPrivateNameserverRequestContent.from_json(json)
# print the JSON string representation of the object
print(RegisterPrivateNameserverRequestContent.to_json())

# convert the object into a dict
register_private_nameserver_request_content_dict = register_private_nameserver_request_content_instance.to_dict()
# create an instance of RegisterPrivateNameserverRequestContent from a dict
register_private_nameserver_request_content_from_dict = RegisterPrivateNameserverRequestContent.from_dict(register_private_nameserver_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


