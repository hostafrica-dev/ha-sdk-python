# DeleteFirewallRuleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from hostafrica_sdk_python.models.delete_firewall_rule_output import DeleteFirewallRuleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFirewallRuleOutput from a JSON string
delete_firewall_rule_output_instance = DeleteFirewallRuleOutput.from_json(json)
# print the JSON string representation of the object
print(DeleteFirewallRuleOutput.to_json())

# convert the object into a dict
delete_firewall_rule_output_dict = delete_firewall_rule_output_instance.to_dict()
# create an instance of DeleteFirewallRuleOutput from a dict
delete_firewall_rule_output_from_dict = DeleteFirewallRuleOutput.from_dict(delete_firewall_rule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


