import uuid
from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

from product_management.domain.aggregates.product import Product

Base = declarative_base()


class ProductModel(Base):
    __tablename__ = "products"  # Replace with your actual Django table name
    __table_args__ = {"extend_existing": True}  # Important to avoid table recreation

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    price = Column(Float)
    
    @staticmethod
    def from_entity(product: Product):
        return ProductModel(
            id=product.id,
            name=product.name,
            price=product.price
        )
    
    def to_entity(self):
        return Product(id=self.id, name=self.name, price=self.price)