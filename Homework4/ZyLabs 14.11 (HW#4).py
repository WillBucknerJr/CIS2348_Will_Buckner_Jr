# Will Buckner Jr#
# PSID: 2101260#

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        max_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_index]:
                max_index = j

        # Swap the found maximum element with the first element
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

        # Output the list after each iteration of the outer loop
        together = ' '.join(map(str, numbers))
        print(f"{together} ")


if __name__ == "__main__":
    input_list = input()
    numbers1 = [int(x) for x in input_list.split()]
    selection_sort_descend_trace(numbers1)
