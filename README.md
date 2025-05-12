
# Product Management Service

This repository contains the **Access Management Service**, an independent microservice implemented as a [Fission](https://fission.io/) function. It provides product management capabilities and is designed following **Domain-Driven Design (DDD)** principles along with the **Repository** and **Service** patterns.

---

## 📁 Project Structure

``` bash
product_management/
├── application/        # Commands and service logic
├── domain/             # Aggregates, value objects, domain events
├── infrastructure/     # ORM models and other infra details, repositories
├── interfaces/         # Interfaces for external interactions
├── main.py             # Entry point for the function
├── requirements.txt    # Dependencies
shared/                 # Shared abstractions (DB, messaging, etc.)
specs/                  # Fission deployment configs and routes
```

---

## Architecture patterns used

### Domain-Driven Design (DDD)

* Domain layer contains aggregates, entities, value objects, and events.
* Business logic is encapsulated in aggregates like `Product`.

### Repository Pattern

* Abstracts data access via repository interfaces and implementations like `product_repository.py`.

### Service Pattern

* Encapsulates application-specific logic in `services/product_service.py`.

---

## 🚀 Fission Deployment

The `specs/` directory contains the YAML specifications to deploy this service as a Fission function:

* `function-product-management.yaml`: Registers the function.
* `route-product-create.yaml`: Maps HTTP route to product creation or messaging.
* `fission-deployment-config.yaml`: Additional deployment configuration.

Deploy all resources using:

```bash
fission spec apply --specdir specs
```

## 📄 Example Event Flow (Product Creation)

1. Request hits Fission route → triggers function
2. Handler receives command (e.g. `CreateProduct`)
3. Handler delegates to `ProductService`
4. Service constructs and persists domain aggregate
5. Domain event `ProductCreated` is dispatched (e.g., to Kafka)

## Deployment

For deployment, go to the shared submodule and check document [running_locally](./shared/docs/running_locally.md) file.

---
