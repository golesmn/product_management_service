import uuid

from flask import request

from product_management.application.services.product_service import ProductService
from product_management.domain.aggregates.product import Product
from product_management.infrastructure.product_repository import ProductRepository
from shared.abstractions.events.event import Event
from shared.infrastructure.messaging.kafka_producer import get_dispatcher
from shared.utils.create_service import create_service

KAFKA_PRODUCT_MANAGEMENT_TOPICS_MAP = {
    "ProductCreated": "product-topic",
}


dispatcher = get_dispatcher(kafka_topic_map=KAFKA_PRODUCT_MANAGEMENT_TOPICS_MAP)


def main():
    product_body = request.get_json()
    service, uow = create_service(
        ProductRepository, ProductService, dispatcher=dispatcher
    )

    with uow:
        product = Product.create(id=uuid.uuid4(), **product_body)
        service.create_product(product_input=product)
        uow.register(product)

    return {"msg": "product created successfully"}
