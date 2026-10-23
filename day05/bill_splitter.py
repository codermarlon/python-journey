def calculate_split(bill, tip_percentage, num_of_people):
    tip = bill * tip_percentage / 100
    total = bill + tip
    per_person = total / num_of_people
    return tip, total, per_person

bill_amount = float(input("Bill amount: $ "))
tip_percent = int(input("Tip percentage: % "))
people = int(input("Number of people: "))

tip_amount, bill_total, each_person = calculate_split(bill_amount, tip_percent, people)

print("-----------Bill Summary-------------")
print(f"{'Bill':<25}: {'$'}{bill_amount:>6.2f}")
print(f"{'Tip(':<5}{tip_percent:<3} {'%)':<16}: ${tip_amount:>6.2f}")
print(f"{'Total':<25}: ${bill_total:>6.2f}")
print(f"{'Per person':<25}: ${each_person:>6.2f}")

