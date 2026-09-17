# RepoMind FastAPI fixture

A small, self-contained FastAPI User + Order application for repository analysis, retrieval, and PR review testing. It uses an in-memory data store and needs no PostgreSQL, Redis, Docker, or external service.

## Install and run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Interactive OpenAPI documentation is available at `/docs`.

## Test

```bash
pytest -v
```

## Architecture

`API → Service → Repository → In-Memory Data Store`.
Routes are in `app/api`, business rules in `app/services`, and data access in `app/repositories`.
See `docs/architecture.md`, `docs/api-contract.md`, `docs/database.md`, and `docs/security.md`.

## API overview

- `GET /health`
- `POST /users`
- `GET /users/{user_id}`
- `POST /orders`
- `GET /orders/{order_id}`

Successful user and order creation return `201`; missing resources return `404`; invalid input returns `422`.

## Repository knowledge questions

1. **Where is user creation implemented?** `UserService.create_user` in `app/services/user_service.py`, called by `app/api/users.py`.
2. **Which service handles order creation?** `OrderService` in `app/services/order_service.py`.
3. **Which layer owns data access?** The repository layer in `app/repositories/`.
4. **What endpoint creates an order?** `POST /orders`.
5. **What is the User/Order relationship?** One user can own many orders; each order has one `user_id`.
6. **What status indicates successful user creation?** `201 Created`.
7. **Where is order validation implemented?** Request constraints are in `app/models/order.py`; ownership and totals are in `OrderService`.
8. **Which tests cover order creation?** `tests/test_orders.py`.
9. **What configuration does the application use?** `app/config.py` reads settings such as `APP_NAME`, `API_KEY`, `DEBUG`, and `ORDER_TAX_RATE` from the environment.
