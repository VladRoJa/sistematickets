# app/controllers/ticket_controller.py
from flask import jsonify, session, request
from app.models.ticket_model import create_ticket, get_tickets, update_ticket_status

class TicketController:
    def create_ticket(self, data):
        titulo = data.get('titulo')
        descripcion = data.get('descripcion')
        username = data.get('username')
        sucursal_id = session.get('sucursal_id')
        ticket = create_ticket(titulo, descripcion, username, sucursal_id)
        return jsonify({
            'mensaje': 'Ticket creado exitosamente',
            'id': ticket['id'],
            'estado': ticket['estado'],
            'fecha_creacion': ticket['fecha_creacion']
        }), 201

    def get_tickets(self, estado):
        sucursal_id = session.get('sucursal_id')
        limit = request.args.get('limit', default=None, type=int)
        sort = request.args.get('sort', default=None, type=str)
        tickets = get_tickets(estado, sucursal_id, limit, sort)
        return tickets, 200

    def update_ticket_status(self, id, data):
        nuevo_estado = data.get('estado')
        ticket = update_ticket_status(id, nuevo_estado)
        if ticket:
            return jsonify({
                'mensaje': 'Estado del ticket actualizado exitosamente',
                'ticket': ticket
            }), 200
        else:
            return jsonify({'mensaje': 'Ticket no encontrado'}), 404

# Crea una instancia de la clase
ticket_controller = TicketController()