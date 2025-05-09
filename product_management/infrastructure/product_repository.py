
from product_management.infrastructure.models import ProductModel
from shared.infrastructure.db.sqlalchemy_repository import SQLAlchemyRepository

from sqlalchemy.orm import Session



class ProductRepository(SQLAlchemyRepository[ProductModel]):
    def __init__(self, session: Session):
        super().__init__(session, ProductModel)