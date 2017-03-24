from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cloudmeb.products.models import Product

class ProductResource(ModelResource):
    solution_categories = fields.ToManyField('cloudmeb.categories.api.CategoryResource', 'solution_categories', full=True, null=True)
    solution_values = fields.ToManyField('cloudmeb.values.api.ValueResource', 'solution_values', full=True, null=True)
    solution_benefits = fields.ToManyField('cloudmeb.benefits.api.BenefitResource', 'solution_benefits', full=True, null=True)
    price_inputs = fields.ToManyField('cloudmeb.inputs.api.InputResource', 'price_inputs', full=True, null=True)

    class Meta:
        queryset = Product.objects.all().distinct()
        resource_name = 'product'
        allowed_methods = ['get']
        filtering = {
            'name': ALL,
            'solution_categories': ALL_WITH_RELATIONS,
            'solution_values': ALL_WITH_RELATIONS,
            'solution_benefits': ALL_WITH_RELATIONS,
            'price_inputs': ALL_WITH_RELATIONS,
        }
