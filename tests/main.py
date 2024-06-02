from src.df import filter_by_state, sort_by_date
from src.widget import mask_number, refactor_the_date

card_num1 = "Visa Platinum 7000 7922 8960 6361"
card_num2 = "Maestro 1596837868705199"
acc_num1 = "Счет 64686473678894779589"
acc_num2 = "Счет 73654108430135874305"
date1 = "2018-07-11T02:26:18.671407"
date2 = "2023-08-19T13:21:86.675477"
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


print(mask_number(card_num1))
print(mask_number(card_num2))
print(mask_number(acc_num1))
print(mask_number(acc_num2))
print(refactor_the_date(date1))
print(refactor_the_date(date2))
print("Filtered by state ('EXECUTED'):")
for i in filter_by_state:
    print(i)

print("\nSorted by date (descending):")
for i in sort_by_date:
    print(i)
