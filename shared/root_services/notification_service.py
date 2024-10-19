from flask import Blueprint, jsonify, request
from notification_manager import NotificationManager

notification_bp = Blueprint('notification', __name__)
notification_manager = NotificationManager()

@notification_bp.route('/notifications', methods=['GET'])
def get_notifications():
    user_id = request.args.get('user_id')
    notifications = notification_manager.get_unread_notifications(user_id)
    return jsonify([notification.message for notification in notifications])

@notification_bp.route('/notifications/read', methods=['POST'])
def mark_notification_as_read():
    notification_id = request.json.get('notification_id')
    notification_manager.mark_as_read(notification_id)
    return jsonify({"message": "Notification marked as read"})
