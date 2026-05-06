# ListSnapshotsResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ServiceSnapshotsResponseData**](ServiceSnapshotsResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_snapshots_response_content import ListSnapshotsResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshotsResponseContent from a JSON string
list_snapshots_response_content_instance = ListSnapshotsResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListSnapshotsResponseContent.to_json())

# convert the object into a dict
list_snapshots_response_content_dict = list_snapshots_response_content_instance.to_dict()
# create an instance of ListSnapshotsResponseContent from a dict
list_snapshots_response_content_from_dict = ListSnapshotsResponseContent.from_dict(list_snapshots_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


