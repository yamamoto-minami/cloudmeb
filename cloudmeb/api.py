from tastypie.api import Api
from cloudmeb.values.api import ValueResource
from cloudmeb.inputs.api import InputResource
from cloudmeb.prices.api import PriceResource
from cloudmeb.benefits.api import BenefitResource
from cloudmeb.categories.api import CategoryResource
from cloudmeb.solutions.api import SolutionResource
from cloudmeb.products.api import ProductResource
from cloudmeb.services.api import ServiceResource
from cloudmeb.partners.api import PartnerResource
from cloudmeb.partner_services.api import PartnerServiceResource

api = Api(api_name='v1')
api.register(ValueResource())
api.register(InputResource())
api.register(PriceResource())
api.register(BenefitResource())
api.register(CategoryResource())
api.register(SolutionResource())
api.register(ProductResource())
api.register(ServiceResource())
api.register(PartnerResource())
api.register(PartnerServiceResource())
