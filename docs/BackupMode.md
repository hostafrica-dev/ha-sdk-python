# BackupMode

Backup mode option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Backup mode value | 
**label** | **str** | Human-readable label for the backup mode | 

## Example

```python
from ha_sdk_python.models.backup_mode import BackupMode

# TODO update the JSON string below
json = "{}"
# create an instance of BackupMode from a JSON string
backup_mode_instance = BackupMode.from_json(json)
# print the JSON string representation of the object
print(BackupMode.to_json())

# convert the object into a dict
backup_mode_dict = backup_mode_instance.to_dict()
# create an instance of BackupMode from a dict
backup_mode_from_dict = BackupMode.from_dict(backup_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


