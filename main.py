수입 오픈아이
os 가져오기
supabase에서 create_클라이언트 가져오기, 클라이언트
dotenv에서 load_dotenv 가져오기
플라스크 가져오기 플라스크, 요청, jsonify

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
오픈아이.api_key = os.getenv("OPENAI")_API_KEY")

# 수파베이스 연결
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
첨두: 클라이언트 = create_c라이언트(SUPABASE_URL, SUPABASE_KEY)

앱 = 플라스크(__name__)

# AI 기억 불러오기
def get_memory(user_id):
 응답 = supabase.table ("ai_memory").("*", eq("user_id", user_id".order ("timestamp", desc=True).limit(10).execute()를 선택합니다
 응답으로 [msg["message"]를 반환합니다.data]

# AI 기억 저장하기
def save_memory(user_id, 메시지):
 supabase.table ("ai_memory").({"user_id"를 삽입합니다: user_id, "message": 메시지, "timestamp": "now ()"}).execute()

@app.route("/채팅, 메서드=["POST"])
기본 채팅 ():
 데이터 = request.get_json ()
 user_id = data.get ("user_id")
 사용자_message = data.get ("message")

 past_memories = get_memory(user_id)
 메모리_context = "\n". join(과거_memories)

 응답 = openai.채팅 완료.생성(
 model="gpt-4",
 메시지 =[
 {"role": "system", "content": "당신은 기억을 유지하는 AI입니다."},
 {"역할": "사용자", "콘텐츠": memory_context},
 {"역할": "사용자", "콘텐츠": 사용자_message}
 ]
 )
    
 ai_response = 응답 ["choices"][0]["message"]["콘텐츠"]
 저장_메모리(user_id, user_message)
 저장_메모리(user_id, ai_response)

 jsonify ({ "response"를 반환합니다: ai_response})

__name__ == "__main__"인 경우:
 app.run(호스트="0.0.0.0", 포트=5000)
