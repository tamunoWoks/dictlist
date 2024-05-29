def main():
    info = [
        {
            "fname": "Tammy",
            "lname": "Wokoma",
            "hometown": "Buguma",
            "status": "is Married",
        },
        {
            "fname": "Esther",
            "lname": "Dimkpa",
            "hometown": "Ebubu",
            "status": "is Married",
        },
        {
            "fname": "Nene",
            "lname": "Nnaji",
            "hometown": "Nbawsi",
            "status": "is Single",
        },
        {"fname": "Ibiba", "lname": "Longjohn", "hometown": "Bonny", "status": None},
    ]
    for people in info:
        people["status"] = (
            people["status"] if people["status"] is not None else "status is unknown"
        )
        print(
            f"{people['fname']} {people['lname']} is from {people['hometown']} and {people['status']}"
        )


if __name__ == "__main__":
    main()
