import subprocess
import csv

# Pobierz logi Gita
log = subprocess.check_output(
    ['git', 'log', '--pretty=format:%H;%an;%ar;%s'], universal_newlines=True
)

# Przetwarzanie logów
data = [line.split(";") for line in log.split("\n")]

# Zapisz do CSV
with open("commit_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Hash", "Author", "Date", "Message"])
    writer.writerows(data)

print("Raport zapisany w commit_report.csv")
