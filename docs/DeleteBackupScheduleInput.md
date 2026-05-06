# DeleteBackupScheduleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**schedule_id** | **str** | Backup schedule ID to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_backup_schedule_input import DeleteBackupScheduleInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupScheduleInput from a JSON string
delete_backup_schedule_input_instance = DeleteBackupScheduleInput.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupScheduleInput.to_json())

# convert the object into a dict
delete_backup_schedule_input_dict = delete_backup_schedule_input_instance.to_dict()
# create an instance of DeleteBackupScheduleInput from a dict
delete_backup_schedule_input_from_dict = DeleteBackupScheduleInput.from_dict(delete_backup_schedule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


