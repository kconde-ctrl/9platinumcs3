# Class Attributes and Methods

## Previous Design
Link to my previous activity: [classObjectUML.md](classObjectUML.md)

## Design Revision
No major structural changes were made to the attributes or methods. The visibility modifier for `assignedUser` was set to private (`-`) to ensure data encapsulation, while other properties remain public (`+`).

## Visibility Decisions

| Attribute | Data Type | Visibility | Reason |
| --- | --- | --- | --- |
| `deviceID` | `string` | Public | Necessary for general system lookup and asset tracking across the organization. |
| `isFunctional` | `boolean` | Public | System operators need quick visibility into operational readiness. |
| `ramGB` | `int` | Public | System specifications are public metadata required for resource allocation. |
| `assignedUser` | `string` | Private | Sensitive user association data that must only be updated via strict validation methods. |

## Updated UML Class Diagram

![Updated Class Diagram](images/UpdatedclassDiagram.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run Output
```text
--- BEFORE ---
Device 1 (DEV-101): User = Alice, Functional = True
Device 2 (DEV-102): User = Bob, Functional = True

--- Performing action on Object 1 ---
Device DEV-101 successfully assigned to Charlie.
Issue reported: Device DEV-101 status set to non-functional.

--- AFTER ---
Device 1 (DEV-101): User = Charlie, Functional = False
Device 2 (DEV-102): User = Bob, Functional = True
