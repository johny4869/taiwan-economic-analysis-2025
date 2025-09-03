import json

def generate_html_report(data):
    """
    接收一個包含分析數據的字典，並生成一份HTML報告檔案。

    Args:
        data (dict): 包含報告所需數據的字典。
    """

    # 步驟 1: 將圖表數據轉換為JavaScript可讀的格式
    # 在真實專案中，這些數據將來自您的Pandas DataFrame
    history_labels_js = json.dumps(data['history_chart']['labels'])
    history_values_js = json.dumps(data['history_chart']['values'])

    # 步驟 2: 定義HTML模板
    # 我們使用f-string來插入Python變數。{}中的變數會被替換。
    # 三個引號 """...""" 允許我們建立一個跨越多行的字串。
    html_template = f"""
<!DOCTYPE html>
<html lang="zh-Hant" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['report_title']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Noto Sans TC', sans-serif;
            background-color: #F8F9FA;
        }}
        .chart-container {{
            position: relative;
            width: 100%;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            height: 450px;
        }}
        .gradient-text {{
            background: linear-gradient(90deg, #7A5195, #EF5675, #FF764A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
    </style>
</head>
<body class="text-gray-800">

    <header class="bg-white/90 backdrop-blur-lg sticky top-0 z-50 shadow-md">
        <nav class="container mx-auto px-6 py-3">
            <h1 class="text-xl font-bold text-[#003F5C]">{data['header_title']}</h1>
        </nav>
    </header>

    <main class="container mx-auto px-6 py-10">

        <section id="hero" class="text-center py-20">
            <h2 class="text-sm font-bold uppercase tracking-widest text-[#7A5195] mb-4">{data['hero']['subtitle']}</h2>
            <p class="text-8xl font-bold gradient-text tracking-tighter">{data['hero']['main_metric']}%</p>
            <p class="mt-4 text-2xl font-semibold text-[#003F5C]">{data['hero']['status']}</p>
            <p class="mt-6 max-w-3xl mx-auto text-gray-600 text-lg">
                {data['hero']['description']}
            </p>
        </section>

        <section id="history" class="py-20">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-bold text-[#003F5C]">歷史的軌跡：一場估值的雲霄飛車</h2>
                <p class="text-lg text-gray-600 max-w-3xl mx-auto">將當前指標置於歷史長河中，我們發現自2020年後，市場估值似乎進入了一個前所未見的「新常態」。</p>
            </div>
            <div class="bg-white p-8 rounded-2xl shadow-lg">
                <div class="chart-container">
                    <canvas id="historyChart"></canvas>
                </div>
            </div>
        </section>

    </main>
    
    <script>
        document.addEventListener('DOMContentLoaded', function () {{
            const historyData = {{
                labels: {history_labels_js},
                datasets: [{{
                    label: '台灣巴菲特指標 (%)',
                    data: {history_values_js},
                    borderColor: '#EF5675',
                    backgroundColor: 'rgba(239, 86, 117, 0.1)',
                    fill: true,
                    tension: 0.1,
                }}]
            }};

            const historyConfig = {{
                type: 'line',
                data: historyData,
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                }}
            }};

            const historyCtx = document.getElementById('historyChart').getContext('2d');
            new Chart(historyCtx, historyConfig);
        }});
    </script>

</body>
</html>
    """

    # 步驟 3: 將生成的HTML內容寫入一個檔案
    try:
        with open("report.html", "w", encoding="utf-8") as f:
            f.write(html_template)
        print("報告 'report.html' 已成功生成！")
    except Exception as e:
        print(f"生成報告時發生錯誤: {e}")

# --- 主執行區 ---
if __name__ == "__main__":
    # 這是一個模擬數據，它將模擬您在21天計畫中分析得出的結果
    analysis_results = {
        "report_title": "動態生成-台股估值儀表板",
        "header_title": "Python 動態報告",
        "hero": {
            "subtitle": "2025年中期評估：台灣巴菲特指標",
            "main_metric": 281.2,  # 這是從Python計算來的小數
            "status": "達到歷史新高，處於「嚴重高估」區間",
            "description": "這是一份由Python腳本根據最新分析結果動態生成的報告。單一指標發出了強烈的警示信號，但這並非故事的全貌。"
        },
        "history_chart": {
            "labels": ['2000 (網路泡沫)', '2009 (金融海嘯)', '2021 (後疫情)', '2025 (當前)'],
            "values": [210, 95, 265, 281.2] # 最後一個值也是動態的
        }
    }

    # 呼叫主函式，傳入您的分析結果
    generate_html_report(analysis_results)
