class Evaluator:

    @staticmethod
    def evaluate_mcqs(user, correct):
        score = sum(1 for u, c in zip(user, correct) if u == c)
        percent = int((score / len(correct)) * 100)
        return score, percent

    @staticmethod
    def run_coding_test(code, test_cases):
        try:
            local_env = {}
            exec(code, {}, local_env)

            if "solution" not in local_env:
                return False, "Function 'solution' not found."

            fn = local_env["solution"]

            for t in test_cases:
                if fn(*t["input"]) != t["expected"]:
                    return False, "Incorrect output for test case."

            return True, "All tests passed."

        except Exception as e:
            return False, str(e)
