sessions = {}


def add_message(session_id: str, role: str, message: str):

    if session_id not in sessions:
        sessions[session_id] = []

    sessions[session_id].append({
        "role": role,
        "message": message
    })

    # Keep only last 20 messages
    sessions[session_id] = sessions[session_id][-20:]


def get_session(session_id: str):

    return sessions.get(session_id, [])


def clear_session(session_id: str):

    if session_id in sessions:
        del sessions[session_id]

def delete_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
        return True
    return False