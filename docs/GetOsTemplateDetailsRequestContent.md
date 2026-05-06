# GetOsTemplateDetailsRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**image_id** | **str** | Image identifier for the OS template | 

## Example

```python
from hostafrica_sdk_python.models.get_os_template_details_request_content import GetOsTemplateDetailsRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetOsTemplateDetailsRequestContent from a JSON string
get_os_template_details_request_content_instance = GetOsTemplateDetailsRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetOsTemplateDetailsRequestContent.to_json())

# convert the object into a dict
get_os_template_details_request_content_dict = get_os_template_details_request_content_instance.to_dict()
# create an instance of GetOsTemplateDetailsRequestContent from a dict
get_os_template_details_request_content_from_dict = GetOsTemplateDetailsRequestContent.from_dict(get_os_template_details_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


