# -*- coding: utf-8 -*-
"""발표 장표 + 대본 결합 PDF 생성기"""
import pymupdf

SRC = '/root/.claude/uploads/b0f96146-8493-513b-a8a8-3280388d5ba4/75765f77-26_________________________.pdf'
OUT = '/home/user/3svs-website/docs/심의위원회_발표자료_대본합본.pdf'
REG = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
BLD = '/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf'

YELLOW = (0.98, 0.78, 0.09)
BLACK  = (0.09, 0.09, 0.09)
GRAY   = (0.45, 0.45, 0.45)
LINE   = (0.85, 0.85, 0.85)
CREAM  = (1.0, 0.97, 0.87)

# (슬라이드번호, 시간, 구간명, 대본, 팁)
SCRIPT = [
(1, "0:00 – 0:20", "오프닝 — 한 문장 정의",
 "안녕하십니까. 주식회사 쓰리스트라이프 대표이사 배종원입니다.\n"
 "저희를 한 문장으로 소개드리면 **“AI 기술로 성과를 만드는 글로벌 비즈니스 플랫폼 기업”**입니다. "
 "행사를 대행하는 회사가 아니라, **자체 개발한 AI 플랫폼을 글로벌 현장에서 직접 검증하는 기술기업**입니다.",
 "천천히, 또박또박. 이 한 문장이 오늘 발표 전체의 프레임입니다."),

(2, "0:20 – 0:25", "목차 — 넘기며 한 문장",
 "오늘은 회사 개요와 사업모델, 그리고 대출금 사용 계획까지 **5분 안에 실적과 숫자로** 말씀드리겠습니다.",
 "멈추지 말고 바로 다음 장으로 넘깁니다."),

(3, "0:25 – 0:55", "회사 개요 — 1년 만의 트랙레코드",
 "저희는 **2025년 4월 설립, 임직원 7명**의 기업입니다.\n"
 "설립 1년 남짓한 기간에 **퀄컴 QAIPI APAC 데모데이를 APAC 10개국** 대상으로 운영했고, "
 "올해 1월 **CES 공식 K-엔터테크 포럼**, 6월 **서울대 반도체 연합행사와 연세대 x 넷플릭스 세션**, "
 "7월에는 **KAIT SW 중소기업 해외진출 프로그램**에 착수했습니다.\n"
 "매출은 설립 첫해 9개월 만에 **2억 1,300만원**, 올해는 7월 기준 이미 **1억 8,300만원**입니다.",
 "연혁 표를 손으로 짚으며 “1년”과 “기관 이름”을 강조하세요."),

(4, "0:55 – 1:20", "경영진 — 현장에서 증명한 팀",
 "이것이 가능했던 이유는 팀입니다.\n"
 "저는 현대자동차그룹과 Plug and Play를 거쳐 **글로벌 프로그램 100건 이상**을 운영했고, "
 "배승훈 이사는 동남아 특화 역량으로 포럼·컨퍼런스 100건 이상, 권오욱 이사는 **EXIT 2회 경험**을 보유하고 있습니다.\n"
 "**평균 경력 12년, 기획부터 운영까지 외주 없이 직접 실행하는 조직**입니다.",
 "“외주 없이 직접”에 힘을 주면 뒤의 기술 선순환 논리가 자연스럽게 이어집니다."),

(5, "1:20 – 2:05", "사업 구조 — 기술 선순환",
 "저희 사업은 **자체 개발 AI 플랫폼을 코어로 세 축**이 맞물려 돌아갑니다. "
 "**AI SaaS 플랫폼 개발·운영**, 월마트·샘스클럽·태국 Konvy·필리핀 SM 그룹 채널과 브랜드를 잇는 "
 "**글로벌 리테일 소싱**, 진단부터 현지 IR까지 이어지는 **창업기업 글로벌 진출 지원**입니다.\n"
 "여기서 저희만의 구조를 강조드리고 싶습니다. **서비스를 직접 개발해 저희가 수주한 프로그램에 실전 투입하고, "
 "실증 데이터를 쌓아 고도화한 뒤, 외부에 SaaS로 판매**합니다.\n"
 "즉 **행사는 비용이 아니라 저희 기술이 검증되는 테스트베드이자 레퍼런스**입니다. "
 "경쟁사가 인력을 투입할 때, 저희는 데이터를 쌓습니다.",
 "하단 선순환 화살표를 왼쪽에서 오른쪽으로 짚으며 말하면 설득력이 올라갑니다."),

(6, "2:05 – 3:00", "자체 AI 서비스 4종 — 핵심 슬라이드",
 "현재 자체 개발·운영 중인 서비스는 네 가지입니다.\n"
 "**대화 AI**는 비즈니스 미팅 특화 양방향 동시통역 SaaS로, 실시간 통역부터 대화록·요약 리포트 자동 생성까지 지원하며 "
 "**사용처를 이미 확보**했습니다. **TRIBO**는 동남아 인플루언서를 AI로 매칭·관리하는 K-코스메틱 커머스 플랫폼으로 "
 "**현재 운영 중**입니다. **PITCHKO**는 미국 진출 기업과 현지 수행사를 연결하는 매치메이킹 플랫폼, "
 "네 번째는 **소규모 기업 특화 AI 연동형 ERP**로 두 서비스는 테스트베드를 진행 중입니다.\n"
 "성과는 숫자로 말씀드리겠습니다. AI 매칭으로 성사시킨 **비즈니스 미팅 87건**, 매칭 미팅 **노쇼율 0%**, "
 "**해외 연사·기관 직접 네트워크 100곳 이상**입니다. "
 "수익은 **B2G·B2B 프로그램 수주와 SaaS 구독의 이중 구조**로 설계했습니다.",
 "가장 중요한 장표. 87건 / 0% / 100+ 세 숫자는 반드시 또렷하게."),

(7, "3:00 – 3:20", "SWOT — 강점과 약점 대응",
 "강점은 **AI 서비스 4종의 개발·운영 역량, 퀄컴·CES 등 글로벌 실적, 100곳 이상의 해외 네트워크, "
 "그리고 7인 정예 조직의 민첩성**입니다.\n"
 "짧은 업력과 지재권 미확보라는 약점은 인정합니다. 다만 **이번 재원으로 개발과 지재권 출원을 함께 진행**해 보완하겠습니다.",
 "약점을 먼저 인정하고 곧바로 대응책을 붙이면 심의위원의 질문을 미리 막을 수 있습니다."),

(8, "3:20 – 3:40", "STP — 시장 포지셔닝",
 "포지셔닝은 분명합니다. 저희는 **인력 동원형 대행사와 가격으로 경쟁하지 않습니다.**\n"
 "**AI·테크 산업 중심의 B2G·B2B 시장을 선점**하고, **데이터와 기술로 성과를 보증하는 파트너**로 시장을 다시 정의합니다.",
 "“경쟁하지 않습니다”에서 한 박자 쉬고 다음 문장으로."),

(9, "3:40 – 3:50", "4P — 빠르게 넘기기",
 "자체 플랫폼으로 원가를 낮춰 **예산 대부분을 실질 프로그램에 투입**하는 것이 저희 가격 경쟁력이고, "
 "**공공 조달과 글로벌 파트너 직접 채널**이 판로입니다.",
 "시간이 부족하면 이 장은 한 문장으로 줄이고 넘어가세요."),

(10, "3:50 – 4:00", "성과 측정 — 데이터 자산화",
 "모든 프로그램은 **KPI를 사전 정의하고 ORBIT 5단계로 운영**하며, "
 "**운영 데이터가 저희 AI 플랫폼에 축적되어 다음 서비스의 학습 데이터**가 됩니다.",
 "여기서 다시 “선순환” 키워드를 한 번 더 심어줍니다."),

(11, "4:00 – 4:15", "고용창출 — 첫 채용이 AI 개발자",
 "고용은 현재 7명에서 **3년 내 15명, 신규 8명을 채용**하고 이 중 **5명이 기술 직군**입니다.\n"
 "특히 **이번 대출 재원으로 확보하는 첫 채용이 AI 서비스 개발 인력 2명**입니다. "
 "기술기업으로의 인력 구조 전환을 실행하겠습니다.",
 "“첫 채용이 개발자”는 자금 용도의 진정성을 보여주는 문장입니다."),

(12, "4:15 – 4:35", "대출금 사용 및 상환 계획",
 "신청 금액은 **1억원이며, 70%인 7천만원이 기술에 직접 투입**됩니다. "
 "**AI 플랫폼 고도화 개발비 4천만원, AI 개발 인력 인건비 3천만원**, "
 "그리고 글로벌 판로·마케팅비 1,500만원, 임차료·운영비 1,000만원, 예비비로 구성됩니다.\n"
 "상환은 **3년 거치 후 3년 분할, 총 6년 구조**로 2029년부터 월 약 299만원을 균등 상환합니다.",
 "⚠ 자료 확인: 예비비가 50,000,000원으로 표기되어 합계 1억원과 맞지 않습니다 (500만원으로 수정 권장)."),

(13, "4:35 – 4:50", "매출·손익 — 상환 능력",
 "상환 재원은 **B2G·B2B 수주 매출과 SaaS 구독 매출**입니다.\n"
 "저희는 **설립 2년차에 전년 대비 3배 성장 궤도**에 있고, FY26 매출 **6억 5천만원, 당기순이익 4,400만원**을 전망합니다. "
 "하반기 **KAIT·상생포럼 등 확정된 파이프라인**을 이미 확보하고 있어 상환에 무리가 없습니다.",
 "그래프를 짚으며 “흑자”와 “확정 파이프라인” 두 단어를 반드시 발음하세요."),

(14, "4:50 – 5:00", "클로징 — 요청",
 "정리드리겠습니다. 저희는 **1년 만에 글로벌 실적을 만든 팀**이고, "
 "**AI 서비스 4종을 직접 개발해 현장에서 검증**하고 있으며, **이 자금의 대부분을 기술과 사람에 씁니다.**\n"
 "검증된 실행력에 기술을 더할 수 있도록 지원을 부탁드립니다. 감사합니다.",
 "마지막 문장은 고개를 들고 심의위원을 보며."),
]

