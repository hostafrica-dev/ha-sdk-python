# ListSnapshotsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 

## Example

```python
from hostafrica_sdk_python.models.list_snapshots_input import ListSnapshotsInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshotsInput from a JSON string
list_snapshots_input_instance = ListSnapshotsInput.from_json(json)
# print the JSON string representation of the object
print(ListSnapshotsInput.to_json())

# convert the object into a dict
list_snapshots_input_dict = list_snapshots_input_instance.to_dict()
# create an instance of ListSnapshotsInput from a dict
list_snapshots_input_from_dict = ListSnapshotsInput.from_dict(list_snapshots_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


