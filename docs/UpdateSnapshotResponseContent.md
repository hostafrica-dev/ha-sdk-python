# UpdateSnapshotResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.update_snapshot_response_content import UpdateSnapshotResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnapshotResponseContent from a JSON string
update_snapshot_response_content_instance = UpdateSnapshotResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateSnapshotResponseContent.to_json())

# convert the object into a dict
update_snapshot_response_content_dict = update_snapshot_response_content_instance.to_dict()
# create an instance of UpdateSnapshotResponseContent from a dict
update_snapshot_response_content_from_dict = UpdateSnapshotResponseContent.from_dict(update_snapshot_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


