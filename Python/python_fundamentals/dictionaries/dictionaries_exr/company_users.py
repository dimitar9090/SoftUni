companies = {}
while True:
    current_command = input()
    if current_command == "End":
        break
    company_name, id_of_employer = current_command.split(" -> ")
    if company_name not in companies:
        companies[company_name] = []
    if id_of_employer not in companies[company_name]:
        companies[company_name].append(id_of_employer)
for name, id_ in companies.items():
    print(name)
    print("-- ", end="")
    print("\n-- ".join(id_))


