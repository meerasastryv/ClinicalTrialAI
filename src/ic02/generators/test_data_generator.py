from src.ic02.models.test_data import TestData


class TestDataGenerator:

    def generate(self, testcase):
        data = {}

        title = testcase.title.lower()

        if "username" in title:
            data["username"] = "testuser"

        if "password" in title:
            data["password"] = "Password@123"

        return TestData(
            testcase_id=testcase.test_case_id,
            input_data=data
        )
