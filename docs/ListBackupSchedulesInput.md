# ListBackupSchedulesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_backup_schedules_input import ListBackupSchedulesInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListBackupSchedulesInput from a JSON string
list_backup_schedules_input_instance = ListBackupSchedulesInput.from_json(json)
# print the JSON string representation of the object
print(ListBackupSchedulesInput.to_json())

# convert the object into a dict
list_backup_schedules_input_dict = list_backup_schedules_input_instance.to_dict()
# create an instance of ListBackupSchedulesInput from a dict
list_backup_schedules_input_from_dict = ListBackupSchedulesInput.from_dict(list_backup_schedules_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


