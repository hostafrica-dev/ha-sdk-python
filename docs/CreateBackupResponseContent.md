# CreateBackupResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**BackupCreateResponseData**](BackupCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_backup_response_content import CreateBackupResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupResponseContent from a JSON string
create_backup_response_content_instance = CreateBackupResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateBackupResponseContent.to_json())

# convert the object into a dict
create_backup_response_content_dict = create_backup_response_content_instance.to_dict()
# create an instance of CreateBackupResponseContent from a dict
create_backup_response_content_from_dict = CreateBackupResponseContent.from_dict(create_backup_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


