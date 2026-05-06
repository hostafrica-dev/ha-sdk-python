# DeleteRdnsRecordOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.delete_rdns_record_output import DeleteRdnsRecordOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRdnsRecordOutput from a JSON string
delete_rdns_record_output_instance = DeleteRdnsRecordOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteRdnsRecordOutput.to_json())

# convert the object into a dict
delete_rdns_record_output_dict = delete_rdns_record_output_instance.to_dict()
# create an instance of DeleteRdnsRecordOutput from a dict
delete_rdns_record_output_from_dict = DeleteRdnsRecordOutput.from_dict(delete_rdns_record_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


