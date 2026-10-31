import os
import requests

def send_telegram_message(message: str) -> bool:
    """텔레그램 봇을 통해 지정된 채팅방으로 메시지를 전송합니다."""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        print("[Telegram] 경고: TELEGRAM_BOT_TOKEN 또는 TELEGRAM_CHAT_ID 환경 변수가 설정되지 않았습니다.")
        return False
        
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            print("[Telegram] 메시지 전송 성공!")
            return True
        else:
            print(f"[Telegram] 전송 실패 (상태코드: {response.status_code}): {response.text}")
            return False
    except Exception as e:
        print(f"[Telegram] 예외 발생: {e}")
        return False