QNA = [
("업력이 짧은데 지속 가능한가?",
 "설립 9개월 만에 2억 1,300만원, 올해 7월까지 1억 8,300만원을 이미 달성했습니다. 퀄컴·CES·KAIT 등 재수주와 공공 채널 기반 매출이며, 하반기 확정 파이프라인도 확보되어 있습니다."),
("AI 서비스라지만 결국 행사 대행 아닌가?",
 "대화 AI는 사용처 확보를 마쳤고 TRIBO는 운영 중입니다. 행사 매출과 별개로 SaaS 구독 매출이 FY27부터 발생하며, 행사는 그 서비스의 실증 데이터를 만드는 채널입니다."),
("7명으로 감당 가능한가?",
 "ORBIT 5단계 표준 방법론과 SOP 문서화로 운영을 표준화했고, AI 매칭 시스템이 진단·매칭·운영 전 과정에 적용되어 있습니다. 실제로 매칭 87건·노쇼율 0%를 7인 조직이 만들었습니다."),
("지재권이 없는데 기술 차별성은?",
 "상표·특허 출원을 추진 중이며 이번 대출 재원에 그 비용을 반영했습니다. 더 근본적인 진입장벽은 실전 운영에서만 쌓이는 매칭 데이터입니다."),
]

src = pymupdf.open(SRC)
doc = pymupdf.open()
freg = pymupdf.Font(fontfile=REG)
fbld = pymupdf.Font(fontfile=BLD)
W, H = 595, 842
M = 42

