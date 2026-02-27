from app.core.constants import THEME


def _escape(text: str) -> str:
    """SVG용 특수문자 이스케이프"""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
    )


def make_stat_badge(label: str, value: str | int, width: int = 160) -> str:
    """
    통계 배지 생성
    예: [Followers] [42]
    """
    label = _escape(str(label))
    value = _escape(str(value))
    
    label_w = width * 62 // 100     # 라벨 영역  62%
    value_w = width - label_w       # 값 영역 38%
    height = 28
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" role="img">
    <title>{label}: {value}</title>
    <rect width="{width}" height="{height}" rx="6" fill="{THEME['border']}"/>
    <rect width="{label_w}" height="{height}" rx="6" fill="{THEME['accent']}"/>
    <rect x="{label_w - 4}" width="8" height="{height}" fill="{THEME['accent']}"/>
    <rect x="{label_w}" width="{value_w}" height="{height}" rx="0" fill="{THEME['card_bg']}"/>
    <rect x="{width - 6}" width="6" height="{height}" rx="0" fill="{THEME['card_bg']}"/>
    <rect x="{width - 6}" width="6" height="{height}" rx="6" fill="{THEME['border']}"/>
    <text x="{label_w // 2}" y="18" font-family="Arial,sans-serif" font-size="11"
        fill="#ffffff" text-anchor="middle" font-weight="bold">{label}</text>
    <text x="{label_w + value_w // 2}" y="18" font-family="Arial,sans-serif" font-size="11"
        fill="{THEME['title']}" text-anchor="middle" font-weight="bold">{value}</text>
    </svg>"""


def make_label_badge(text: str, color: str | None = None, width: int = 120) -> str:
    """
    단색 라벨 배지 생성
    예: [Python]
    """
    text = _escape(str(text))
    bg = color or THEME["accent"]
    height = 24
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" role="img">
    <title>{text}</title>
    <rect width="{width}" height="{height}" rx="12" fill="{bg}" opacity="0.15"/>
    <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="11"
            fill="none" stroke="{bg}" stroke-width="1.2"/>
    <text x="{width // 2}" y="16" font-family="Arial,sans-serif" font-size="11"
            fill="{bg}" text-anchor="middle" font-weight="bold">{text}</text>
    </svg>"""


def make_profile_badge(
    name: str,
    username: str,
    followers: int,
    following: int,
    public_repos: int,
    width: int = 340,
) -> str:
    """
    프로필 요약 배지 (이름, 유저명, 팔로워/팔로잉/레포 수)
    """
    name = _escape(name)
    username = _escape(username)
    height = 90
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" role="img">
    <title>{name} (@{username})</title>
    <!-- 배경 -->
    <rect width="{width}" height="{height}" rx="10"
            fill="{THEME['card_bg']}" stroke="{THEME['border']}" stroke-width="1.5"/>
    <!-- 상단 강조 바 -->
    <rect width="{width}" height="5" rx="10" fill="{THEME['accent']}"/>
    <rect y="5" width="{width}" height="5" fill="{THEME['accent']}"/>
    <!-- 이름 -->
    <text x="18" y="32" font-family="Arial,sans-serif" font-size="15"
            fill="{THEME['title']}" font-weight="bold">{name}</text>
    <!-- 유저명 -->
    <text x="18" y="50" font-family="Arial,sans-serif" font-size="11"
            fill="{THEME['subtext']}">@{username}</text>
    <!-- 구분선 -->
    <line x1="18" y1="58" x2="{width - 18}" y2="58"
            stroke="{THEME['border']}" stroke-width="1"/>
    <!-- 통계: Followers -->
    <text x="{width // 6}" y="74" font-family="Arial,sans-serif" font-size="11"
            fill="{THEME['subtext']}" text-anchor="middle">Followers</text>
    <text x="{width // 6}" y="86" font-family="Arial,sans-serif" font-size="12"
            fill="{THEME['title']}" text-anchor="middle" font-weight="bold">{followers}</text>
    <!-- 통계: Following -->
    <text x="{width // 2}" y="74" font-family="Arial,sans-serif" font-size="11"
            fill="{THEME['subtext']}" text-anchor="middle">Following</text>
    <text x="{width // 2}" y="86" font-family="Arial,sans-serif" font-size="12"
            fill="{THEME['title']}" text-anchor="middle" font-weight="bold">{following}</text>
    <!-- 통계: Repos -->
    <text x="{width * 5 // 6}" y="74" font-family="Arial,sans-serif" font-size="11"
            fill="{THEME['subtext']}" text-anchor="middle">Public Repos</text>
    <text x="{width * 5 // 6}" y="86" font-family="Arial,sans-serif" font-size="12"
            fill="{THEME['title']}" text-anchor="middle" font-weight="bold">{public_repos}</text>
    </svg>"""