# EditBackupScheduleResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.edit_backup_schedule_response_content import EditBackupScheduleResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of EditBackupScheduleResponseContent from a JSON string
edit_backup_schedule_response_content_instance = EditBackupScheduleResponseContent.from_json(json)
# print the JSON string representation of the object
print(EditBackupScheduleResponseContent.to_json())

# convert the object into a dict
edit_backup_schedule_response_content_dict = edit_backup_schedule_response_content_instance.to_dict()
# create an instance of EditBackupScheduleResponseContent from a dict
edit_backup_schedule_response_content_from_dict = EditBackupScheduleResponseContent.from_dict(edit_backup_schedule_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


