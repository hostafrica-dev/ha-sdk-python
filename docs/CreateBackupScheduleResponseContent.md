# CreateBackupScheduleResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.create_backup_schedule_response_content import CreateBackupScheduleResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupScheduleResponseContent from a JSON string
create_backup_schedule_response_content_instance = CreateBackupScheduleResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateBackupScheduleResponseContent.to_json())

# convert the object into a dict
create_backup_schedule_response_content_dict = create_backup_schedule_response_content_instance.to_dict()
# create an instance of CreateBackupScheduleResponseContent from a dict
create_backup_schedule_response_content_from_dict = CreateBackupScheduleResponseContent.from_dict(create_backup_schedule_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


