# AddDnssecRecordResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**DnssecMutationData**](DnssecMutationData.md) |  | 

## Example

```python
from ha_sdk_python.models.add_dnssec_record_response_content import AddDnssecRecordResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of AddDnssecRecordResponseContent from a JSON string
add_dnssec_record_response_content_instance = AddDnssecRecordResponseContent.from_json(json)
# print the JSON string representation of the object
print(AddDnssecRecordResponseContent.to_json())

# convert the object into a dict
add_dnssec_record_response_content_dict = add_dnssec_record_response_content_instance.to_dict()
# create an instance of AddDnssecRecordResponseContent from a dict
add_dnssec_record_response_content_from_dict = AddDnssecRecordResponseContent.from_dict(add_dnssec_record_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


