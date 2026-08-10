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

    "Active User Account": {
        "title": "Verify active user account",
        "priority": "High",
        "test_type": "Positive",
        "automation_candidate": True,
        "preconditions": [
            "User account exists"
        ],
        "steps": [
            "Verify account status is Active"
        ],
        "expected_results": [
            "Active account is accepted"
        ]
    },

    "Authentication Service Available": {
        "title": "Verify authentication service availability",
        "priority": "Medium",
        "test_type": "Positive",
        "automation_candidate": True,
        "preconditions": [
            "Authentication service is running"
        ],
        "steps": [
            "Connect to authentication service"
        ],
        "expected_results": [
            "Authentication service responds successfully"
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
    },

    "Error Message Displayed": {
        "title": "Verify error message",
        "priority": "Medium",
        "test_type": "Negative",
        "automation_candidate": True,
        "preconditions": [
            "Login attempt failed"
        ],
        "steps": [
            "Observe displayed message"
        ],
        "expected_results": [
            "Correct error message is displayed"
        ]
    },

    "Username Blank": {
        "title": "Verify blank username",
        "priority": "High",
        "test_type": "Negative",
        "automation_candidate": True,
        "preconditions": [
            "Login page is available"
        ],
        "steps": [
            "Leave username blank",
            "Enter password",
            "Click Login"
        ],
        "expected_results": [
            "Username validation message is displayed"
        ]
    },

    "Validation Message Displayed": {
        "title": "Verify validation message",
        "priority": "Medium",
        "test_type": "Negative",
        "automation_candidate": True,
        "preconditions": [
            "Mandatory field is blank"
        ],
        "steps": [
            "Observe validation message"
        ],
        "expected_results": [
            "Validation message is displayed correctly"
        ]
    },

    "Password Blank": {
        "title": "Verify blank password",
        "priority": "High",
        "test_type": "Negative",
        "automation_candidate": True,
        "preconditions": [
            "Username entered"
        ],
        "steps": [
            "Leave password blank",
            "Click Login"
        ],
        "expected_results": [
            "Password validation message is displayed"
        ]
    },

    "Account Locked": {
        "title": "Verify locked account",
        "priority": "High",
        "test_type": "Negative",
        "automation_candidate": True,
        "preconditions": [
            "Locked account exists"
        ],
        "steps": [
            "Enter locked account credentials",
            "Click Login"
        ],
        "expected_results": [
            "Account locked message is displayed"
        ]
    },

    "Lock Message Displayed": {
        "title": "Verify lock message",
        "priority": "Medium",
        "test_type": "Negative",
        "automation_candidate": True,
        "preconditions": [
            "Account is locked"
        ],
        "steps": [
            "Observe displayed lock message"
        ],
        "expected_results": [
            "Correct lock message is displayed"
        ]
    }

}
