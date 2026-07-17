# CatalogueProduct

A product entry within a catalogue group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Product identifier | 
**name** | **str** | Product display name | 
**type** | **str** | Product type (e.g. server) | 
**requires_hostname** | **bool** | Whether the product requires a hostname at order time | 
**billing_cycles** | **List[str]** | Billing cycles available for this product | 
**pricing** | **object** | Base per-cycle pricing for the product (before plan selection) | 
**use_plans** | **bool** | Whether this product uses plan-based sizing | 
**plans** | [**List[CataloguePlan]**](CataloguePlan.md) | Available plans (size tiers) for this product | 
**config_options** | [**List[CatalogueConfigOption]**](CatalogueConfigOption.md) | Configurable add-on options for this product | 
**additional_information** | **object** | Additional product information fields | 

## Example

```python
from ha_sdk_python.models.catalogue_product import CatalogueProduct

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueProduct from a JSON string
catalogue_product_instance = CatalogueProduct.from_json(json)
# print the JSON string representation of the object
print(CatalogueProduct.to_json())

# convert the object into a dict
catalogue_product_dict = catalogue_product_instance.to_dict()
# create an instance of CatalogueProduct from a dict
catalogue_product_from_dict = CatalogueProduct.from_dict(catalogue_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


