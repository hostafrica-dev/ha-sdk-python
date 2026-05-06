# NoVncConsoleResponseData

Response data for noVNC console operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**console** | [**NoVncConsoleDetails**](NoVncConsoleDetails.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.no_vnc_console_response_data import NoVncConsoleResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of NoVncConsoleResponseData from a JSON string
no_vnc_console_response_data_instance = NoVncConsoleResponseData.from_json(json)
# print the JSON string representation of the object
print(NoVncConsoleResponseData.to_json())

# convert the object into a dict
no_vnc_console_response_data_dict = no_vnc_console_response_data_instance.to_dict()
# create an instance of NoVncConsoleResponseData from a dict
no_vnc_console_response_data_from_dict = NoVncConsoleResponseData.from_dict(no_vnc_console_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


