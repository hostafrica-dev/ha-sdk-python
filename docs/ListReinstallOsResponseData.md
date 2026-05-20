# ListReinstallOsResponseData

Response data for reinstall list OS operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**templates** | **List[str]** | List of available OS templates | 

## Example

```python
from ha_sdk_python.models.list_reinstall_os_response_data import ListReinstallOsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListReinstallOsResponseData from a JSON string
list_reinstall_os_response_data_instance = ListReinstallOsResponseData.from_json(json)
# print the JSON string representation of the object
print(ListReinstallOsResponseData.to_json())

# convert the object into a dict
list_reinstall_os_response_data_dict = list_reinstall_os_response_data_instance.to_dict()
# create an instance of ListReinstallOsResponseData from a dict
list_reinstall_os_response_data_from_dict = ListReinstallOsResponseData.from_dict(list_reinstall_os_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


