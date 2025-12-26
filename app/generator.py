from typing import List, Tuple
from app.models import GenerateRequest, Block

def _split_yards(level: str, total: int) -> Tuple[int, int, int]:
    # warmup, main, cooldown ratios by level
    if level == "beginner":
        warm = round(total * 0.30)
        main = round(total * 0.50)
    elif level == "intermediate":
        warm = round(total * 0.25)
        main = round(total * 0.60)
    else:  # advanced
        warm = round(total * 0.20)
        main = round(total * 0.65)
    cool = total - warm - main
    return warm, main, cool

def _build_warmup(req: GenerateRequest, target: int) -> Block:
    details: List[str] = []
    yards = 0

    # simple Swim/Kick/Pull pattern like your examples
    unit = 100 if req.level == "beginner" else 200
    pattern = [f"{unit} swim easy", f"{unit} kick easy", f"{unit} pull easy"]

    i = 0
    while yards + unit <= target and i < 50:
        details.append(pattern[i % 3])
        yards += unit
        i += 1

    # adjust if we undershoot a lot (optional)
    if yards < target and target - yards >= 50:
        details.append("50 easy choice")
        yards += 50

    return Block(type="warmup", yards=yards, details=details)

def _build_main(req: GenerateRequest, target: int) -> Block:
    details: List[str] = []
    yards = 0

    if req.focus == "technique":
        # more drills, not sprinting
        if req.level == "beginner":
            set_line = "6 x 100 freestyle (technique focus) @ easy/moderate, :20 rest"
            set_yards = 600
        elif req.level == "intermediate":
            set_line = "5 x 200 freestyle @ challenging interval (hold form), :20 rest"
            set_yards = 1000
            details.append("200 freestyle + zipper drill focus")
            yards += 200
        else:
            set_line = "10 x 100 swim (form first) @ challenging interval"
            set_yards = 1000

        if yards + set_yards <= target:
            details.append(set_line)
            yards += set_yards

        # fill remainder with drill-ish 50s
        while yards + 200 <= target:
            details.append("4 x 50 drill/swim by 25 @ :20 rest")
            yards += 200

    elif req.focus == "speed":
        # sprints + more rest
        if req.level == "beginner":
            chunk = ("8 x 25 fast (good form) @ :30 rest", 200)
        elif req.level == "intermediate":
            chunk = ("12 x 50 race-pace @ :30–:45 rest", 600)
        else:
            chunk = ("16 x 50 sprint @ :30–:60 rest", 800)

        while yards + chunk[1] <= target:
            details.append(chunk[0])
            yards += chunk[1]

        # optional kick speed component if room
        if yards + 200 <= target:
            details.append("4 x 50 kick fast @ :30 rest")
            yards += 200

    else:  # endurance
        # longer repeats
        if req.level == "beginner":
            chunk = ("4 x 100 steady aerobic @ :20 rest", 400)
        elif req.level == "intermediate":
            chunk = ("4 x 200 steady aerobic @ :20 rest", 800)
        else:
            chunk = ("3 x 400 steady aerobic (strong breathing) @ :30 rest", 1200)

        while yards + chunk[1] <= target:
            details.append(chunk[0])
            yards += chunk[1]

        if yards + 200 <= target:
            details.append("4 x 50 easy/moderate build @ :15 rest")
            yards += 200

    return Block(type="main", yards=yards, details=details)

def _build_cooldown(req: GenerateRequest, target: int) -> Block:
    details: List[str] = []
    yards = 0

    # simple easy swimming to fill target
    while yards + 200 <= target:
        details.append("200 easy choice")
        yards += 200
    if yards + 100 <= target:
        details.append("100 easy choice")
        yards += 100
    if yards + 50 <= target:
        details.append("50 easy choice")
        yards += 50

    return Block(type="cooldown", yards=yards, details=details)

def generate_workout(req: GenerateRequest) -> List[Block]:
    warm_t, main_t, cool_t = _split_yards(req.level, req.total_yards)
    warm = _build_warmup(req, warm_t)
    main = _build_main(req, main_t)
    cool = _build_cooldown(req, cool_t)

    # NOTE: total yards may not match exactly at v1; that’s fine for now.
    return [warm, main, cool]
