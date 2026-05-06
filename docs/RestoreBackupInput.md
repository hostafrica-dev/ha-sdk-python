# RestoreBackupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**backup_id** | **str** | Backup identifier for the backup to restore | 

## Example

```python
from hostafrica_sdk_python.models.restore_backup_input import RestoreBackupInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreBackupInput from a JSON string
restore_backup_input_instance = RestoreBackupInput.from_json(json)
# print the JSON string representation of the object
print(RestoreBackupInput.to_json())

# convert the object into a dict
restore_backup_input_dict = restore_backup_input_instance.to_dict()
# create an instance of RestoreBackupInput from a dict
restore_backup_input_from_dict = RestoreBackupInput.from_dict(restore_backup_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


