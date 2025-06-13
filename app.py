from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for orders and logs
orders = {}
action_logs = []

def log_action(action_type, performed_by, order_id=None):
    """Helper function to log actions"""
    log_entry = {
        'action_type': action_type,
        'performed_by': performed_by,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'order_id': order_id
    }
    action_logs.append(log_entry)

@app.route('/')
def index():
    return render_template('orders.html', orders=orders, logs=action_logs[-10:])

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        order_id = str(uuid.uuid4())
        orders[order_id] = {
            'num_items': request.form['num_items'],
            'delivery_date': request.form['delivery_date'],
            'sender_name': request.form['sender_name'],
            'recipient_name': request.form['recipient_name'],
            'recipient_address': request.form['recipient_address'],
            'status': 'Ongoing'
        }
        log_action('Created', request.form.get('performed_by', 'System'), order_id)
        return redirect(url_for('index'))
    return render_template('add_order.html')

@app.route('/edit_order/<order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    if order_id not in orders:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        orders[order_id] = {
            'num_items': request.form['num_items'],
            'delivery_date': request.form['delivery_date'],
            'sender_name': request.form['sender_name'],
            'recipient_name': request.form['recipient_name'],
            'recipient_address': request.form['recipient_address'],
            'status': orders[order_id]['status']  # Keep existing status
        }
        log_action('Edited', request.form.get('performed_by', 'System'), order_id)
        return redirect(url_for('index'))
    
    return render_template('edit_order.html', order=orders[order_id], order_id=order_id)

@app.route('/mark_delivered/<order_id>')
def mark_delivered(order_id):
    if order_id in orders:
        orders[order_id]['status'] = 'Delivered'
        log_action('Marked Delivered', request.args.get('performed_by', 'System'), order_id)
    return redirect(url_for('index'))

@app.route('/delete_order/<order_id>')
def delete_order(order_id):
    if order_id in orders:
        del orders[order_id]
        log_action('Deleted', request.args.get('performed_by', 'System'), order_id)
    return redirect(url_for('index'))

@app.route('/logs')
def view_logs():
    return render_template('logs.html', logs=action_logs)

if __name__ == '__main__':
    app.run(debug=True)