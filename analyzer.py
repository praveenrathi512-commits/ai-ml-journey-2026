import csv

# Load CSV data into a list
def load_data(filename):
  data = []
  try:
    with open(filename,newline='') as file:
      reader = csv.reader(file)
      next(reader)
      for row in reader:
        data.append(row)
  except FileNotFoundError:
    print(f'File {filename} not found')
  return data

# Calculate statistics
def calculate_average_age(data):
  total = 0 
  for row in data:
    try:
     total += int(row[1])
    except ValueError:
      print("Invalid age value:", row)
  return total / len(data)

# Filter based on conditions
def filter_by_age(data, min_age):
  filtered = []
  for row in data:
    try:
      if int(row[1]) > min_age:
        filtered.append(row)
    except ValueError:
      pass
  return filtered

# Save results to a report
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

  if not data:
    print("No data loaded.")
    return
  
  avg_age = calculate_average_age(data)
  filterd = filter_by_age(data, 25)
  write_report("report.txt", avg_age, filterd)
  print("Report generated sucessfully.")

if __name__ == "__main__":
  main()