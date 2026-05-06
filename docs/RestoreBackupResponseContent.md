# RestoreBackupResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.restore_backup_response_content import RestoreBackupResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreBackupResponseContent from a JSON string
restore_backup_response_content_instance = RestoreBackupResponseContent.from_json(json)
# print the JSON string representation of the object
print(RestoreBackupResponseContent.to_json())

# convert the object into a dict
restore_backup_response_content_dict = restore_backup_response_content_instance.to_dict()
# create an instance of RestoreBackupResponseContent from a dict
restore_backup_response_content_from_dict = RestoreBackupResponseContent.from_dict(restore_backup_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


