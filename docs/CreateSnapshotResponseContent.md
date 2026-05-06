# CreateSnapshotResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**SnapshotCreateResponseData**](SnapshotCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_snapshot_response_content import CreateSnapshotResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotResponseContent from a JSON string
create_snapshot_response_content_instance = CreateSnapshotResponseContent.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotResponseContent.to_json())

# convert the object into a dict
create_snapshot_response_content_dict = create_snapshot_response_content_instance.to_dict()
# create an instance of CreateSnapshotResponseContent from a dict
create_snapshot_response_content_from_dict = CreateSnapshotResponseContent.from_dict(create_snapshot_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


