# ListOsTemplatesRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_os_templates_request_content import ListOsTemplatesRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListOsTemplatesRequestContent from a JSON string
list_os_templates_request_content_instance = ListOsTemplatesRequestContent.from_json(json)
# print the JSON string representation of the object
print(ListOsTemplatesRequestContent.to_json())

# convert the object into a dict
list_os_templates_request_content_dict = list_os_templates_request_content_instance.to_dict()
# create an instance of ListOsTemplatesRequestContent from a dict
list_os_templates_request_content_from_dict = ListOsTemplatesRequestContent.from_dict(list_os_templates_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


