# DeleteBackupRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**backup_id** | **int** | Backup ID to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_backup_request_content import DeleteBackupRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupRequestContent from a JSON string
delete_backup_request_content_instance = DeleteBackupRequestContent.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupRequestContent.to_json())

# convert the object into a dict
delete_backup_request_content_dict = delete_backup_request_content_instance.to_dict()
# create an instance of DeleteBackupRequestContent from a dict
delete_backup_request_content_from_dict = DeleteBackupRequestContent.from_dict(delete_backup_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


