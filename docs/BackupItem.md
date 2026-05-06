# BackupItem

Individual backup item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Backup ID | 
**size** | **str** | Backup size in human-readable format | 
**create_date** | **str** | Backup creation date and time | 
**format** | **str** | Backup format (e.g., vma, vma.lzo) | 
**protected** | **bool** | Whether the backup is protected from deletion | 

## Example

```python
from hostafrica_sdk_python.models.backup_item import BackupItem

# TODO update the JSON string below
json = "{}"
# create an instance of BackupItem from a JSON string
backup_item_instance = BackupItem.from_json(json)
# print the JSON string representation of the object
print(BackupItem.to_json())

# convert the object into a dict
backup_item_dict = backup_item_instance.to_dict()
# create an instance of BackupItem from a dict
backup_item_from_dict = BackupItem.from_dict(backup_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


