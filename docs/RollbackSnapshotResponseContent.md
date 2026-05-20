# RollbackSnapshotResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.rollback_snapshot_response_content import RollbackSnapshotResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackSnapshotResponseContent from a JSON string
rollback_snapshot_response_content_instance = RollbackSnapshotResponseContent.from_json(json)
# print the JSON string representation of the object
print(RollbackSnapshotResponseContent.to_json())

# convert the object into a dict
rollback_snapshot_response_content_dict = rollback_snapshot_response_content_instance.to_dict()
# create an instance of RollbackSnapshotResponseContent from a dict
rollback_snapshot_response_content_from_dict = RollbackSnapshotResponseContent.from_dict(rollback_snapshot_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


