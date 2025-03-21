import csv

log_file = "logs/fuzz_data.csv"
cleaned_file = "logs/fuzz_data_cleaned.csv"

try:
    with open(log_file, "r", newline="", encoding="utf-8") as infile, open(cleaned_file, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if len(row) < 5:  # Skip malformed rows
                print(f"Skipping malformed row: {row}")
                continue

            timestamp, input_data, input_length, crashed, error_msg = row

            # Skip lines with the error message we want to remove
            if "log_fuzz_data() got multiple values for argument 'crashed'" in error_msg:
                print(f"Removing row due to error: {row}")
                continue

            # Fix 'None' input length issue
            if input_data == "None":
                input_length = "0"

            writer.writerow([timestamp, input_data, input_length, crashed, error_msg])

    print(f"✅ Cleaned log saved to: {cleaned_file}")

except Exception as e:
    print(f"❌ Error: {e}")
