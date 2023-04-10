# Initialize variables
ticket_counter = 2000
tickets_created = 0
tickets_resolved = 0
tickets_to_solve = 0
tickets = []

# Function to submit a new ticket
def submit_ticket():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter
    # Get input from user
    staff_id = input("Please enter your staff ID: ")
    creator_name = input("Please enter your name: ")
    contact_email = input("Please enter your contact email: ")
    print("If you require a new password, type: password change")
    description = input("Please enter a description of the issue: ")

    # Increment ticket counter and create ticket
    ticket_counter += 1
    ticket_number = ticket_counter
    # dictionary
    ticket = {
        "ticket_number": ticket_number,
        "creator_name": creator_name,
        "staff_id": staff_id,
        "contact_email": contact_email,
        "description": description,
        "response": "Not Yet Provided",
        "status": "Open"
    }
    # Add ticket to list and update ticket statistics
    tickets.append(ticket)
    tickets_created += 1
    tickets_to_solve += 1
    # Check if password change is requested
    if description.lower() == "password change":
        new_password = staff_id[:2] + creator_name[:3]
        ticket["response"] = f"New password generated: {new_password}"
        ticket["status"] = "Closed"
        print("New password generated: " + new_password)
        tickets_resolved += 1
        tickets_to_solve -= 1
        another_ticket = input("Do you want to submit another ticket? (Y/N)")
        if another_ticket == "y":
            submit_ticket()
        elif another_ticket == "n":
            action()
        else:
            print("Invalid input. Please enter Y or N.")
    else:
        another_ticket = input("Do you want to submit another ticket? (Y/N)")
        if another_ticket == "y":
            submit_ticket()
        elif another_ticket == "n":
            print("Ticket created saved.")
        else:
            print("Invalid input. Please enter Y or N.")


# Function to respond to a ticket
def respond_to_ticket():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter
    # Get input from user
    ticket_number = int(input("Please enter the ticket number: "))
    print("Type: Problem resolved/ On progress/ On hold")
    response = input("Please enter your response: ")
    # Find ticket in list and update response and status
    for ticket in tickets:
        if ticket["ticket_number"] == ticket_number:
            ticket["response"] = response
            if ticket["response"] != "Problem resolved":
                ticket["status"] = "Open"
                print("Response submitted")
            else:
                ticket["status"] = "Closed"
                tickets_resolved += 1
                tickets_to_solve -= 1

# Function to reopen a ticket
def reopen_ticket():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter
    # Get input from user
    ticket_number = int(input("Please enter the ticket number: "))
    # Find ticket in list and update status
    for ticket in tickets:
        if ticket["ticket_number"] == ticket_number:
            ticket["status"] = "Open"
            tickets_resolved -= 1
            tickets_to_solve += 1

# Function to print ticket information1
def print_tickets():
    for ticket in tickets:
        print(f"Ticket Number: {ticket['ticket_number']}")
        print(f"Ticket Creator: {ticket['creator_name']}")
        print(f"Staff ID: {ticket['staff_id']}")
        print(f"Email Address: {ticket['contact_email']}")
        print(f"Description: {ticket['description']}")
        print(f"Response: {ticket['response']}")
        print(f"Ticket Status: {ticket['status']}\n")

#funtion to display tickets stats
def display_stats():
    global tickets_resolved, tickets_to_solve, tickets_created, ticket_counter
    print("Resolved tickets: ", tickets_resolved)
    print("Open tickets: ", tickets_to_solve)
    print("Submitted tickets: ", tickets_created)


# Main loop
while True:
    # Get input from user
    action = input("Please select an action: Submit ticket (1), Respond to ticket (2), Reopen ticket (3), Print tickets (4), Display tickets stats (5), Exit (6): ")
    # Call appropriate function based on input
    if action == "1":
        submit_ticket()
    elif action == "2":
        respond_to_ticket()
    elif action == "3":
        reopen_ticket()
    elif action == "4":
        print_tickets()
    elif action == "5":
        display_stats()
    elif action == "6":
        break
    else:
        print("Invalid")
