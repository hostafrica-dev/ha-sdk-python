# CreateBackupOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**BackupCreateResponseData**](BackupCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_backup_output import CreateBackupOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupOutput from a JSON string
create_backup_output_instance = CreateBackupOutput.from_json(json)
# print the JSON string representation of the object
print(CreateBackupOutput.to_json())

# convert the object into a dict
create_backup_output_dict = create_backup_output_instance.to_dict()
# create an instance of CreateBackupOutput from a dict
create_backup_output_from_dict = CreateBackupOutput.from_dict(create_backup_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


