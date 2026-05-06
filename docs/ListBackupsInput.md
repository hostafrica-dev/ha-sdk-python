# ListBackupsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_backups_input import ListBackupsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListBackupsInput from a JSON string
list_backups_input_instance = ListBackupsInput.from_json(json)
# print the JSON string representation of the object
print(ListBackupsInput.to_json())

# convert the object into a dict
list_backups_input_dict = list_backups_input_instance.to_dict()
# create an instance of ListBackupsInput from a dict
list_backups_input_from_dict = ListBackupsInput.from_dict(list_backups_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


