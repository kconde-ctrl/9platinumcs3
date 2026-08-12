# Computational Thinking Exercise

## Smart Vending Machine

**Name:** Kyle Christopher A. Conde  
**Section:** Platinum  
**Last Name:** Conde  
**Date:** August 12, 2026  

---

## Step 1: Identify the Big Problem

### Main Problem

The automated vending machine system causes delays, incorrect payments, and transaction failures because transaction processing, inventory tracking, and button-input verifications are not properly automated or synchronized in real time.

---

## Step 2: Identify the Sub-Problems

1. **Incorrect Change Calculation:** The machine fails to track coin/bill reserves accurately or calculate remaining balances, leading to incorrect change given to students.
2. **Lack of Inventory Tracking:** Food and drink items run out, but the machine does not update its display or send notifications, causing students to attempt purchasing out-of-stock items.
3. **Accidental Wrong Item Selection:** Students frequently press incorrect physical buttons or make selection mistakes without a final confirmation prompt, receiving unwanted items.
4. **Slow Multi-User Processing:** Sequentially processing one student at a time without an optimized user interface leads to long queues during short break periods.

---

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |
| :--- | :--- | :--- |
| Incorrect change given to students | Algorithm Design | Implement a step-by-step mathematical routine that calculates total inserted funds, subtracts item cost, updates physical change stock, and dispenses exact change automatically. |
| Machine does not notify when items run out | Pattern Recognition & Abstraction | Detect patterns when item counts hit zero to automatically hide or grey out unavailable products from the UI while firing an automated alert to canteen staff. |
| Students press wrong buttons and get wrong items | Decomposition | Break down the item purchasing process into three clear, independent stages: Item Selection $\rightarrow$ Visual Confirmation Prompt $\rightarrow$ Final Payment Execution. |
| Machine runs slowly for consecutive users | Abstraction | Simplify user screen options by displaying key item information (image, price, availability status) clearly to minimize decision-making time per student. |

---

## Step 4: Algorithmic Solution

### Selected Sub-Problem

Automated calculation of change and verification of funds prior to item dispensation.

### Pseudocode

START

Display available snacks and drinks on digital menu
Prompt student to select an item
Get selected_item and item_price

Prompt student to insert cash or scan payment card
Get inserted_amount

IF inserted_amount < item_price THEN
    Calculate remaining_balance = item_price - inserted_amount
    Display "Insufficient funds. Please insert remaining amount."
ELSE
    Calculate change_due = inserted_amount - item_price
    
    IF change_due > 0 THEN
        IF machine_has_change(change_due) THEN
            Dispense change_due
            Dispense selected_item
            Update inventory stock for selected_item
            Display "Transaction Successful! Enjoy your item."
        ELSE
            Refund inserted_amount
            Display "Exact change unavailable. Transaction cancelled."
        END IF
    ELSE
        Dispense selected_item
        Update inventory stock for selected_item
        Display "Transaction Successful! Enjoy your item."
    END IF
END IF

END
