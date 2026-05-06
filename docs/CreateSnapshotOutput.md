# CreateSnapshotOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**SnapshotCreateResponseData**](SnapshotCreateResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_snapshot_output import CreateSnapshotOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotOutput from a JSON string
create_snapshot_output_instance = CreateSnapshotOutput.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotOutput.to_json())

# convert the object into a dict
create_snapshot_output_dict = create_snapshot_output_instance.to_dict()
# create an instance of CreateSnapshotOutput from a dict
create_snapshot_output_from_dict = CreateSnapshotOutput.from_dict(create_snapshot_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


