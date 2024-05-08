### This is Ecomerce Website using Django tech
#### <ins>Management apps:</ins>
- Main app: Core 
- Sub apps: 
    - Store

```mermaid
graph TD;
    Core --> Store;
```

#### <ins>Pages in Store App:</ins>
```mermaid
graph TD;
    Base --> Home.html;
    Base --> Login.html;
    Base --> Checkout.html;
    Base --> Cart.html;
```