class CoverageAnalyzer:
    """
    Analyzes the coverage of generated test artifacts.
    """

    def analyze(self, results):
        total_scenarios = len(results)

        total_conditions = 0
        total_testcases = 0
        positive = 0
        negative = 0

        for scenario_result in results:

            conditions = scenario_result["conditions"]
            total_conditions += len(conditions)

            for condition_result in conditions:
                testcases = condition_result["testcases"]
                total_testcases += len(testcases)
                #for testcase in testcases:
                #    title = testcase.title.lower()
                #    if any(word in title for word in [
                #        "valid",
                #        "success",
                #        "positive"
                #    ]):
                #        positive += 1
                #    else:
                #        negative += 1
                for testcase in testcases:
                    if testcase.test_type.lower() == "positive":
                        positive += 1
                    else:
                        negative += 1

        coverage = {
            "scenario_count": total_scenarios,
            "condition_count": total_conditions,
            "testcase_count": total_testcases,
            "positive_testcases": positive,
            "negative_testcases": negative,
            "coverage_score": 100 if total_testcases > 0 else 0
        }

        return coverage
