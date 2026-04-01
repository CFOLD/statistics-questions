<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
    .header { background: #4A90A4; color: white; padding: 20px; border-radius: 8px 8px 0 0; }
    .content { background: #f9f9f9; padding: 20px; border: 1px solid #ddd; border-top: none; }
    .question { background: white; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #4A90A4; }
    .explanation { background: #f0f8ff; padding: 15px; margin: 10px 0; border-radius: 5px; }
    .footer { text-align: center; padding: 20px; color: #666; font-size: 0.9em; }
    h1 { margin: 0; font-size: 1.5em; }
    h2 { color: #4A90A4; font-size: 1.2em; }
    .math { font-family: 'Courier New', monospace; background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }
  </style>
</head>
<body>
  <div class="header">
    <h1>📊 통계분석 일일 문제</h1>
    <p>${{ formatdate('yyyy-MM-dd', github.event.schedule) }}</p>
  </div>

  <div class="content">
    <h2>오늘의 문제</h2>
    <p>매일 한 개의 통계분석 문제를 보내드립니다. 개념 이해와 계산 능력을 함께 기를 수 있도록 준비되었습니다.</p>

    <div class="question">
      <strong>문제:</strong><br>
      [여기에 문제가 표시됩니다]
    </div>

    <div class="explanation">
      <strong>📝 해설:</strong><br>
      [여기에 해설이 표시됩니다]
    </div>
  </div>

  <div class="footer">
    <p>더 많은 문제는 <a href="https://github.com/CFOLD/statistics-questions">statistics-questions 저장소</a>에서 확인하세요.</p>
  </div>
</body>
</html>
