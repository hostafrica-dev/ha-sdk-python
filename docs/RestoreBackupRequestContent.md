# RestoreBackupRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**backup_id** | **str** | Backup identifier for the backup to restore | 

## Example

```python
from ha_sdk_python.models.restore_backup_request_content import RestoreBackupRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreBackupRequestContent from a JSON string
restore_backup_request_content_instance = RestoreBackupRequestContent.from_json(json)
# print the JSON string representation of the object
print(RestoreBackupRequestContent.to_json())

# convert the object into a dict
restore_backup_request_content_dict = restore_backup_request_content_instance.to_dict()
# create an instance of RestoreBackupRequestContent from a dict
restore_backup_request_content_from_dict = RestoreBackupRequestContent.from_dict(restore_backup_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


