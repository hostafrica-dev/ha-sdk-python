# ListReinstallOsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListReinstallOsResponseData**](ListReinstallOsResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_reinstall_os_output import ListReinstallOsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListReinstallOsOutput from a JSON string
list_reinstall_os_output_instance = ListReinstallOsOutput.from_json(json)
# print the JSON string representation of the object
print(ListReinstallOsOutput.to_json())

# convert the object into a dict
list_reinstall_os_output_dict = list_reinstall_os_output_instance.to_dict()
# create an instance of ListReinstallOsOutput from a dict
list_reinstall_os_output_from_dict = ListReinstallOsOutput.from_dict(list_reinstall_os_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


