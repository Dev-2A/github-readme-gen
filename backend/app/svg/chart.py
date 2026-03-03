import math
from app.core.constants import THEME, LANGUAGE_COLORS, DEFAULT_COLOR


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
    )


def make_pie_chart(lang_ratio: dict[str, float], width: int = 340) -> str:
    """
    언어 비율 파이차트 + 범례 SVG 생성
    lang_ratio: {"Python": 45.0, "TypeScript": 30.0, ...}
    """
    if not lang_ratio:
        return _empty_chart("언어 데이터 없음", width)

    height = 200
    cx, cy, r = 100, 100, 75  # 파이 중심 및 반지름

    # 상위 6개만 사용, 나머지는 "Other"로 묶기
    items = list(lang_ratio.items())[:6]
    total = sum(v for _, v in items)
    remainder = max(0.0, 100.0 - total)
    if remainder > 0.5:
        items.append(("Other", round(remainder, 1)))

    # 파이 슬라이스 계산
    slices = []
    start_angle = -90.0  # 12시 방향 시작
    for lang, pct in items:
        sweep = pct / 100 * 360
        slices.append((lang, pct, start_angle, sweep))
        start_angle += sweep

    def polar(angle_deg: float, radius: float) -> tuple[float, float]:
        rad = math.radians(angle_deg)
        return cx + radius * math.cos(rad), cy + radius * math.sin(rad)

    def arc_path(start: float, sweep: float, radius: float) -> str:
        if sweep >= 359.99:
            # 원 전체
            x1, y1 = polar(start, radius)
            x2, y2 = polar(start + 180, radius)
            return (
                f"M {x1:.2f} {y1:.2f} "
                f"A {radius} {radius} 0 1 1 {x2:.2f} {y2:.2f} "
                f"A {radius} {radius} 0 1 1 {x1:.2f} {y1:.2f} Z"
            )
        end = start + sweep
        x1, y1 = polar(start, radius)
        x2, y2 = polar(end, radius)
        large = 1 if sweep > 180 else 0
        return (
            f"M {cx} {cy} "
            f"L {x1:.2f} {y1:.2f} "
            f"A {radius} {radius} 0 {large} 1 {x2:.2f} {y2:.2f} Z"
        )

    # SVG 조립
    legend_x = 210  # 범례 시작 X
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" role="img">',
        f'  <title>언어 사용 비율</title>',
        # 배경 카드
        f'  <rect width="{width}" height="{height}" rx="10" '
        f'fill="{THEME["card_bg"]}" stroke="{THEME["border"]}" stroke-width="1.5"/>',
        # 제목
        f'  <text x="18" y="24" font-family="Arial,sans-serif" font-size="12" '
        f'fill="{THEME["title"]}" font-weight="bold">🗂️ Languages</text>',
    ]

    # 파이 슬라이스
    for lang, pct, start, sweep in slices:
        color = LANGUAGE_COLORS.get(lang, DEFAULT_COLOR)
        path = arc_path(start, sweep, r)
        svg_parts.append(
            f'  <path d="{path}" fill="{color}" stroke="{THEME["card_bg"]}" stroke-width="1.5"/>'
        )

    # 도넛 구멍
    svg_parts.append(
        f'  <circle cx="{cx}" cy="{cy}" r="38" fill="{THEME["card_bg"]}"/>'
    )
    # 가운데 텍스트
    svg_parts.append(
        f'  <text x="{cx}" y="{cy - 5}" font-family="Arial,sans-serif" font-size="10" '
        f'fill="{THEME["subtext"]}" text-anchor="middle">Top</text>'
    )
    svg_parts.append(
        f'  <text x="{cx}" y="{cy + 10}" font-family="Arial,sans-serif" font-size="10" '
        f'fill="{THEME["subtext"]}" text-anchor="middle">Langs</text>'
    )

    # 범례
    for i, (lang, pct, _, _) in enumerate(slices):
        color = LANGUAGE_COLORS.get(lang, DEFAULT_COLOR)
        ly = 40 + i * 24
        label = _escape(lang)
        svg_parts += [
            f'  <rect x="{legend_x}" y="{ly - 9}" width="12" height="12" rx="3" fill="{color}"/>',
            f'  <text x="{legend_x + 17}" y="{ly}" font-family="Arial,sans-serif" '
            f'font-size="11" fill="{THEME["text"]}">{label}</text>',
            f'  <text x="{width - 14}" y="{ly}" font-family="Arial,sans-serif" '
            f'font-size="11" fill="{THEME["subtext"]}" text-anchor="end">{pct}%</text>',
        ]

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def make_bar_chart(lang_ratio: dict[str, float], width: int = 340) -> str:
    """
    언어 비율 가로 바 차트 SVG 생성 (파이차트 대안)
    """
    if not lang_ratio:
        return _empty_chart("언어 데이터 없음", width)

    items = list(lang_ratio.items())[:6]
    bar_width = width - 120   # 라벨 영역 제외
    row_h = 26
    height = 36 + len(items) * row_h

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" role="img">',
        f'  <title>언어 사용 비율 바 차트</title>',
        f'  <rect width="{width}" height="{height}" rx="10" '
        f'fill="{THEME["card_bg"]}" stroke="{THEME["border"]}" stroke-width="1.5"/>',
        f'  <text x="18" y="22" font-family="Arial,sans-serif" font-size="12" '
        f'fill="{THEME["title"]}" font-weight="bold">🗂️ Languages</text>',
    ]

    for i, (lang, pct) in enumerate(items):
        color = LANGUAGE_COLORS.get(lang, DEFAULT_COLOR)
        y = 32 + i * row_h
        filled = max(4, int(bar_width * pct / 100))
        label = _escape(lang)

        svg_parts += [
            # 언어명
            f'  <text x="14" y="{y + 13}" font-family="Arial,sans-serif" '
            f'font-size="11" fill="{THEME["text"]}">{label}</text>',
            # 바 배경
            f'  <rect x="100" y="{y + 2}" width="{bar_width}" height="14" '
            f'rx="7" fill="{THEME["accent_light"]}"/>',
            # 바 채움
            f'  <rect x="100" y="{y + 2}" width="{filled}" height="14" '
            f'rx="7" fill="{color}" opacity="0.85"/>',
            # 퍼센트
            f'  <text x="{width - 10}" y="{y + 13}" font-family="Arial,sans-serif" '
            f'font-size="10" fill="{THEME["subtext"]}" text-anchor="end">{pct}%</text>',
        ]

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def make_repo_card(
    name: str,
    description: str,
    stars: int,
    language: str,
    url: str,
    width: int = 340,
) -> str:
    """
    레포지토리 카드 SVG 생성
    """
    name = _escape(name)
    # 설명 길이 제한
    desc = _escape(description[:52] + "…" if len(description) > 52 else description)
    lang = _escape(language or "Unknown")
    lang_color = LANGUAGE_COLORS.get(language, DEFAULT_COLOR)
    height = 100

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" role="img">
  <title>{name}</title>
  <rect width="{width}" height="{height}" rx="10"
        fill="{THEME['card_bg']}" stroke="{THEME['border']}" stroke-width="1.5"/>
  <!-- 레포 이름 -->
  <text x="16" y="28" font-family="Arial,sans-serif" font-size="14"
        fill="{THEME['title']}" font-weight="bold">📁 {name}</text>
  <!-- 설명 -->
  <text x="16" y="50" font-family="Arial,sans-serif" font-size="11"
        fill="{THEME['text']}">{desc}</text>
  <!-- 구분선 -->
  <line x1="16" y1="62" x2="{width - 16}" y2="62"
        stroke="{THEME['border']}" stroke-width="1"/>
  <!-- 언어 색상 점 -->
  <circle cx="24" cy="80" r="6" fill="{lang_color}"/>
  <!-- 언어명 -->
  <text x="36" y="84" font-family="Arial,sans-serif" font-size="11"
        fill="{THEME['text']}">{lang}</text>
  <!-- 스타 아이콘 + 수 -->
  <text x="{width - 55}" y="84" font-family="Arial,sans-serif" font-size="11"
        fill="{THEME['star']}">★</text>
  <text x="{width - 44}" y="84" font-family="Arial,sans-serif" font-size="11"
        fill="{THEME['subtext']}">{stars}</text>
</svg>"""


def _empty_chart(message: str, width: int) -> str:
    """데이터 없을 때 빈 차트"""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="80">'
        f'<rect width="{width}" height="80" rx="10" fill="{THEME["card_bg"]}" '
        f'stroke="{THEME["border"]}" stroke-width="1.5"/>'
        f'<text x="{width // 2}" y="44" font-family="Arial,sans-serif" font-size="12" '
        f'fill="{THEME["subtext"]}" text-anchor="middle">{_escape(message)}</text>'
        f"</svg>"
    )