import csv

def load_data(filename):
  data = []
  with open(filename,newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      data.append(row)
  return data

def calculate_average_age(data):
  total = 0 
  for row in data:
    total += int(row[1])
  return total / len(data)

def filter_by_age(data, min_age):
  filtered = []
  for row in data:
    if int(row[1]) > min_age:
      filtered.append(row)
  return filtered

def write_report(filename, avg_age, filterd):
  with open(filename, "w") as file:
    file.write("DATA ANALYSIS REPORT\n")
    file.write("---------------------\n")
    file.write(f"Average Age: {avg_age}\n\n")
    file.write("People with age >= 25:\n")
    for row in filterd:
      file.write(f"{row[0]} ({row[1]}) - {row[2]}\n")

def main():
  data = load_data("people.csv")
  avg_age = calculate_average_age(data)
  filterd = filter_by_age(data, 25)
  write_report("report.txt", avg_age, filterd)
  print("Report generated sucessfully.")

main()