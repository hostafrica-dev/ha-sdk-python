# ListSnapshotsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ServiceSnapshotsResponseData**](ServiceSnapshotsResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_snapshots_output import ListSnapshotsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshotsOutput from a JSON string
list_snapshots_output_instance = ListSnapshotsOutput.from_json(json)
# print the JSON string representation of the object
print(ListSnapshotsOutput.to_json())

# convert the object into a dict
list_snapshots_output_dict = list_snapshots_output_instance.to_dict()
# create an instance of ListSnapshotsOutput from a dict
list_snapshots_output_from_dict = ListSnapshotsOutput.from_dict(list_snapshots_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