def spans(text):
    """**bold** 파싱 → [(문자열, bold)]"""
    out, bold = [], False
    for part in text.split('**'):
        if part:
            out.append((part, bold))
        bold = not bold
    return out

def draw_text(page, x, y, width, text, size=11, leading=17.5, color=BLACK):
    """볼드 혼합 자동 줄바꿈. 반환: 다음 y"""
    tw = pymupdf.TextWriter(page.rect)
    for para in text.split('\n'):
        cx = x
        for chunk, bold in spans(para):
            font = fbld if bold else freg
            token, buf = '', ''
            for ch in chunk:
                buf += ch
                if ch in ' ,.·의를을이가은는와과도로서만' or len(buf) > 0:
                    pass
            # 어절 단위 분해 (공백 유지)
            words, cur = [], ''
            for ch in chunk:
                cur += ch
                if ch == ' ':
                    words.append(cur); cur = ''
            if cur:
                words.append(cur)
            for w in words:
                wl = font.text_length(w, size)
                if cx + wl > x + width and cx > x:
                    y += leading; cx = x
                    if w.startswith(' '):
                        w = w.lstrip(' ')
                        wl = font.text_length(w, size)
                # 한 어절이 폭보다 길면 글자 단위로 쪼갬
                if wl > width:
                    for ch in w:
                        cl = font.text_length(ch, size)
                        if cx + cl > x + width:
                            y += leading; cx = x
                        tw.append((cx, y), ch, font=font, fontsize=size)
                        cx += cl
                else:
                    tw.append((cx, y), w, font=font, fontsize=size)
                    cx += wl
        y += leading
    tw.write_text(page, color=color)
    return y

