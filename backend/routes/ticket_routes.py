from flask import Blueprint, request, jsonify
from services.classifier import classify_ticket
from services.rag_engine import get_similar_solution, get_similar_tickets
from services.llm_service import generate_solution
from services.priority_service import detect_priority
from services.assignment_service import assign_team
from services.impact_service import predict_impact
from services.learning_service import save_incident

ticket_bp = Blueprint("ticket", __name__)

@ticket_bp.route("/analyze", methods=["POST"])
def analyze_ticket():

    data = request.json
    ticket = data.get("ticket")
    impact = predict_impact(ticket)
    category = classify_ticket(ticket)
    assigned_team = assign_team(ticket, category)
    similar_solution = get_similar_solution(ticket)
    ai_solution = generate_solution(ticket, similar_solution)
    save_incident(ticket, ai_solution)
    priority = detect_priority(ticket)
    similar_tickets = get_similar_tickets(ticket)

    return jsonify({
        "ticket": ticket,
        "category": category,
        "priority": priority,
        "assigned_team": assigned_team,
        "ai_solution": ai_solution,
        "similar_tickets": similar_tickets,
        "impact_analysis": impact,
    })