# DeleteBackupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**backup_id** | **int** | Backup ID to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_backup_input import DeleteBackupInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupInput from a JSON string
delete_backup_input_instance = DeleteBackupInput.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupInput.to_json())

# convert the object into a dict
delete_backup_input_dict = delete_backup_input_instance.to_dict()
# create an instance of DeleteBackupInput from a dict
delete_backup_input_from_dict = DeleteBackupInput.from_dict(delete_backup_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


