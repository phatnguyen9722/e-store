### How Docker works with Django?


```mermaid
---
title: Docker workflow
---
flowchart LR
    subgraph DA
        subgraph Django Application
            id["Django App"]
        end
    end

    subgraph DI
        subgraph Docker Image
            id1["Django App"]
            id2["Dockerfile"]
        end
    end

    subgraph DC
        subgraph Docker Container
            id3["OS"]
            id4["Database"]
            id5["Django App"]
            id6["Package]
        end
    end
    
    DA ==> DI
    DI ==> DC
```