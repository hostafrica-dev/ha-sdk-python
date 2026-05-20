# GetNoVncConsoleResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NoVncConsoleResponseData**](NoVncConsoleResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.get_no_vnc_console_response_content import GetNoVncConsoleResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetNoVncConsoleResponseContent from a JSON string
get_no_vnc_console_response_content_instance = GetNoVncConsoleResponseContent.from_json(json)
# print the JSON string representation of the object
print(GetNoVncConsoleResponseContent.to_json())

# convert the object into a dict
get_no_vnc_console_response_content_dict = get_no_vnc_console_response_content_instance.to_dict()
# create an instance of GetNoVncConsoleResponseContent from a dict
get_no_vnc_console_response_content_from_dict = GetNoVncConsoleResponseContent.from_dict(get_no_vnc_console_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


