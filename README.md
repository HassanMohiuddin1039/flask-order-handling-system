# flask-order-handling-system
A Flask-based Order Handling System for Galvan AI Internship Task
Repository Structure

order-handling-system/         
static/
styles.css            # CSS styles for the application      

templates/       
base.html            # Base template with common layout,       
orders.html          # Main orders listing page,        
add_order.html       # Form to add new orders,        
edit_order.html      # Form to edit existing orders,        
logs.html            # Page displaying all action logs

app.py                   # Main Flask application file        
requirements.txt          # Python dependencies        
README.md                # This documentation file       

Approach
Core Features Implementation

Order Management:
Used Python dictionaries for in-memory storage of orders
Implemented CRUD operations (Create, Read, Update, Delete)
Added status tracking with default "Ongoing" state

Action Logging:
Created a logging system that records all operations
Stored timestamp, action type, performer, and order ID
Displayed recent logs on the main page

User Interface:
Developed a clean, responsive interface with Bootstrap-inspired styling
Added Font Awesome icons for better visual cues
Implemented card-based layout for better content organization

Technical Decisions
Storage:
Used in-memory storage for simplicity in this demo

Frontend:
Created a custom CSS stylesheet for consistent styling
Used semantic HTML for better accessibility
Implemented responsive design principles

Security:
Basic form validation implemented

Installation Instructions
Clone the repository:
git clone https://github.com/HassanMohiuddin1039/order-handling-system.git
cd order-handling-system
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
pip install -r requirements.txt
Run the application:
python app.py
Access the application at:
http://localhost:5000

Usage Instructions
Viewing Orders:
The home page displays all orders in a table
Recent actions are shown at the bottom

Adding an Order:
Click "Add Order" in the navigation
Fill out the form and submit

Editing an Order:
Click the "Edit" button next to any order
Modify the information and submit

Marking as Delivered:
Click the "Deliver" button next to ongoing orders

Deleting an Order:
Click the "Delete" button next to any order

Viewing Logs:
Click "View Logs" in the navigation to see all actions

Features
Order Management:
Add new orders with all required fields
Edit existing orders
Mark orders as delivered
Delete orders

Tracking:
Automatic logging of all actions
Timestamp recording for all operations
Visual status indicators

User Interface:
Clean, modern design
Responsive layout
Intuitive navigation

Dependencies
Python 3.x
Flask 2.0+
