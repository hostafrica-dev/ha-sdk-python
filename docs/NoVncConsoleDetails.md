# NoVncConsoleDetails

noVNC console connection details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**novnc_redirect_url** | **str** | Redirect URL for the noVNC console | 

## Example

```python
from ha_sdk_python.models.no_vnc_console_details import NoVncConsoleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NoVncConsoleDetails from a JSON string
no_vnc_console_details_instance = NoVncConsoleDetails.from_json(json)
# print the JSON string representation of the object
print(NoVncConsoleDetails.to_json())

# convert the object into a dict
no_vnc_console_details_dict = no_vnc_console_details_instance.to_dict()
# create an instance of NoVncConsoleDetails from a dict
no_vnc_console_details_from_dict = NoVncConsoleDetails.from_dict(no_vnc_console_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


