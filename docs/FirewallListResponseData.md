# FirewallListResponseData

Response data for firewall list operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Status message | 
**rules** | [**List[FirewallRule]**](FirewallRule.md) | List of firewall rules | 
**available_interfaces** | [**List[FirewallOption]**](FirewallOption.md) | Available network interfaces | 
**available_macros** | [**List[FirewallOption]**](FirewallOption.md) | Available firewall macros | 
**available_protocols** | [**List[FirewallOption]**](FirewallOption.md) | Available network protocols | 

## Example

```python
from ha_sdk_python.models.firewall_list_response_data import FirewallListResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallListResponseData from a JSON string
firewall_list_response_data_instance = FirewallListResponseData.from_json(json)
# print the JSON string representation of the object
print(FirewallListResponseData.to_json())

# convert the object into a dict
firewall_list_response_data_dict = firewall_list_response_data_instance.to_dict()
# create an instance of FirewallListResponseData from a dict
firewall_list_response_data_from_dict = FirewallListResponseData.from_dict(firewall_list_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