def line(page, y, col=LINE, w=0.7):
    page.draw_line(pymupdf.Point(M, y), pymupdf.Point(W - M, y), color=col, width=w)

# ── 표지 ──────────────────────────────────────────────
cover = doc.new_page(width=W, height=H)
cover.draw_rect(pymupdf.Rect(0, 0, W, 190), color=None, fill=BLACK)
cover.draw_rect(pymupdf.Rect(0, 186, W, 194), color=None, fill=YELLOW)
tw = pymupdf.TextWriter(cover.rect)
tw.append((M, 92), "심의위원회 발표", font=fbld, fontsize=30)
tw.append((M, 132), "장표 + 대본 합본", font=freg, fontsize=20)
tw.write_text(cover, color=(1, 1, 1))
tw = pymupdf.TextWriter(cover.rect)
tw.append((M, 165), "주식회사 쓰리스트라이프  |  3Stripe Venture Studio", font=freg, fontsize=11)
tw.write_text(cover, color=YELLOW)

y = 250
y = draw_text(cover, M, y, W - 2 * M,
  "**발표 시간 5분 (낭독 약 1,730자 · 분당 340자 기준)**\n"
  "이 문서는 발표 장표 14장과 각 장의 낭독 대본을 한 페이지씩 짝지어 정리한 합본입니다. "
  "장표 아래 회색 박스가 실제로 말할 문장이고, 노란 박스는 전달 팁입니다.", size=11.5)

y += 14
cover.draw_rect(pymupdf.Rect(M, y, W - M, y + 108), color=None, fill=CREAM)
yy = draw_text(cover, M + 16, y + 26, W - 2 * M - 32,
  "**발표를 관통하는 3개의 축**\n"
  "①  대행사가 아닌 **자체 AI 플랫폼 기술기업**  —  대화 AI · TRIBO · PITCHKO · AI ERP\n"
  "②  개발 → 실전 투입 → 실증 데이터 → 고도화 → SaaS 판매의 **기술 선순환**\n"
  "③  **대출금의 70%가 기술 투자**, 첫 신규 채용이 AI 개발 인력", size=11)

y += 130
y = draw_text(cover, M, y, W - 2 * M,
  "**반드시 외울 숫자 6개**\n"
  "87건 (AI 매칭 미팅 성사)   ·   0% (노쇼율)   ·   100+ (해외 연사·기관 네트워크)\n"
  "213백만원 (`25년 첫해 9개월 매출)   ·   650백만원 (FY26 매출 목표)   ·   70% (대출금 중 기술 투자 비중)", size=11)

y += 10
y = draw_text(cover, M, y, W - 2 * M,
  "**반복할 한 문장**\n“행사는 우리 기술이 증명되는 현장이고, 그 코어는 자체 개발 AI 플랫폼입니다.”", size=11)

y += 26
y = draw_text(cover, M, y, W - 2 * M, "**타임라인**", size=11)
y += 4
line(cover, y)
y += 17
for pno, time, title, _b, _t in SCRIPT:
    tw = pymupdf.TextWriter(cover.rect)
    tw.append((M, y), time, font=freg, fontsize=9.5)
    tw.append((M + 92, y), f"p.{pno}", font=freg, fontsize=9.5)
    tw.write_text(cover, color=GRAY)
    tw = pymupdf.TextWriter(cover.rect)
    tw.append((M + 130, y), title, font=fbld if pno in (5, 6, 12) else freg, fontsize=9.5)
    tw.write_text(cover, color=BLACK)
    y += 15.5
