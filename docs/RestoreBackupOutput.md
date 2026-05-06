# RestoreBackupOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.restore_backup_output import RestoreBackupOutput

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreBackupOutput from a JSON string
restore_backup_output_instance = RestoreBackupOutput.from_json(json)
# print the JSON string representation of the object
print(RestoreBackupOutput.to_json())

# convert the object into a dict
restore_backup_output_dict = restore_backup_output_instance.to_dict()
# create an instance of RestoreBackupOutput from a dict
restore_backup_output_from_dict = RestoreBackupOutput.from_dict(restore_backup_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


