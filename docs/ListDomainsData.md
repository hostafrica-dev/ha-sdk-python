# ListDomainsData

List domains response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message indicating the result | 
**domains** | [**List[DomainInfo]**](DomainInfo.md) | Domains owned by the authenticated client | 
**domain_warranty** | **bool** | Whether ID-protection warranty is enabled for the account | 
**domain_warranty_rename** | **str** | Domain warranty rename setting when configured | [optional] 
**domain_evaluation_available** | **bool** | Whether domain evaluation is available for the account | 
**total_count** | **int** | Total number of domains returned | 

## Example

```python
from ha_sdk_python.models.list_domains_data import ListDomainsData

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomainsData from a JSON string
list_domains_data_instance = ListDomainsData.from_json(json)
# print the JSON string representation of the object
print(ListDomainsData.to_json())

# convert the object into a dict
list_domains_data_dict = list_domains_data_instance.to_dict()
# create an instance of ListDomainsData from a dict
list_domains_data_from_dict = ListDomainsData.from_dict(list_domains_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


