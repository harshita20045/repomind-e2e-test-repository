"""Logical data model and persistence boundary.

The baseline deliberately uses process-local dictionaries rather than an external database.
Repositories own that data-access detail, so a future database adapter can replace them
without moving business rules into the API layer.
"""

from app.dependencies import order_repository, user_repository

__all__ = ["order_repository", "user_repository"]
