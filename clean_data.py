import re
import csv

month_mapping = {
    'มกราคม': '01',
    'กุมภาพันธ์': '02',
    'มีนาคม': '03',
    'เมษายน': '04',
    'พฤษภาคม': '05',
    'มิถุนายน': '06',
    'กรกฎาคม': '07',
    'สิงหาคม': '08',
    'กันยายน': '09',
    'ตุลาคม': '10',
    'พฤศจิกายน': '11',
    'ธันวาคม': '12'
}

output_lines = []

with open('raw_lottery_result.txt', 'r') as file:
    for line in file:
        # print("line", line)
        count = 0
        for char in line:
            if char.isdigit():
                count += 1
            elif char.isalpha():
                break

        if count < 2:
            line = "0" + line

        # print("line", line)
        split = 0
        day = line[0:2]
        split += len(day)
        # print("day", day)

        th_month = re.findall("[ก-๙เแไใๆ]+", line)
        month = month_mapping[th_month[0]]
        split += len(th_month[0])
        # print("month", month)

        year = line[split:split+4]
        split += len(year)
        # print("year", year)

        one_prize = line[split:split+6]
        split += len(one_prize)
        # print("one_prize", one_prize)

        two_top = line[split:split+2]
        split += len(two_top)
        # print("two_top", two_top)

        three_top = line[split:split+3]
        split += len(three_top)
        # print("three_top", three_top)

        two_low = line[split:split+2]
        split += len(two_low)
        # print("two_top", two_low)

        three_fronts_three_bottoms_1 = line[split:split+3]
        split += len(three_fronts_three_bottoms_1)
        # print("three_fronts_three_bottoms_1", three_fronts_three_bottoms_1)

        three_fronts_three_bottoms_2 = line[split:split+3]
        split += len(three_fronts_three_bottoms_2)
        # print("three_fronts_three_bottoms_2", three_fronts_three_bottoms_2)

        three_fronts_three_bottoms_3 = line[split:split+3]
        split += len(three_fronts_three_bottoms_3)
        # print("three_fronts_three_bottoms_3", three_fronts_three_bottoms_3)

        three_fronts_three_bottoms_4 = line[split:split+3]
        split += len(three_fronts_three_bottoms_4)
        # print("three_fronts_three_bottoms_4", three_fronts_three_bottoms_4)

        # For txt file
        # new_line = f"{day}/{month}/{year},{one_prize},{two_top},{three_top},{two_low},{three_fronts_three_bottoms_1},{three_fronts_three_bottoms_2},{three_fronts_three_bottoms_2},{three_fronts_three_bottoms_4}"
        # output_lines.append(new_line)

        # For csv file
        new_line = [f"{day}/{month}/{year}", one_prize, two_top, three_top, two_low, three_fronts_three_bottoms_1,
                    three_fronts_three_bottoms_2, three_fronts_three_bottoms_2, three_fronts_three_bottoms_4]
        output_lines.append(new_line)

# # Write the modified lines to a new file
# with open('clean_lottery_result.txt', 'w') as file:
#     file.write('\n'.join(output_lines))

# Write the modified lines to a CSV file
with open('clean_lottery_result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    header = ["Date", "1st", "2T", "3T", "2L", "3F3L(1)",
              "3F3L(2)", "3F3L(3)", "3F3L(4)"]
    writer.writerow(header)
    writer.writerows(output_lines)