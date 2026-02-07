class InterviewOrchestrator:
    def __init__(self):
        self.rounds = {
            "ROUND_1": "General Screening",
            "ROUND_2": "Technical Deep Dive",
            "ROUND_3": "Coding Challenge"
        }

    def get_status_message(self, current_step):
        messages = {
            "START": "Candidate has entered the portal. Waiting for initialization...",
            "ROUND_1": "Agent is generating behavioral and general CS questions...",
            "ROUND_2": "Screening passed. Agent is preparing technical MCQs...",
            "ROUND_3": "Technical MCQs passed. Spinning up secure coding environment...",
            "DECISION": "All data points collected. Synthesizing final hiring decision...",
            "REJECTED": "Candidate failed to meet the threshold. Closing session."
        }
        return messages.get(current_step, "Processing...")