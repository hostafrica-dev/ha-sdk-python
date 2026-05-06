# ListReinstallOsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_reinstall_os_input import ListReinstallOsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListReinstallOsInput from a JSON string
list_reinstall_os_input_instance = ListReinstallOsInput.from_json(json)
# print the JSON string representation of the object
print(ListReinstallOsInput.to_json())

# convert the object into a dict
list_reinstall_os_input_dict = list_reinstall_os_input_instance.to_dict()
# create an instance of ListReinstallOsInput from a dict
list_reinstall_os_input_from_dict = ListReinstallOsInput.from_dict(list_reinstall_os_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


