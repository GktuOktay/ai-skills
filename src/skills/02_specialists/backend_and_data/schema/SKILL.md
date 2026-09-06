---
name: Schema Design
description: "İlişkisel veri tabanları, NoSQL ve API'ler için ölçeklenebilir ve güvenli şema tasarım kalıpları."
---

# Database and API Schema Design

Effective schema design is foundational to application performance, data integrity, and future scalability. This guide covers relational, NoSQL, and API schema design principles.

## 1. Relational Database Schema Design (SQL)

Relational databases (PostgreSQL, MySQL) excel at structured data with complex relationships.

### Normalization
The process of organizing data to reduce redundancy and improve data integrity.
- **1NF**: Eliminate repeating groups (each column contains atomic values).
- **2NF**: Eliminate partial dependencies (non-key columns depend on the entire primary key).
- **3NF**: Eliminate transitive dependencies (non-key columns depend only on the primary key, not on other non-key columns).
*Rule of thumb: Normalize to 3NF by default, denormalize only for specific read-performance bottlenecks.*

### Indexing
Indexes drastically speed up read operations but slow down writes and consume disk space.
- **Primary Keys**: Automatically indexed.
- **Foreign Keys**: Always index foreign keys to speed up JOIN operations.
- **Frequent Queries**: Create B-Tree indexes on columns frequently used in `WHERE`, `ORDER BY`, or `GROUP BY` clauses.
- **Composite Indexes**: Use for queries that filter on multiple columns simultaneously (order matters: put the most selective column first).

### Constraints
Enforce data integrity at the database level.
- `NOT NULL`, `UNIQUE`, `CHECK` (e.g., `price > 0`), `FOREIGN KEY` (referential integrity).

### Migrations
Always use a migration tool (e.g., Prisma, Flyway, Alembic) to version control schema changes. Never modify the production schema manually.

## 2. NoSQL Schema Patterns

NoSQL databases (MongoDB, DynamoDB, Neo4j) are chosen for flexibility, horizontal scalability, or specific data models.

### Document Databases (MongoDB)
- **Embedding vs. Referencing**: 
  - Embed data (sub-documents) if it is frequently accessed together and rarely changes (e.g., User addresses).
  - Reference data (store IDs) if the nested data is large, grows unbounded, or is accessed independently (e.g., Post comments).

### Key-Value / Wide Column (DynamoDB, Cassandra)
- **Access Pattern Driven**: Design the schema based on *how* you will query the data, not how the data is related.
- **Single Table Design**: Storing multiple entity types in a single table using generic Partition Keys (PK) and Sort Keys (SK) to retrieve complex relations in a single query.

### Graph Databases (Neo4j)
- Use for highly connected data (social networks, recommendation engines). Focus on Nodes (entities) and Edges (relationships).

## 3. API Schema Design

APIs act as the contract between the frontend and backend.

### REST Conventions
- **Nouns, not Verbs**: Use `/users`, not `/getUsers`.
- **Plurals**: Consistently use plural nouns (`/products/123`).
- **Nesting**: Represent relationships logically: `GET /users/123/orders`.
- **Filtering/Pagination**: Use query parameters: `GET /users?role=admin&limit=20&offset=40`.

### GraphQL Schema
- Strongly typed. Clients request exactly what they need.
- Define clearly separated Queries (reads) and Mutations (writes/updates).
- Avoid overly deep nesting to prevent expensive database queries (the N+1 problem).

### OpenAPI / Swagger
- The industry standard for defining REST API contracts.
- Use it to generate interactive documentation, client SDKs, and server stubs.

## 4. Schema Validation

Never trust client input. Validate data at the boundary.
- **Zod (TypeScript)**: Excellent for runtime validation and deriving TypeScript types simultaneously.
- **JSON Schema**: Language-agnostic standard for describing JSON data formats.
- **Codable (Swift)**: First-party solution for parsing JSON safely in iOS apps.

## 5. Versioning Strategies

APIs evolve. Avoid breaking changes for existing clients.
- **URI Versioning**: `/api/v1/users` (Most common, easy to cache).
- **Header Versioning**: `Accept: application/vnd.company.v1+json` (Cleaner URLs, harder to test in browser).
- **GraphQL**: Evolve the schema by adding new fields and deprecating old ones using the `@deprecated` directive, avoiding hard version bumps.

## 6. Common Anti-Patterns

- **EAV (Entity-Attribute-Value)**: Creating generic tables (`entity_id`, `attribute_name`, `value`) in SQL. It destroys performance and makes querying a nightmare. Use JSONB columns in Postgres instead.
- **Fat Controllers**: Putting schema validation and business logic in the API routing layer instead of dedicated validation modules.
- **God Objects**: Returning massive, deeply nested API responses when the client only needs two fields.
