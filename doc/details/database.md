
```mermaid
---
title: Product
---
erDiagram
    PRODUCT {
        string title
        string description
        float price
        int inventory
        datetfield last_updated
    }
```

```mermaid
---
title: Customer
---
erDiagram
    CUSTOMER {
        string first_name
        string last_name
        email_field email
        string phone
        datefield birth_date
    }
```