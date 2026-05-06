# ListRdnsResponseData

Response data for the list-rdns operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[RdnsRecord]**](RdnsRecord.md) | All PTR records owned by the client | 
**ptr_count** | **int** | Number of PTR records | 
**ptr_limit** | **int** | Lowest finite per-package PTR limit (-1 &#x3D; unlimited / not configured) | 
**custom_ip_mode** | **bool** | Any IP is allowed in the PTR add form | 
**subnet_custom_ip_mode** | **bool** | Free-text IP allowed inside an offered subnet pool | 
**service_only_ips** | **bool** | UI hint: only show IPs tied to the related service | 
**available_items** | [**List[RdnsAvailableItem]**](RdnsAvailableItem.md) | Services the client can manage PTRs for | 

## Example

```python
from hostafrica_sdk_python.models.list_rdns_response_data import ListRdnsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListRdnsResponseData from a JSON string
list_rdns_response_data_instance = ListRdnsResponseData.from_json(json)
# print the JSON string representation of the object
print(ListRdnsResponseData.to_json())

# convert the object into a dict
list_rdns_response_data_dict = list_rdns_response_data_instance.to_dict()
# create an instance of ListRdnsResponseData from a dict
list_rdns_response_data_from_dict = ListRdnsResponseData.from_dict(list_rdns_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


