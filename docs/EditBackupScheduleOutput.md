# EditBackupScheduleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.edit_backup_schedule_output import EditBackupScheduleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EditBackupScheduleOutput from a JSON string
edit_backup_schedule_output_instance = EditBackupScheduleOutput.from_json(json)
# print the JSON string representation of the object
print(EditBackupScheduleOutput.to_json())

# convert the object into a dict
edit_backup_schedule_output_dict = edit_backup_schedule_output_instance.to_dict()
# create an instance of EditBackupScheduleOutput from a dict
edit_backup_schedule_output_from_dict = EditBackupScheduleOutput.from_dict(edit_backup_schedule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


