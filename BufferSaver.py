import time
from datetime import datetime, timedelta
import os
import json

# 本来はモデル
def model_function(value):
    return value * 2

# バッファファイルを初期化（新しい日付での利用時）
def initialize_buffer():
    with open(BUFFER_FILE, 'w') as f:
        json.dump([], f)  # 空リストで初期化

# バッファファイル名
BUFFER_FILE = 'buffer.json'

def update_buffer():
    # 初期値
    input_value = 1
    current_date = datetime.now().date()  # 今日の日付

    # 初回起動時にファイルを初期化
    if not os.path.exists(BUFFER_FILE):
        initialize_buffer()

    while True:
        # 現在の日付を取得
        new_date = datetime.now().date()

        # 日付が変わった場合はバッファファイルをリセット
        if new_date != current_date:
            current_date = new_date
            initialize_buffer()

        # 新しいデータの生成
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M')
        prediction = model_function(input_value)
        new_data = {"timestamp": timestamp, "prediction": prediction}

        # バッファファイルにデータを追記
        with open(BUFFER_FILE, 'r') as f:
            data = json.load(f)

        data.append(new_data)

        with open(BUFFER_FILE, 'w') as f:
            json.dump(data, f, indent=4)

        # 次の処理まで1分待機
        time.sleep(60)


if __name__ == '__main__':
    update_buffer()
