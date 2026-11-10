"""
LogForge Engine - Pure Python Data Analysis Pipeline
Demonstrating Core Python Concepts: Mutability, Shared References, and Precision.
"""

from decimal import Decimal


def parse_log_line(line: str) -> dict:
    # 1. 利用字符串 replace 和 split 处理文本[span_17](start_span)[span_17](end_span)
    clean_line = line.strip().replace("[INFO]", "").replace("[ERROR]", "")
    parts = clean_line.split(",")

    # 2. 避免浮点数误差，使用 Decimal 解析金额[span_18](start_span)[span_18](end_span)
    user_id, ip, status_code, amount_str = (
        parts[0],
        parts[1],
        int(parts[2]),
        parts[3],
    )
    amount = Decimal(amount_str)

    return {
        "user_id": user_id,
        "ip": ip,
        "status": status_code,
        "amount": amount,
    }


def process_dataset(raw_data: list) -> dict:
    # 3. 数据防护：切断共享引用 (Shared Reference)，避免修改原列表[span_19](start_span)[span_19](end_span)
    working_data = raw_data.copy()

    # 4. 元组：定义不可变的合法状态码白名单[span_20](start_span)[span_20](end_span)
    VALID_STATUSES = (200, 201)

    # 5. 字典：聚合统计数据[span_21](start_span)[span_21](end_span)
    stats = {"total_revenue": Decimal("0.00"), "user_count": 0, "ip_list": []}

    for record in working_data:
        if record["status"] in VALID_STATUSES:
            stats["total_revenue"] += record["amount"]
            stats["ip_list"].append(record["ip"])

    stats["user_count"] = len(stats["ip_list"])
    return stats


# 测试运行
if __name__ == "__main__":
    sample_logs = [
        "USER01,192.168.1.1,200,10.50",
        "USER02,192.168.1.2,500,0.00",
        "USER03,192.168.1.3,200,20.25",
    ]

    parsed_records = [parse_log_line(line) for line in sample_logs]
    result = process_dataset(parsed_records)

    print(f"总收入(精准计算): ${result['total_revenue']}")
