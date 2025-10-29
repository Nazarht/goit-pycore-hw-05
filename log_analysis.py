import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    date, time, level, *text = line.split(" ")
    return {
        "timestamp": f"{date} {time}",
        "level": level.lower(),
        "message": " ".join(text).strip()
    }
    
def analyze_log(path: str) -> dict:
    with open(path, 'r') as file:
        for line in file.readlines():
            yield parse_log_line(line)
            
def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list[dict]) -> dict[str, int]:
    return Counter(log['level'] for log in logs)

def display_logs_by_level(logs: dict[str, int]):
    print(f"{'Logs Level':^12}|{'Count':^7}")
    print(f"{'-'*12}+{'-'*6}")
    for level, count in logs.items():
        print(f"{level:^12}|{count:^7}")
    
    print(f"{'-'*12}+{'-'*6}")

def main():
    _, path, *args = sys.argv
    logs: list[dict] = [log for log in analyze_log(path)]
    
    display_logs_by_level(count_logs_by_level(logs))
    
    if args:
        level = args[0]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"Logs with level {level.upper()}:")
        for log in filtered_logs:
            print(f"{log['timestamp']} - {log['message']}")

if __name__ == "__main__":
    main()