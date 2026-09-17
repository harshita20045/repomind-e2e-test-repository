# Logical data model

The baseline has no external database. `UserRepository` and `OrderRepository` use in-memory
Python dictionaries, so data is lost when the process stops.

## User

- `id`
- `email`
- `name`
- `created_at`

## Order

- `id`
- `user_id`
- `items`
- `subtotal`
- `tax`
- `total`
- `created_at`

Relationship:

```text
User 1 ──── N Order
```

Each order references the owning user through `user_id`; order creation rejects unknown users.
