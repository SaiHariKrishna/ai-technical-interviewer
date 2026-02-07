class DecisionAgent:
    @staticmethod
    def provide_verdict(scores):
        r1 = scores.get('r1', 0)
        r2 = scores.get('r2', 0)
        coding = scores.get('coding', False)

        if r1 >= 70 and r2 >= 70 and coding:
            return "SELECTED", "The candidate exhibits strong theoretical foundations and practical coding skills. High potential for the role."
        elif coding and (r1 >= 60 or r2 >= 60):
            return "FOLLOW-UP", "Strong coding skills but inconsistent theoretical knowledge. Recommend a live technical interview."
        else:
            return "REJECTED", "Candidate failed to meet the minimum proficiency threshold in technical or fundamental rounds."