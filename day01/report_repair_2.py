with open('input.txt') as report:
    report_list = report.readlines()
report_list = [int(x.strip()) for x in report_list]

list_length = len(report_list)

for entry in report_list:
    for i in range(report_list.index(entry) + 1, list_length):
        for j in range(i + 1, list_length):
            first_num = report_list[report_list.index(entry)]
            second_num = report_list[i]
            third_num = report_list[j]
            num_sum = first_num + second_num + third_num
            if num_sum == 2020:
                print(str(first_num) + " + " + str(second_num) + " + " + str(third_num) + " = " + str(num_sum))
                solution = first_num * second_num * third_num
                print(solution)
