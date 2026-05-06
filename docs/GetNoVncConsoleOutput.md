# GetNoVncConsoleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**NoVncConsoleResponseData**](NoVncConsoleResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.get_no_vnc_console_output import GetNoVncConsoleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GetNoVncConsoleOutput from a JSON string
get_no_vnc_console_output_instance = GetNoVncConsoleOutput.from_json(json)
# print the JSON string representation of the object
print(GetNoVncConsoleOutput.to_json())

# convert the object into a dict
get_no_vnc_console_output_dict = get_no_vnc_console_output_instance.to_dict()
# create an instance of GetNoVncConsoleOutput from a dict
get_no_vnc_console_output_from_dict = GetNoVncConsoleOutput.from_dict(get_no_vnc_console_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


