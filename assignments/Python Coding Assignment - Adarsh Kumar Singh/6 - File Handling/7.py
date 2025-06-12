import csv

def calculate_column_averages(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        sums = [0.0] * len(headers)
        counts = [0] * len(headers)

        for row in reader:
            for i in range(len(row)):
                try:
                    value = float(row[i])
                    sums[i] += value
                    counts[i] += 1
                except ValueError:
                    continue

        averages = []
        for i in range(len(headers)):
            if counts[i] > 0:
                avg = sums[i] / counts[i]
                averages.append((headers[i], avg))

        return averages

filename = 'data.csv'
averages = calculate_column_averages(filename)

for col, avg in averages:
    print(f"Average of '{col}': {avg:.2f}")
