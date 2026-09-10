# Class Relationships: Association and Multiplicity

## Previous Work

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class

Class: Computer Device

Description: Represents a physical computer workstation device managed within a computer laboratory system. It tracks the hardware specifications, operational status and assignment details of a desktop or laptop unit
Properties

## New Related Class

Class: ITDepartment

Description: Represents an IT department or laboratory unit that manages and maintains multiple computing hardware devices

## Association

Relationship: HAS-A manages

Explanation: ITDepartment manages ComputerDevice

## Multiplicity

Multiplicity: 1 : 0

Explanation: One ITDepartment manages zero or many ComputerDvices

## UML Class Relationship Diagram

![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation

[View Python Source](classRelationships.py)

## Test Run

![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram

![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?

### What multiplicity did you choose and why?

### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?
