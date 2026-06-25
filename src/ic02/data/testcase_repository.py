TESTCASE_LIBRARY = {

    "Valid Username": {

        "title": "Verify valid username",

        "priority": "High",

        "test_type": "Positive",

        "automation_candidate": True,

        "preconditions": [
            "Login page is available",
            "User account exists"
        ],

        "steps": [
            "Open login page",
            "Enter valid username"
        ],

        "expected_results": [
            "Username is accepted"
        ]
    },

    "Valid Password": {

        "title": "Verify valid password",

        "priority": "High",

        "test_type": "Positive",

        "automation_candidate": True,

        "preconditions": [
            "Username has been entered"
        ],

        "steps": [
            "Enter valid password"
        ],

        "expected_results": [
            "Password is accepted"
        ]
    },

    "Invalid Password": {

        "title": "Verify invalid password",

        "priority": "High",

        "test_type": "Negative",

        "automation_candidate": True,

        "preconditions": [
            "Valid username entered"
        ],

        "steps": [
            "Enter invalid password",
            "Click Login"
        ],

        "expected_results": [
            "Error message is displayed"
        ]
    }

}
