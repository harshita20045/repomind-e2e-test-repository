# Architecture

The application follows:

```text
API → Service → Repository → In-Memory Data Store
```

- **API** (`app/api/`) validates HTTP input, selects status codes, and serializes responses.
- **Service** (`app/services/`) owns business rules such as checking that an order's user exists and calculating subtotal, tax, and total.
- **Repository** (`app/repositories/`) owns data access operations and hides the process-local dictionaries.
- **In-memory data store** is the dictionaries held by the repository instances in `app/dependencies.py`.

The API does not calculate order totals or manipulate repository dictionaries directly.
The shared repository instances preserve data across requests during one application process.
