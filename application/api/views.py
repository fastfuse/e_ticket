"""
API views
"""
import uuid

from flask import request, jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from voluptuous import MultipleInvalid

from application import models, logger
from application.utils import json_resp, BASE_SCHEMA, PAYMENT_SCHEMA, REFILL_SCHEMA
from . import api_blueprint

SUCCESS = 'success'
FAILURE = 'failure'


class TicketRegistrationView(MethodView):
    """
    Ticket Registration
    """

    def post(self):
        try:
            data = request.get_json()

            try:
                BASE_SCHEMA(data)
            except MultipleInvalid as e:
                return jsonify(
                    json_resp("Failure", str(e))), 400

            ticket_uid = data['ticket_uid']
            ticket = models.Ticket(uid=ticket_uid, available_trips=1)
            ticket.save()

            logger.info(f"New ticket registered. UID: {ticket.uid}")

            return jsonify(json_resp("Success", "Ticket added")), 201

        except IntegrityError as e:
            logger.error(e)

            return jsonify(
                json_resp("Failure", "Ticket ID already exists")), 400

        except Exception as e:
            logger.error(e)

            return jsonify(json_resp("Failure", "Some error occurred")), 500


class PaymentView(MethodView):
    """
    Payment endpoint
    """

    def post(self):
        try:
            data = request.get_json()

            try:
                PAYMENT_SCHEMA(data)
            except MultipleInvalid as e:
                return jsonify(
                    json_resp("Failure", str(e))), 400

            ticket = models.Ticket.query.filter_by(uid=data['ticket_uid']).one_or_none()
            reader = models.Reader.query.filter_by(uid=data['reader_uid']).one_or_none()

            if not ticket:
                logger.info(
                    f"Payment failure. Ticket not found")

                return jsonify(
                    json_resp("Failure", "Ticket not found")), 404

            if not reader:
                logger.info(
                    f"Payment failure. Reader not found")

                return jsonify(
                    json_resp("Failure", "Reader not found")), 404

            # create transaction
            transaction = models.Transaction(uid=uuid.uuid4(),
                                             ticket_id=ticket.id,
                                             reader_id=reader.id)

            if ticket.available_trips < 1:
                logger.info(
                    f"Payment failure. Reason: no available trips. Ticket UID: {ticket.uid}")

                transaction.status = FAILURE
                transaction.save()

                return jsonify(
                    json_resp("Failure",
                              "Ticket does not have available trips. Please refill")), 403
            else:
                ticket.available_trips -= 1
                ticket.save()

                transaction.status = SUCCESS
                transaction.save()

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

            try:
                REFILL_SCHEMA(data)
            except MultipleInvalid as e:
                return jsonify(
                    json_resp("Failure", str(e))), 400

            ticket = models.Ticket.query.filter_by(uid=data['ticket_uid']).one_or_none()

            if not ticket:
                return jsonify(
                    json_resp("Failure", "Ticket not found")), 404

            trips = data.get('trips', 1)

            ticket.available_trips += trips
            ticket.save()

            logger.info(f"Successful ticket refill. Ticket UID: {ticket.uid}")

            return jsonify(json_resp("Success", "Refill successful")), 200

        except Exception as e:
            logger.error(e)

            return jsonify(json_resp("Failure", "Some error occurred")), 500


class TicketValidationView(MethodView):
    """
    Validate ticket
    """

    def post(self):
        try:
            data = request.get_json()

            try:
                PAYMENT_SCHEMA(data)
            except MultipleInvalid as e:
                return jsonify(
                    json_resp("Failure", str(e))), 400

            ticket = models.Ticket.query.filter_by(uid=data['ticket_uid']).one_or_none()
            reader = models.Reader.query.filter_by(uid=data['reader_uid']).one_or_none()

            if not ticket:
                logger.info(
                    f"Payment failure. Ticket not found")

                return jsonify(
                    json_resp("Failure", "Ticket not found")), 404

            if not reader:
                logger.info(
                    f"Payment failure. Reader not found")

                return jsonify(
                    json_resp("Failure", "Reader not found")), 404

            transactions = models.Transaction.query.filter_by(ticket_id=ticket.id).all()

            if transactions:
                return transactions[-1].timestamp

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

api_blueprint.add_url_rule('/validate',
                           view_func=TicketValidationView.as_view('validation'),
                           methods=['POST'])
