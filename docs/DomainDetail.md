# DomainDetail

Full domain details returned by get-domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Domain service id | 
**type** | **str** | Domain operation type (e.g. Register, Transfer) | 
**domain** | **str** | Fully qualified domain name | 
**sld** | **str** | Second-level domain label (e.g. dandelyn) | [optional] 
**tld** | **str** | Top-level domain including dot (e.g. .co.za) | [optional] 
**status** | **str** | Domain status (e.g. Active, Expired, Cancelled) | 
**period** | **int** | Registration or billing period in years | 
**registrationdate** | **str** | Registration timestamp from upstream (ISO 8601) | [optional] 
**donotrenew** | **int** | Renewal flag: 0 &#x3D; renew, 1 &#x3D; do not renew | 
**id_protection** | **int** | WHOIS privacy enabled: 0 &#x3D; off, 1 &#x3D; on | 
**id_protection_supported** | **bool** | Whether the TLD supports ID protection | 
**firstpaymentamount** | **str** | First payment amount as a decimal string | [optional] 
**recurringamount** | **str** | Recurring amount as a decimal string (e.g. \&quot;149.99\&quot;) | 
**dnsmanagement** | **bool** | Whether DNS management addon is currently enabled | [optional] 
**emailforwarding** | **bool** | Whether email forwarding addon is currently enabled | [optional] 
**is_premium** | **bool** | Whether the domain is premium | [optional] 
**lock_status** | **str** | Registrar lock status (e.g. locked, unlocked, unavailable) | [optional] 
**grace_period** | **int** | Grace period length in days | [optional] 
**redemption_period** | **int** | Redemption period length in days | [optional] 
**grace_period_fee** | **int** | Grace period renewal fee | [optional] 
**redemption_period_fee** | **int** | Redemption period renewal fee | [optional] 
**in_grace** | **bool** | Whether the domain is currently in grace period | [optional] 
**in_redemption** | **bool** | Whether the domain is currently in redemption period | [optional] 
**expirydate** | **str** | Domain expiry date (YYYY-MM-DD or ISO 8601 from upstream) | [optional] 
**nextinvoicedate** | **str** | Next invoice date (YYYY-MM-DD or ISO 8601 from upstream) | [optional] 
**nextduedate** | **str** | Next due date (YYYY-MM-DD or ISO 8601 from upstream) | [optional] 
**available_features** | [**DomainAvailableFeatures**](DomainAvailableFeatures.md) |  | [optional] 
**domain_nameservers** | **List[str]** | Currently applied nameserver hostnames | [optional] 
**default_nameservers** | **List[str]** | Default nameserver hostnames for this domain/product | [optional] 
**ns_changing** | **str** | Nameserver change state (e.g. own, pending) | [optional] 
**has_hosting** | [**DomainHostingLink**](DomainHostingLink.md) |  | [optional] 
**has_dns_manager_zone** | **bool** | Whether a DNS Manager zone exists for this domain name | 
**expiry_countdown** | [**DomainExpiryCountdown**](DomainExpiryCountdown.md) |  | [optional] 
**evaluation** | **object** | Domain evaluator result when enabled; null when unavailable | [optional] 
**domain_evaluation_available** | **bool** | Whether domain evaluation is available for this domain/account | [optional] 
**has_redirect** | **object** | Configured redirect details when present; null when none | [optional] 
**no_epp** | **bool** | True when EPP/auth code retrieval is disabled for this domain | [optional] 

## Example

```python
from ha_sdk_python.models.domain_detail import DomainDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DomainDetail from a JSON string
domain_detail_instance = DomainDetail.from_json(json)
# print the JSON string representation of the object
print(DomainDetail.to_json())

# convert the object into a dict
domain_detail_dict = domain_detail_instance.to_dict()
# create an instance of DomainDetail from a dict
domain_detail_from_dict = DomainDetail.from_dict(domain_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


