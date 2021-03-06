"""
API views
"""

from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from application import models, logger
from application.utils import json_resp
from . import api_blueprint


class TicketRegistrationView(MethodView):
    """
    Ticket Registration
    """

    def post(self):
        try:
            request_data = request.get_json()

            uid = request_data.get('uid', None)

            if not uid:
                return jsonify(
                    json_resp("Failure", "Failed to get ticket ID")), 400

            trips = request_data.get('trips', 1)

            ticket = models.Ticket(uid=uid, available_trips=trips)
            ticket.save()

            logger.info(f"New ticket registered. UID: {ticket.uid}")

            return jsonify(json_resp("Success", "Ticket added")), 201

        except IntegrityError as e:
            logger.error(e)

            return jsonify(
                json_resp("Failure", "Ticket ID already exists")), 400

        except Exception as e:
            logger.error(e)

            return jsonify(json_resp("Fail", "Some error occurred")), 500


class PaymentView(MethodView):
    """
    Payment endpoint
    """

    def post(self):
        try:
            data = request.get_json()
            uid = data.get('uid', None)

            if not uid:
                return jsonify(
                    json_resp("Failure", "Failed to get ticket ID")), 400

            ticket = models.Ticket.query.filter_by(uid=uid).one_or_none()

            if not ticket:
                logger.info(f"Payment failure. Ticket not found. UID: {uid}")

                return jsonify(
                    json_resp("Failure", "Ticket not found")), 404

            if ticket.available_trips < 1:
                logger.info(
                    f"Payment failure. Reason: no available trips. Ticket UID: {ticket.uid}")

                return jsonify(
                    json_resp("Failure",
                              "Ticket does not have available trips. Please refill")), 403
            else:
                ticket.available_trips -= 1
                ticket.save()

                logger.info(f"Payment success. Ticket UID: {ticket.uid}")

                return jsonify(json_resp("Success", "Payment successful")), 200

        except Exception as e:
            logger.error(e)

            return jsonify(json_resp("Failure", "Some error occurred")), 500


class TicketRefillView(MethodView):
    """
    Refill ticket
    """

    # TODO: add authorization
    def post(self):
        try:
            data = request.get_json()
            uid = data.get('uid', None)

            if not uid:
                return jsonify(
                    json_resp("Failure", "Failed to get ticket ID")), 400

            trips = data.get('trips', None)

            if not trips:
                return jsonify(
                    json_resp("Failure", "Please provide trips number")), 400

            ticket = models.Ticket.query.filter_by(uid=uid).one_or_none()

            if not ticket:
                return jsonify(
                    json_resp("Failure", "Ticket not found")), 404

            ticket.available_trips += trips
            ticket.save()

            logger.info(f"Successful ticket refill. Ticket UID: {ticket.uid}")

            return jsonify(json_resp("Success", "Refill successful")), 200

        except Exception as e:
            logger.error(e)

            return jsonify(json_resp("Failure", "Some error occurred")), 500


# =====================   Register endpoints   ==============================

api_blueprint.add_url_rule('/register',
                           view_func=TicketRegistrationView.as_view(
                               'ticket_registration'),
                           methods=['POST'])

api_blueprint.add_url_rule('/pay',
                           view_func=PaymentView.as_view('payment'),
                           methods=['POST'])

api_blueprint.add_url_rule('/refill',
                           view_func=TicketRefillView.as_view('refill'),
                           methods=['POST'])
