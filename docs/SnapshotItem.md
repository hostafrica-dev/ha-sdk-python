# SnapshotItem

Individual snapshot item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Snapshot name | 
**description** | **str** | Snapshot description | 
**snaptime** | **str** | Snapshot creation date | [optional] 
**size** | **int** | Snapshot size in bytes | [optional] 
**vmstate** | **bool** | Whether VM state is included | [optional] 

## Example

```python
from hostafrica_sdk_python.models.snapshot_item import SnapshotItem

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotItem from a JSON string
snapshot_item_instance = SnapshotItem.from_json(json)
# print the JSON string representation of the object
print(SnapshotItem.to_json())

# convert the object into a dict
snapshot_item_dict = snapshot_item_instance.to_dict()
# create an instance of SnapshotItem from a dict
snapshot_item_from_dict = SnapshotItem.from_dict(snapshot_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


