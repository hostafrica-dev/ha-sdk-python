# ListRdnsRecordsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**ListRdnsResponseData**](ListRdnsResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_rdns_records_output import ListRdnsRecordsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListRdnsRecordsOutput from a JSON string
list_rdns_records_output_instance = ListRdnsRecordsOutput.from_json(json)
# print the JSON string representation of the object
print(ListRdnsRecordsOutput.to_json())

# convert the object into a dict
list_rdns_records_output_dict = list_rdns_records_output_instance.to_dict()
# create an instance of ListRdnsRecordsOutput from a dict
list_rdns_records_output_from_dict = ListRdnsRecordsOutput.from_dict(list_rdns_records_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


