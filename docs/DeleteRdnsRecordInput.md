# DeleteRdnsRecordInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **int** | ID of the PTR record to delete | 

## Example

```python
from hostafrica_sdk_python.models.delete_rdns_record_input import DeleteRdnsRecordInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRdnsRecordInput from a JSON string
delete_rdns_record_input_instance = DeleteRdnsRecordInput.from_json(json)
# print the JSON string representation of the object
print(DeleteRdnsRecordInput.to_json())

# convert the object into a dict
delete_rdns_record_input_dict = delete_rdns_record_input_instance.to_dict()
# create an instance of DeleteRdnsRecordInput from a dict
delete_rdns_record_input_from_dict = DeleteRdnsRecordInput.from_dict(delete_rdns_record_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