line(cover, y - 8)

# ── 장표 + 대본 ────────────────────────────────────────
for idx, (pno, time, title, body, tip) in enumerate(SCRIPT, start=1):
    page = doc.new_page(width=W, height=H)
    # 헤더
    tw = pymupdf.TextWriter(page.rect)
    tw.append((M, 44), f"슬라이드 {pno}", font=fbld, fontsize=10)
    tw.write_text(page, color=GRAY)
    tw = pymupdf.TextWriter(page.rect)
    label = f"{idx} / {len(SCRIPT)}"
    tw.append((W - M - freg.text_length(label, 10), 44), label, font=freg, fontsize=10)
    tw.write_text(page, color=GRAY)
    line(page, 52)

    # 장표 (원본 벡터 그대로 삽입)
    sw, sh = src[pno - 1].rect.width, src[pno - 1].rect.height
    iw = W - 2 * M
    ih = iw * sh / sw
    rect = pymupdf.Rect(M, 68, M + iw, 68 + ih)
    page.show_pdf_page(rect, src, pno - 1)
    page.draw_rect(rect, color=LINE, width=0.8)

    y = rect.y1 + 34
    # 시간 배지 + 구간명
    bw = freg.text_length(time, 10) + 20
    page.draw_rect(pymupdf.Rect(M, y - 13, M + bw, y + 5), color=None, fill=BLACK)
    tw = pymupdf.TextWriter(page.rect)
    tw.append((M + 10, y), time, font=fbld, fontsize=10)
    tw.write_text(page, color=YELLOW)
    tw = pymupdf.TextWriter(page.rect)
    tw.append((M + bw + 12, y), title, font=fbld, fontsize=13)
    tw.write_text(page, color=BLACK)

    y += 26
    # 대본 박스
    est = 0
    for para in body.split('\n'):
        est += max(1, int(freg.text_length(para.replace('**', ''), 12) / (iw - 32)) + 1)
    box_h = est * 19 + 30
    page.draw_rect(pymupdf.Rect(M, y, W - M, y + box_h), color=None, fill=(0.97, 0.97, 0.97))
    page.draw_rect(pymupdf.Rect(M, y, M + 4, y + box_h), color=None, fill=YELLOW)
    ny = draw_text(page, M + 20, y + 24, iw - 36, body, size=12, leading=19)
    y = max(ny, y + box_h) + 20

    # 팁 박스
    if tip:
        tw = pymupdf.TextWriter(page.rect)
        tw.append((M, y), "TIP", font=fbld, fontsize=9.5)
        tw.write_text(page, color=(0.75, 0.55, 0.0))
        draw_text(page, M + 30, y, iw - 30, tip, size=10, leading=15, color=GRAY)

    # 메모 영역
    my = max(y + 30, H - 250)
    tw = pymupdf.TextWriter(page.rect)
    tw.append((M, my), "메모", font=fbld, fontsize=9)
    tw.write_text(page, color=(0.72, 0.72, 0.72))
    for k in range(6):
        line(page, my + 22 + k * 26, col=(0.93, 0.93, 0.93), w=0.5)

    # 푸터
    line(page, H - 46, col=(0.92, 0.92, 0.92))
    tw = pymupdf.TextWriter(page.rect)
    tw.append((M, H - 30), "㈜쓰리스트라이프  |  심의위원회 5분 발표 대본", font=freg, fontsize=8.5)
    tw.write_text(page, color=GRAY)

# ── 예상 질의 대응 ─────────────────────────────────────
qp = doc.new_page(width=W, height=H)
qp.draw_rect(pymupdf.Rect(0, 0, W, 6), color=None, fill=YELLOW)
tw = pymupdf.TextWriter(qp.rect)
tw.append((M, 76), "예상 질의 대응", font=fbld, fontsize=22)
tw.write_text(qp, color=BLACK)
tw = pymupdf.TextWriter(qp.rect)
tw.append((M, 98), "각 답변 20초 이내 · 숫자로 시작해서 숫자로 끝내기", font=freg, fontsize=10.5)
tw.write_text(qp, color=GRAY)
line(qp, 116)

