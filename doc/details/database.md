
```mermaid
---
title: Product
---
erDiagram
    PRODUCT {
        string sku PK
        string title
        string description
        float price
        int inventory
        datetfield last_updated
    }
```
- sku = Stock Keeping Unit (Don vi luu kho)

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
        string membership
    }
```