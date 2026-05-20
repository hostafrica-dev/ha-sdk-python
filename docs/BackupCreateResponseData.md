# BackupCreateResponseData

Response data for backup creation operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**task_id** | **int** | Task ID for the backup creation process | 
**backup_is_creating** | **bool** | Whether a backup is currently being created | 
**backup_creation** | [**BackupCreationInfo**](BackupCreationInfo.md) |  | 

## Example

```python
from ha_sdk_python.models.backup_create_response_data import BackupCreateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCreateResponseData from a JSON string
backup_create_response_data_instance = BackupCreateResponseData.from_json(json)
# print the JSON string representation of the object
print(BackupCreateResponseData.to_json())

# convert the object into a dict
backup_create_response_data_dict = backup_create_response_data_instance.to_dict()
# create an instance of BackupCreateResponseData from a dict
backup_create_response_data_from_dict = BackupCreateResponseData.from_dict(backup_create_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


