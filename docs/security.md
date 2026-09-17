# Security

## Implemented baseline behavior

- Pydantic models validate names, email addresses, positive IDs, quantities, and prices.
- Responses contain only the user and order fields defined by the models; no password or secret is stored.
- The application does not log API keys or other secrets.
- Configuration is loaded from environment variables through `app/config.py`; the YAML file is an example only.

## Not implemented

This fixture does not implement authentication, authorization, accounts, passwords, sessions, or
persistent encryption. The local default settings are suitable only for a test fixture, not production.

## Future expectations

A production deployment should require authentication, authorize access to users and orders,
keep secrets in a secret manager or environment, rotate credentials, use TLS, avoid sensitive logs,
and replace the in-memory store with a controlled persistent data layer.
