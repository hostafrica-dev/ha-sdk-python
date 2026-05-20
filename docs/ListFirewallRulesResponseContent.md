# ListFirewallRulesResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**FirewallListResponseData**](FirewallListResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.list_firewall_rules_response_content import ListFirewallRulesResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallRulesResponseContent from a JSON string
list_firewall_rules_response_content_instance = ListFirewallRulesResponseContent.from_json(json)
# print the JSON string representation of the object
print(ListFirewallRulesResponseContent.to_json())

# convert the object into a dict
list_firewall_rules_response_content_dict = list_firewall_rules_response_content_instance.to_dict()
# create an instance of ListFirewallRulesResponseContent from a dict
list_firewall_rules_response_content_from_dict = ListFirewallRulesResponseContent.from_dict(list_firewall_rules_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


