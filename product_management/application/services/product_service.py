from product_management.domain.aggregates.product import Product
from product_management.infrastructure.models import ProductModel
from product_management.infrastructure.product_repository import ProductRepository


class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def create_product(self, product_input: Product):
        product = ProductModel.from_entity(product_input)
        self.product_repo.save(product)
