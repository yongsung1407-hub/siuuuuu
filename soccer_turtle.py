import turtle

W, H = 640, 740
screen = turtle.Screen()
screen.setup(W, H)
screen.title("Simplified Soccer Scene")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1)


def P(x, y):
    """이미지 좌표(좌상단 원점) -> 터틀 좌표(중앙 원점)"""
    return (x - W / 2, H / 2 - y)


def poly(points, fill, outline=None):
    t.penup()
    t.goto(*P(*points[0]))
    t.color(outline or fill, fill)
    t.pendown()
    t.begin_fill()
    for p in points[1:]:
        t.goto(*P(*p))
    t.goto(*P(*points[0]))
    t.end_fill()
    t.penup()


def rect(x1, y1, x2, y2, fill):
    poly([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], fill)


def circle(cx, cy, r, fill):
    t.penup()
    t.goto(*P(cx, cy + r))  # 원은 아래쪽에서 시작하므로 위치 보정
    t.goto(P(cx, cy)[0], P(cx, cy)[1] - r)
    t.color(fill, fill)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()


def text(x, y, s, size, color="black", weight="bold"):
    t.penup()
    t.goto(*P(x, y))
    t.color(color)
    t.write(s, align="center", font=("Arial", size, weight))


# ---------- 배경 ----------
rect(0, 0, 640, 150, "#d9d9d9")      # 관중석
rect(0, 150, 640, 410, "#33383d")    # 어두운 광고 벽
rect(0, 410, 640, 460, "#2f7fb5")    # 파란 광고판
rect(0, 460, 640, 740, "#3f9a3a")    # 잔디

# 광고판 글자 느낌
text(320, 448, "...   UN REGALO", 18, "white")

# 잔디 줄무늬
poly([(0, 560), (640, 545), (640, 552), (0, 567)], "#4aa844")

# ---------- 심판 ----------
circle(93, 288, 9, "#e0b090")
poly([(70, 300), (118, 300), (124, 360), (66, 360)], "#c0392b")
poly([(70, 360), (122, 360), (120, 415), (72, 415)], "#222222")
poly([(75, 415), (88, 415), (88, 480), (76, 480)], "#c0392b")
poly([(100, 415), (113, 415), (112, 480), (101, 480)], "#c0392b")

# ---------- 동료 선수 (줄무늬 유니폼) ----------
circle(205, 168, 17, "#d9a67e")
poly([(150, 215), (240, 205), (250, 375), (180, 385)], "white", "#999999")
for x in (165, 185, 205, 225):
    poly([(x, 215), (x + 8, 213), (x + 12, 380), (x + 4, 382)], "#222222")
poly([(175, 385), (250, 375), (240, 430), (175, 440)], "white", "#999999")
circle(152, 333, 12, "#222222")  # 장갑

# ---------- 주인공 선수 ----------
# 다리 (양말 + 맨살)
poly([(210, 470), (290, 485), (240, 525), (185, 525)], "#d9a67e")
poly([(185, 520), (238, 525), (190, 650), (135, 665)], "white", "#bbbbbb")
poly([(65, 705), (140, 680), (150, 695), (120, 715), (75, 715)], "#f2f2f2", "#888888")

poly([(380, 490), (455, 455), (470, 520), (440, 520)], "#d9a67e")
poly([(440, 520), (470, 515), (555, 665), (525, 670)], "white", "#bbbbbb")
poly([(525, 670), (575, 680), (585, 697), (530, 702)], "#f2f2f2", "#888888")

# 반바지
poly([(250, 335), (412, 320), (455, 455), (380, 490), (335, 430), (290, 485), (208, 470)],
     "white", "#bbbbbb")

# 팔
poly([(245, 190), (215, 195), (168, 345), (190, 352), (240, 260)], "white", "#bbbbbb")
poly([(405, 185), (440, 190), (520, 325), (505, 335), (415, 260)], "white", "#bbbbbb")
circle(150, 385, 13, "#d9a67e")
circle(535, 365, 13, "#d9a67e")

# 몸통(유니폼)
poly([(225, 110), (300, 92), (335, 92), (410, 110), (415, 190),
      (412, 330), (250, 340), (245, 200)], "white", "#bbbbbb")

# 머리 (뒷모습)
circle(313, 50, 30, "#3a3a3a")

# 유니폼 글자
text(325, 140, "RONALDO", 14, "black")
text(333, 255, "7", 64, "#222222")
text(335, 292, "Cygames", 9, "#333333", "normal")

screen.update()
turtle.done()
