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

The association is a HAS-A / manages relationship where an ITDepartment object manages multiple ComputerDevice objects. The department stores direct references to these devices inside its self.managed_devices list to track and manage its hardware inventory

### What multiplicity did you choose and why?

I chose a 1 to 0..* (One-to-Many) multiplicity. A single IT department naturally oversees multiple computing devices across an organization, while 0..* allows a department to exist even before devices are assigned or as inventory changes over time

### How did you implement the relationship in Python?

I initialized an empty list attribute named self.managed_devices inside ITDepartment.__init__(). I then created an add_device(self, device) method that appends complete ComputerDevice object instances directly into this list

### Why did you store an object reference instead of copying its data?

Storing an object reference ensures single-source-of-truth and real-time state updates. For example, calling dev1.report_issue() updates dev1 directly; because ITDepartment holds a reference rather than a static copy, it_dept.display_inventory() automatically reflects the updated status

### If your relationship uses many, why is a list appropriate?

A list is ideal because it dynamically scales as devices are added or removed. It stores actual object references in memory rather than plain text, allowing the department to directly call methods like dev.get_assigned_user() on every managed device
