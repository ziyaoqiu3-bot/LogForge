"""
LogForge - Pure Python Log Parsing and Financial Reporting Tool
"""
from decimal import Decimal

def process_logs(log_filename, report_filename, error_log_filename):
    category_totals = {}
    user_transactions = {}
    total_records = 0
    valid_records = 0

    with open(log_filename, 'r', encoding='utf-8') as f_in, \
         open(error_log_filename, 'w', encoding='utf-8') as f_err:

        for line_idx, line in enumerate(f_in, start=1):
            total_records += 1
            line = line.strip()

            if not line:
                continue

            parts = line.split(',')

            if len(parts) != 5:
                print(f"[WARN] Line {line_idx} data format anomaly: {line}", file=f_err)
                continue

            timestamp, user_id, action, amount_str, status = parts

            if status != 'SUCCESS':
                print(f"[INFO] Line {line_idx} transaction unsuccessful (Status: {status}), skipped", file=f_err)
                continue

            amount = Decimal(amount_str)
            valid_records += 1

            category_totals[action] = category_totals.get(action, Decimal('0')) + amount

            if user_id not in user_transactions:
                user_transactions[user_id] = []
            user_transactions[user_id].append((timestamp, action, amount))

    with open(report_filename, 'w', encoding='utf-8') as f_out:
        f_out.write("=========================================\n")
        f_out.write(" LogForge Financial Summary Report \n")
        f_out.write("=========================================\n\n")

        f_out.write("1. Transaction Totals by Category:\n")
        f_out.write("%-15s %15s\n" % ("TX Type", "Total Amount"))
        f_out.write("-" * 32 + "\n")

        for action, total in category_totals.items():
            f_out.write("%-15s %15.2f\n" % (action, total))

        f_out.write("\n2. User Transaction Details Summary:\n")
        for user_id, records in user_transactions.items():
            user_type = "VIP User" if len(records) >= 2 else "Regular User"
            f_out.write(f"User: {user_id} [{user_type}]\n")

            for timestamp, act, amt in records:
                date_part = timestamp[:10]
                f_out.write(" - [%s] %-10s %8.2f\n" % (date_part, act, amt))

        f_out.write("\n" + "=" * 41 + "\n")
        f_out.write("Total Records Read: %d, Valid Settlements: %d\n" % (total_records, valid_records))

if __name__ == '__main__':
    process_logs('raw_logs.txt', 'output_report.txt', 'error_logs.txt')
    print("Analysis completed! Output files generated: output_report.txt and error_logs.txt")
