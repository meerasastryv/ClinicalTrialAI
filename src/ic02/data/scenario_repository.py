SCENARIO_LIBRARY = {

    "login": [
        ("Successful Login", "Positive"),
        ("Invalid Password", "Negative"),
        ("Empty Username", "Negative"),
        ("Empty Password", "Negative"),
        ("Locked Account", "Negative")
    ],

    "search": [
        ("Valid Search", "Positive"),
        ("No Results Found", "Negative"),
        ("Special Character Search", "Negative")
    ],

    "upload": [
        ("Valid File Upload", "Positive"),
        ("Invalid File Type", "Negative"),
        ("Oversized File Upload", "Negative")
    ]
}
