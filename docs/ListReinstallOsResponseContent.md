# ListReinstallOsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListReinstallOsResponseData**](ListReinstallOsResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_reinstall_os_response_content import ListReinstallOsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListReinstallOsResponseContent from a JSON string
list_reinstall_os_response_content_instance = ListReinstallOsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListReinstallOsResponseContent.to_json())

# convert the object into a dict
list_reinstall_os_response_content_dict = list_reinstall_os_response_content_instance.to_dict()
# create an instance of ListReinstallOsResponseContent from a dict
list_reinstall_os_response_content_from_dict = ListReinstallOsResponseContent.from_dict(list_reinstall_os_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


