# GetCatalogueRequestContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Optional group identifier to filter catalogue results | [optional] 
**product_id** | **str** | Optional product identifier to filter catalogue results | [optional] 

## Example

```python
from ha_sdk_python.models.get_catalogue_request_content import GetCatalogueRequestContent

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogueRequestContent from a JSON string
get_catalogue_request_content_instance = GetCatalogueRequestContent.from_json(json)
# print the JSON string representation of the object
print(GetCatalogueRequestContent.to_json())

# convert the object into a dict
get_catalogue_request_content_dict = get_catalogue_request_content_instance.to_dict()
# create an instance of GetCatalogueRequestContent from a dict
get_catalogue_request_content_from_dict = GetCatalogueRequestContent.from_dict(get_catalogue_request_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


