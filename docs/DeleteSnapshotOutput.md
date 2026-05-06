# DeleteSnapshotOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.delete_snapshot_output import DeleteSnapshotOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnapshotOutput from a JSON string
delete_snapshot_output_instance = DeleteSnapshotOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteSnapshotOutput.to_json())

# convert the object into a dict
delete_snapshot_output_dict = delete_snapshot_output_instance.to_dict()
# create an instance of DeleteSnapshotOutput from a dict
delete_snapshot_output_from_dict = DeleteSnapshotOutput.from_dict(delete_snapshot_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


