# ListFirewallRulesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**FirewallListResponseData**](FirewallListResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.list_firewall_rules_output import ListFirewallRulesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ListFirewallRulesOutput from a JSON string
list_firewall_rules_output_instance = ListFirewallRulesOutput.from_json(json)
# print the JSON string representation of the object
print(ListFirewallRulesOutput.to_json())

# convert the object into a dict
list_firewall_rules_output_dict = list_firewall_rules_output_instance.to_dict()
# create an instance of ListFirewallRulesOutput from a dict
list_firewall_rules_output_from_dict = ListFirewallRulesOutput.from_dict(list_firewall_rules_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


