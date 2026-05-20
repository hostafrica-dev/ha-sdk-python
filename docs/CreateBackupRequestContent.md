# CreateBackupRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**compress** | [**CompressionType**](CompressionType.md) |  | [optional] 
**mode** | [**BackupModeType**](BackupModeType.md) |  | [optional] 

## Example

```python
from ha_sdk_python.models.create_backup_request_content import CreateBackupRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupRequestContent from a JSON string
create_backup_request_content_instance = CreateBackupRequestContent.from_json(json)
# print the JSON string representation of the object
print(CreateBackupRequestContent.to_json())

# convert the object into a dict
create_backup_request_content_dict = create_backup_request_content_instance.to_dict()
# create an instance of CreateBackupRequestContent from a dict
create_backup_request_content_from_dict = CreateBackupRequestContent.from_dict(create_backup_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


