# Travel Fare Calculator & Trip Planner

# # Scenario

# A transport company, *Swift Travels Ghana*, wants a simple system that helps passengers calculate the cost of their journey before purchasing a ticket.

# When the program starts, display the following menu repeatedly until the user chooses to exit.

# text
# ====================================
# SWIFT TRAVELS GHANA
# Travel Fare Calculator
# ====================================

# 1. Book a Trip
# 2. View Today's Statistics
# 3. Exit

# Choose an option:


# ---

# # Feature 1 – Book a Trip

# Ask the passenger to enter:

# * Full Name
# * Age
# * Departure City
# * Destination City
# * Seat Class

#   * Standard
#   * VIP
# * Number of Tickets

# ---

# ## Route Prices

# | Route            | Standard |     VIP |
# | ---------------- | -------: | ------: |
# | Accra → Kumasi   |  GHS 120 | GHS 180 |
# | Accra → Takoradi |  GHS 100 | GHS 160 |
# | Accra → Tamale   |  GHS 220 | GHS 300 |
# | Kumasi → Tamale  |  GHS 180 | GHS 250 |

# ---

# ## Discount Rules

# Apply *only one* of the following discounts.

# | Passenger            | Discount |
# | -------------------- | -------: |
# | Child (below 12)     |      50% |
# | Senior Citizen (60+) |      30% |
# | No Discount          |       0% |

# ---

# ## Group Discount

# If the passenger purchases *4 or more tickets, apply an additional **10% discount* to the final bill.

# ---

# ## Calculate

# Your program should determine:

# * Ticket price
# * Total before discount
# * Discount amount
# * Final amount payable

# ---

# ## Trip Summary

# Display

# text
# ==============================

# TRIP CONFIRMATION

# ==============================

# Passenger Name

# Departure

# Destination

# Seat Class

# Number of Tickets

# Discount Applied

# Amount Payable

# Thank You for Choosing Swift Travels

# ==============================


# ---

# # Feature 2 – Today's Statistics

# Display:

# * Total passengers served
# * Total tickets sold
# * Standard tickets sold
# * VIP tickets sold
# * Children served
# * Senior citizens served
# * Total revenue collected
# * Average amount paid per booking

# ---

# # Feature 3 – Exit

# Before closing,

# Ask

# text
# Are you sure you want to exit?

# (Y/N)


# ---

# # Input Validation

# Your program must reject:

# * Negative ages
# * Zero or negative ticket quantities
# * Invalid menu selections
# * Invalid seat class
# * Invalid route selection
# * Empty names

# Continue requesting input until a valid value is entered.

# ---

# # Programming Requirements

# Your solution *must* include:

# * At least one while loop
# * At least one for loop
# * if, elif, and else
# * Arithmetic operators
# * Comparison operators
# * Logical operators (and, or)
# * Clear and meaningful variable names
# * Comments explaining important sections of your code

# ---

# # Bonus Challenge (Optional)

# Attempt any *two* of the following:

# * Allow passengers to book multiple trips before returning to the main menu.
# * Print a unique ticket number (e.g., ST1001).
# * Display the most popular destination.
# * Display the passenger who paid the highest fare.
# * Allow passengers to cancel a booking before payment.

# ---

# # Submission Instructions

# Submit the following:

# 1. Your Python source code (.py).
# 2. A screenshot showing your program running successfully.
# 3. Push your solution to your personal GitHub repository.
# 4. Submit only the GitHub repository link.