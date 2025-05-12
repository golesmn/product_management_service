import uuid

from flask import request

from product_management.application.services.product_service import ProductService
from product_management.domain.aggregates.product import Product
from product_management.infrastructure.product_repository import ProductRepository
from shared.utils.create_service import create_service


def main():
    product_body = request.get_json()
    service, uow = create_service(ProductRepository, ProductService)

    with uow:
        product = Product.create(id=uuid.uuid4(), **product_body)
        service.create_product(product_input=product)
        uow.register(product)

    return {"msg": "product created successfully"}
