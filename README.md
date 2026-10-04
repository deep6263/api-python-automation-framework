# Enterprise Python API Automation Framework

A scalable API automation framework built with **Python, Pytest, Requests, Allure, JSON Schema, Loguru, and GitHub Actions**.

The framework demonstrates professional API testing practices including reusable API clients, environment-based configuration, external test data, schema validation, response-time validation, negative testing, structured logging, retry handling, reporting, and CI/CD integration.

---

## 🚀 Project Overview

This project automates the REST APIs provided by [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

The framework validates CRUD operations for the Posts API:

```text
GET     /posts
GET     /posts/{id}
POST    /posts
PUT     /posts/{id}
PATCH   /posts/{id}
DELETE  /posts/{id}