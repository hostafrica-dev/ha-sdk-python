# DeleteBackupOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.delete_backup_output import DeleteBackupOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBackupOutput from a JSON string
delete_backup_output_instance = DeleteBackupOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteBackupOutput.to_json())

# convert the object into a dict
delete_backup_output_dict = delete_backup_output_instance.to_dict()
# create an instance of DeleteBackupOutput from a dict
delete_backup_output_from_dict = DeleteBackupOutput.from_dict(delete_backup_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