y = 152
for q, a in QNA:
    tw = pymupdf.TextWriter(qp.rect)
    tw.append((M, y), "Q", font=fbld, fontsize=13)
    tw.write_text(qp, color=YELLOW)
    y = draw_text(qp, M + 22, y, W - 2 * M - 22, "**" + q + "**", size=12.5, leading=19)
    y += 6
    y = draw_text(qp, M + 22, y, W - 2 * M - 40, a, size=11, leading=17.5, color=(0.25, 0.25, 0.25))
    y += 26

y += 4
qp.draw_rect(pymupdf.Rect(M, y, W - M, y + 74), color=None, fill=CREAM)
draw_text(qp, M + 16, y + 24, W - 2 * M - 32,
  "**발표 전 최종 체크**\n"
  "□ 리허설 2회 (스톱워치 5분)      □ 숫자 6개 암기      □ 자료 p.12 예비비 금액 수정 확인", size=11)

doc.save(OUT, garbage=4, deflate=True)
print('saved:', OUT, doc.page_count, 'pages')

# ── 동일 원고로 마크다운 재생성 (PDF와 내용 일치 보장) ──
MD = '/home/user/3svs-website/docs/심의위원회_5분_발표_스크립트.md'
lines = []
lines.append('# 심의위원회 5분 발표 스크립트')
lines.append('**㈜쓰리스트라이프 (3Stripe Venture Studio) | 발표시간 5분 · 낭독 약 1,730자**')
lines.append('')
lines.append('> 장표와 대본을 한 페이지씩 짝지은 PDF 합본: [`심의위원회_발표자료_대본합본.pdf`](./심의위원회_발표자료_대본합본.pdf)')
lines.append('')
lines.append('> 강조 축: ① 대행사가 아닌 **자체 AI 플랫폼 기술기업** ② 개발 → 실전 투입 → 실증 데이터 → 고도화 → **SaaS 판매의 기술 선순환** ③ 대출금의 **70%가 기술 투자**')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## ⏱ 타임라인')
lines.append('')
lines.append('| 시간 | 슬라이드 | 구간 |')
lines.append('|---|---|---|')
for pno, time, title, _b, _t in SCRIPT:
    lines.append(f'| {time} | p.{pno} | {title} |')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 🎤 대본')
for pno, time, title, body, tip in SCRIPT:
    lines.append('')
    lines.append(f'### [{time}] 슬라이드 {pno} — {title}')
    lines.append('')
    for para in body.split(chr(10)):
        lines.append(para)
        lines.append('')
    if tip:
        lines.append(f'> **TIP** {tip}')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 📌 발표 전 체크 포인트')
lines.append('')
lines.append('- **암기할 숫자 6개**: 87건(AI 매칭 미팅 성사) / 0%(노쇼율) / 100+(해외 네트워크) / 213백만원(`25년 매출) / 650백만원(FY26 목표) / 70%(기술 투자 비중)')
lines.append('- **반복할 한 문장**: "행사는 우리 기술이 증명되는 현장이고, 그 코어는 자체 개발 AI 플랫폼입니다."')
lines.append('- **속도**: 낭독 약 1,730자, 분당 340자 기준 5분. 초과되면 슬라이드 9·10을 각 한 문장으로 축약.')
lines.append('- ⚠️ **자료 확인 필요**: p.12 대출금 사용 내역의 예비비가 `50,000,000`으로 표기되어 합계 1억원과 맞지 않습니다(40+30+15+10 = 9,500만원 → 예비비 500만원). 발표 전 수정 권장. 대본에서는 금액을 특정하지 않고 "예비비"로만 언급했습니다.')
lines.append('')
lines.append('## 💬 예상 질의 대응 (각 20초)')
for q, a in QNA:
    lines.append('')
    lines.append(f'**Q. {q}**')
    lines.append('')
    lines.append('> ' + a)
lines.append('')
open(MD, 'w').write(chr(10).join(lines))
print('saved:', MD)
