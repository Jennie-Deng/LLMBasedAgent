import csv
from datetime import datetime
import os

# 定义CSV文件路径
csv_file = '/Volumes/Jennie/Agent/FinAgents/FinAi/data/comment.csv'

# 定义列名
fieldnames = ['user_id', 'username', 'comment_date', 'comment_text']

# 提交评论
def submit_comment(user_id, username, comment_text):
    comment_date = datetime.now().strftime('%Y-%m-%d')
    comment = {'user_id': user_id, 'username': username, 'comment_date': comment_date, 'comment_text': comment_text}

    # 检查文件是否存在，若不存在则写入列名
    file_exists = os.path.isfile(csv_file)

    # 写入CSV文件
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # 仅在文件不存在时写入列名
        writer.writerow(comment)

# 读取所有评论
def get_comments():
    comments = []
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                comments.append(row)
    except FileNotFoundError:
        pass
    return comments

# 示例使用
submit_comment('001', 'Alice', 'This stock is performing well!')
submit_comment('002', 'Bob', 'I think this stock is overvalued.')

comments = get_comments()
comments
