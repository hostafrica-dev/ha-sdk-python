# ListReinstallOsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from ha_sdk_python.models.list_reinstall_os_request_content import ListReinstallOsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListReinstallOsRequestContent from a JSON string
list_reinstall_os_request_content_instance = ListReinstallOsRequestContent.from_json(json)
# print the JSON string representation of the object
print(ListReinstallOsRequestContent.to_json())

# convert the object into a dict
list_reinstall_os_request_content_dict = list_reinstall_os_request_content_instance.to_dict()
# create an instance of ListReinstallOsRequestContent from a dict
list_reinstall_os_request_content_from_dict = ListReinstallOsRequestContent.from_dict(list_reinstall_os_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


