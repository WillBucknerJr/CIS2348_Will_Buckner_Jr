# Will Buckner Jr#
# PSID: 2101260#
main_text = input()
text_list = main_text.split(" ")
text_lists = list(map(int, text_list))
final_list = []

for x in text_lists:
    if x > -1:
        final_list.append(x)

final_list = sorted(final_list)
for x in final_list:
    print(f"{x}", end=" ")
