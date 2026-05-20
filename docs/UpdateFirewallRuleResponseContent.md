# UpdateFirewallRuleResponseContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OperationStatus**](OperationStatus.md) |  | 
**data** | [**VpsSimpleActionResponseData**](VpsSimpleActionResponseData.md) |  | 

## Example

```python
from ha_sdk_python.models.update_firewall_rule_response_content import UpdateFirewallRuleResponseContent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFirewallRuleResponseContent from a JSON string
update_firewall_rule_response_content_instance = UpdateFirewallRuleResponseContent.from_json(json)
# print the JSON string representation of the object
print(UpdateFirewallRuleResponseContent.to_json())

# convert the object into a dict
update_firewall_rule_response_content_dict = update_firewall_rule_response_content_instance.to_dict()
# create an instance of UpdateFirewallRuleResponseContent from a dict
update_firewall_rule_response_content_from_dict = UpdateFirewallRuleResponseContent.from_dict(update_firewall_rule_response_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


