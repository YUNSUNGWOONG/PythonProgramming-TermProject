from datetime import datetime

datetime_str = "2023-06-28 22:33:08"
formatted_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S").strftime("%Y년 %m월 %d일 %H시 %M분")

print(formatted_datetime)
