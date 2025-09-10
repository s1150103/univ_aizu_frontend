import json

data = {
    "date": "2021-01-19",
    "location": "会津若松市内研究室制御盤",
    "data_lists": []
}

# 3つのデバイス（左側、中央、右側ランプ）のデータを生成
for device_index in range(3):
    device_data = []
    
    for minute in range(1440):  # 24時間 * 60分 = 1440分
        hour = minute // 60
        minute_in_hour = minute % 60
        
        # 各デバイスごとにパターンを設定
        if device_index == 0:  # 左側ランプ - 1時間単位で赤、それ以外は緑
            color = 2 if hour % 2 == 0 else 1
        elif device_index == 1:  # 中央ランプ - 全部赤
            color = 2
        else:  # 右側ランプ - 2時間ごとに赤、それ以外は緑
            color = 2 if hour % 4 < 2 else 1
        
        time_str = f"{hour:02d}:{minute_in_hour:02d}:00"
        
        device_data.append({
            "color": color,
            "timestamp": minute,
            "hour": hour,
            "minute": minute_in_hour,
            "time": time_str
        })
    
    data["data_lists"].append(device_data)

# JSONファイルに書き込み
with open("data_2021-01-19.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("完全な1440個のデータポイントを持つJSONファイルを作成しました")
print(f"ファイルサイズ: {len(json.dumps(data))} 文字")