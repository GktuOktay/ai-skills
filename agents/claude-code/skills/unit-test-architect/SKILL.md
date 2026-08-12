---
name: unit-test-architect
description: "Comprehensive unit testing patterns, mock/stub usages, and edge-case scenario coverage. / TR: Kapsamlı birim (unit) testleri, mock/stub kullanımları ve edge-case (uç durum) senaryoları yazma becerisi."
alwaysApply: false
---

# Unit Test Architect Guidelines

As a Unit Test Architect, your goal is to ensure the reliability, maintainability, and correctness of individual code units by applying rigorous testing methodologies. You focus on isolated behavior, minimizing side effects, and ensuring edge cases are fully covered.

## Core Philosophy

1. **Isolation**: A unit test must isolate the tested unit from its dependencies.
2. **Determinism**: Tests must consistently pass or fail based purely on the code's behavior, not external factors like time, network, or filesystem.
3. **Speed**: Unit tests should execute rapidly to provide immediate developer feedback.
4. **Clarity**: Test failures must immediately point to the exact issue.

## The AAA Pattern (Arrange, Act, Assert)

Every unit test should be structured logically using the AAA pattern:

- **Arrange**: Set up the environment, initialize objects, establish mocks/stubs, and prepare data.
- **Act**: Invoke the method or behavior being tested.
- **Assert**: Verify that the expected outcome occurred (return values, state changes, or interactions).

### Code Example: AAA Pattern

```typescript
// Example using Jest
describe('ShoppingCart', () => {
  it('should calculate the total price with tax correctly', () => {
    // Arrange
    const cart = new ShoppingCart();
    const item = new Item('Laptop', 1000);
    cart.addItem(item);
    const taxRate = 0.10; // 10%

    // Act
    const total = cart.calculateTotal(taxRate);

    // Assert
    expect(total).toBe(1100);
  });
});
```

## Mocking vs. Stubbing

Understanding the distinction is critical for writing meaningful tests without over-mocking.

| Concept | Definition | When to Use |
| :--- | :--- | :--- |
| **Stub** | An object that holds predefined data and uses it to answer calls during tests. It does not fail the test. | When your unit needs data from an external dependency to execute a path. |
| **Mock** | An object that registers calls they receive. In test assertion we can verify that all expected actions were performed. | When you want to verify that an external dependency was called correctly (e.g., saving to DB, sending an email). |
| **Spy** | A wrapper around a real function that tracks calls, arguments, and return values without necessarily altering behavior. | When you need real behavior but also want to track interactions. |

### Handling Side Effects

Code that interacts with the outside world (I/O, database, API) should be abstracted.

```python
# Example using Python unittest.mock
from unittest.mock import Mock

def process_payment(payment_gateway, amount):
    if amount <= 0:
        raise ValueError("Invalid amount")
    return payment_gateway.charge(amount)

def test_process_payment_success():
    # Arrange
    mock_gateway = Mock()
    mock_gateway.charge.return_value = True
    
    # Act
    result = process_payment(mock_gateway, 100)
    
    # Assert
    assert result is True
    mock_gateway.charge.assert_called_once_with(100)
```

## Edge Cases & Boundary Value Analysis

Always consider what happens at the boundaries of your inputs.

- Null/Undefined inputs
- Empty strings, arrays, or objects
- Zero, negative numbers, maximum safe integers
- Invalid state transitions

## Mutation Testing Concepts

Going beyond code coverage, mutation testing modifies your source code in small ways (mutants) and checks if your tests fail (kill the mutant). If a test still passes despite a mutation (e.g., `>` changed to `>=`), your test suite is weak.

*Always write assertions that are strict enough to fail if the underlying logic changes.*

## Framework Agnostic Principles

Whether you are using Jest, JUnit, XCTest, or PyTest, these principles apply:
- **One assertion concept per test**: While you can have multiple `assert` statements, they should all relate to testing a single behavior.
- **Don't test the framework**: Don't write tests verifying that a built-in library function works.
- **Refactor tests like production code**: Extract common setup into helper functions or `beforeEach` blocks.

## Pre-Flight Checklist

- [ ] Does the test fail when the production code is broken? (Red-Green-Refactor)
- [ ] Is the test name descriptive? (e.g., `Should_ThrowException_When_InputIsNull`)
- [ ] Are dependencies properly mocked or stubbed?
- [ ] Are all edge cases and boundary conditions considered?
- [ ] Is there no logic (if/else, loops) inside the test itself?
