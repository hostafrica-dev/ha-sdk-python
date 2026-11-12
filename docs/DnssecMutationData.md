# DnssecMutationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**records** | [**List[DnssecRecordInfo]**](DnssecRecordInfo.md) | DNSSEC DS records after mutation when returned by upstream | [optional] 

## Example

```python
from ha_sdk_python.models.dnssec_mutation_data import DnssecMutationData

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecMutationData from a JSON string
dnssec_mutation_data_instance = DnssecMutationData.from_json(json)
# print the JSON string representation of the object
print(DnssecMutationData.to_json())

# convert the object into a dict
dnssec_mutation_data_dict = dnssec_mutation_data_instance.to_dict()
# create an instance of DnssecMutationData from a dict
dnssec_mutation_data_from_dict = DnssecMutationData.from_dict(dnssec_mutation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


