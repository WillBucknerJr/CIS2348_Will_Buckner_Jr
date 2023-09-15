#Will Buckner Jr#
#PSID: 2101260#

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")
Services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12, "-": "No service"}

first_service = input("Select first service:")
second_service = input("\nSelect second service:\n")
if first_service == "-":
    print("\nDavy's auto shop invoice")
    print(f"\nService 1: {Services[first_service]}")
    print(f"Service 2: {second_service}, ${Services[second_service]}\n")
    print(f"Total: ${Services[second_service]}")
elif second_service == "-":
    print("\nDavy's auto shop invoice")
    print(f"\nService 1: {first_service}, ${Services[first_service]}")
    print(f"Service 2: {Services[second_service]}\n")
    print(f"Total: ${Services[first_service]}")
else:
    print("\nDavy's auto shop invoice")
    print(f"\nService 1: {first_service}, ${Services[first_service]}")
    print(f"Service 2: {second_service}, ${Services[second_service]}\n")
    print(f"Total: ${(Services[first_service] + Services[second_service])}")

