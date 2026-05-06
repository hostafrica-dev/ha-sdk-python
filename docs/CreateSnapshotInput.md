# CreateSnapshotInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Service ID - must be sent as a string | 
**snapname** | **str** | Name for the snapshot | [optional] 
**description** | **str** | Description for the snapshot | [optional] 

## Example

```python
from hostafrica_sdk_python.models.create_snapshot_input import CreateSnapshotInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotInput from a JSON string
create_snapshot_input_instance = CreateSnapshotInput.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotInput.to_json())

# convert the object into a dict
create_snapshot_input_dict = create_snapshot_input_instance.to_dict()
# create an instance of CreateSnapshotInput from a dict
create_snapshot_input_from_dict = CreateSnapshotInput.from_dict(create_snapshot_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


