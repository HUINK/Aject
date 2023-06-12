# number_of_packages_sent = ""
# total_weight_of_packages_sent = 0
# #   Total 'unused' capacity (non-optimal packaging). This is calculated as the number of packages sent multiplied by 20 kg, minus the total weight of packages sent.
# #   The package number that had the most 'unused' capacity and the amount of 'unused' capacity in that package.
# while True:
#     final_box = input("\n how many of packages you sent?: ")
#     if not final_box:
#         continue
#     elif final_box == "back":
#         break
#
#     box_weight = int(input("\nwhat is your package weight(kg)?: "))
#     numbers_of_packages = int(input("\n how many box you want to sent?: "))
#
#     if number_of_packages_sent:
#         number_of_packages_sent = number_of_packages_sent + "," + final_box
#     else:
#         numbers_of_packages_sent = final_box
#
#     total_weight_of_packages_sent += box_weight * numbers_of_packages
#
# total_weight_of_packages_sent /= 20
#
# print(f"\npackages you sent: {numbers_of_packages_sent} total boxes you sent is{total_weight_of_packages_sent} boxes")

# 1
num_items = int(input("\nhow many of item you sent?: "))

index_counter = 0
num_packages = 0
current_package_weight = 0
total_weight_package = 0
# most_unused_pack_number = 0
# most_unused_pack_cap = 0

# 2
while True:
    index_counter = index_counter + 1
    item_weight = int(input("\nwhat is your item "+ str(index_counter) +" weight(kg)?: "))

    # 3
    current_package_weight = current_package_weight + item_weight

    total_weight_package = total_weight_package + item_weight

    if current_package_weight > 20:
        num_packages = num_packages + 1
        current_package_weight = item_weight
    elif current_package_weight == 20:
        num_packages = num_packages + 1
        current_package_weight = 0

    # 4
    if item_weight == 0:
        num_packages = num_packages + 1
        break

#5
print(f"\nNumber of packages sent: {num_packages}")
print(f"Total weight of packages sent: {total_weight_package}")

total_unused = num_packages * 20 - total_weight_package
print(f"Total 'unused' capacity: {total_unused}")