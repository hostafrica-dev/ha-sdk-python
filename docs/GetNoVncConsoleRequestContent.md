# GetNoVncConsoleRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.get_no_vnc_console_request_content import GetNoVncConsoleRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetNoVncConsoleRequestContent from a JSON string
get_no_vnc_console_request_content_instance = GetNoVncConsoleRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetNoVncConsoleRequestContent.to_json())

# convert the object into a dict
get_no_vnc_console_request_content_dict = get_no_vnc_console_request_content_instance.to_dict()
# create an instance of GetNoVncConsoleRequestContent from a dict
get_no_vnc_console_request_content_from_dict = GetNoVncConsoleRequestContent.from_dict(get_no_vnc_console_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


