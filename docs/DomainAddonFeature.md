# DomainAddonFeature

Priced addon/feature block returned under available_features

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**price** | **float** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**product_desc** | **str** | Optional HTML product description from upstream | [optional] 

## Example

```python
from ha_sdk_python.models.domain_addon_feature import DomainAddonFeature

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAddonFeature from a JSON string
domain_addon_feature_instance = DomainAddonFeature.from_json(json)
# print the JSON string representation of the object
print(DomainAddonFeature.to_json())

# convert the object into a dict
domain_addon_feature_dict = domain_addon_feature_instance.to_dict()
# create an instance of DomainAddonFeature from a dict
domain_addon_feature_from_dict = DomainAddonFeature.from_dict(domain_addon_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


