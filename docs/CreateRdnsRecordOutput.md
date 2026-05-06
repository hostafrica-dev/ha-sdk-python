# CreateRdnsRecordOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**CreateRdnsRecordResponseData**](CreateRdnsRecordResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.create_rdns_record_output import CreateRdnsRecordOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRdnsRecordOutput from a JSON string
create_rdns_record_output_instance = CreateRdnsRecordOutput.from_json(json)
# print the JSON string representation of the object
print(CreateRdnsRecordOutput.to_json())

# convert the object into a dict
create_rdns_record_output_dict = create_rdns_record_output_instance.to_dict()
# create an instance of CreateRdnsRecordOutput from a dict
create_rdns_record_output_from_dict = CreateRdnsRecordOutput.from_dict(create_rdns_record_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


