# BackupCreationInfo

Information about an ongoing backup creation process

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Backup creation task ID | 
**status** | **str** | Status of the backup creation | 
**message** | **str** | Status message | 
**created_at** | **str** | Timestamp when backup creation started | 
**updated_at** | **str** | Timestamp when backup creation was last updated | 

## Example

```python
from hostafrica_sdk_python.models.backup_creation_info import BackupCreationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCreationInfo from a JSON string
backup_creation_info_instance = BackupCreationInfo.from_json(json)
# print the JSON string representation of the object
print(BackupCreationInfo.to_json())

# convert the object into a dict
backup_creation_info_dict = backup_creation_info_instance.to_dict()
# create an instance of BackupCreationInfo from a dict
backup_creation_info_from_dict = BackupCreationInfo.from_dict(backup_creation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


