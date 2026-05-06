# CreateBackupInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**compress** | [**CompressionType**](CompressionType.md) |  | [optional] 
**mode** | **str** | Backup mode (e.g., snapshot, suspend, stop) | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_backup_input import CreateBackupInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBackupInput from a JSON string
create_backup_input_instance = CreateBackupInput.from_json(json)
# print the JSON string representation of the object
print(CreateBackupInput.to_json())

# convert the object into a dict
create_backup_input_dict = create_backup_input_instance.to_dict()
# create an instance of CreateBackupInput from a dict
create_backup_input_from_dict = CreateBackupInput.from_dict(create_backup_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


