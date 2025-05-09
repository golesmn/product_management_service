from datetime import datetime
import uuid
from product_management.domain.events.product_created import ProductCreated
from shared.abstractions.primitives.aggregate import AggregateRoot


class Product(AggregateRoot):
    def __init__(self, id: str, name: str, price: float):
        super().__init__()
        self.id = id
        self.name = name
        self.price = price

    @classmethod
    def create(cls, id: str, name: str, price: float):
        instance = cls(id, name, price)
        instance.add_event(ProductCreated(
                                        event_id=uuid.uuid4(),
                                        event_type="product.created", 
                                        name="product.created", 
                                        timestamp=datetime.now()))
        return instance