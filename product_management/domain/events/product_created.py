from dataclasses import dataclass

from shared.abstractions.events.event import Event


@dataclass
class ProductCreated(Event):
    name: str
