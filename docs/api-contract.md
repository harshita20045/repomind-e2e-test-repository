# API contract

The service is available locally at `http://127.0.0.1:8000`.

## `GET /health`

Returns `200` and `{ "status": "ok" }`.

## `POST /users`

Request: `{ "name": "Ada", "email": "ada@example.com" }`.

Returns `201` with `id`, `name`, `email`, and `created_at`. Invalid or missing fields return `422`.

## `GET /users/{user_id}`

Returns `200` with the user, or `404` with `User not found`.

## `POST /orders`

Request: `{ "user_id": 1, "items": [{"sku": "book", "quantity": 2, "unit_price": 10}] }`.

Returns `201` with the order, item list, subtotal, tax, total, and `created_at`.
The service calculates subtotal as quantity times unit price and applies the configured tax rate.
A nonexistent `user_id` returns `404`. Empty items, non-positive quantities/prices, and malformed
requests return `422`.

## `GET /orders/{order_id}`

Returns `200` with the order, or `404` with `Order not found`.
