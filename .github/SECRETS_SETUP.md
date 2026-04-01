# GitHub Secrets 설정 가이드

이 저장소에서 매일 이메일을 보낼 수 있도록 GitHub Secrets 를 설정하세요.

## 설정 방법

1. GitHub 저장소로 이동: https://github.com/CFOLD/statistics-questions
2. `Settings` → `Secrets and variables` → `Actions`
3. `New repository secret` 을 클릭하여 아래 secret 들을 추가

## 필요한 Secrets

| Secret 이름 | 설명 | 예시 |
|-------------|------|------|
| `SMTP_HOST` | SMTP 서버 주소 | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP 포트 | `587` |
| `SMTP_USERNAME` | SMTP 사용자 (보내는 이메일) | `your-email@gmail.com` |
| `SMTP_PASSWORD` | SMTP 비밀번호 (Gmail 은 앱 비밀번호) | `xxxx xxxx xxxx xxxx` |
| `EMAIL_RECIPIENTS` | 받는사람 이메일 (콤마 구분) | `you@example.com, friend@example.com` |

## Gmail 사용 방법

1. Google 계정 → [앱 비밀번호 생성](https://myaccount.google.com/apppasswords)
2. 앱 이름: `Statistics Email` 입력
3. 생성된 16 자리 비밀번호를 `SMTP_PASSWORD` 로 설정

```
예시: abcd efgh ijkl mnop
```

## 수동 테스트

설정 후 Actions 탭에서:

1. `Daily Statistics Question Email` 워크플로우 선택
2. `Run workflow` 클릭
3. 수동으로 이메일 발송 테스트

## 스케줄

- 매일 UTC 00:00 (한국시간 오전 9 시) 에 자동 발송
- `workflow_dispatch` 이벤트로 수동 실행 가능
