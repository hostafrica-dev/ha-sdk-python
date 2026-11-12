# DeletePrivateNameserverRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id - must be sent as a string | 
**nameserver** | **str** | Child nameserver hostname to delete | 

## Example

```python
from ha_sdk_python.models.delete_private_nameserver_request_content import DeletePrivateNameserverRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePrivateNameserverRequestContent from a JSON string
delete_private_nameserver_request_content_instance = DeletePrivateNameserverRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeletePrivateNameserverRequestContent.to_json())

# convert the object into a dict
delete_private_nameserver_request_content_dict = delete_private_nameserver_request_content_instance.to_dict()
# create an instance of DeletePrivateNameserverRequestContent from a dict
delete_private_nameserver_request_content_from_dict = DeletePrivateNameserverRequestContent.from_dict(delete_private_nameserver_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


