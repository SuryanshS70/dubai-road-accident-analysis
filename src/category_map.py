"""Maps the Arabic Dubai Police incident category (acci_name, severity suffix removed)
to an English collision type. Rules are checked in order; the first match wins.
Categories mapped to None are not traffic collisions (breakdowns, parking,
congestion, hazards, violations, cancelled events) and are excluded."""
import re

# (regex on the Arabic base name, English group, is_collision)
RULES = [
    (r'تم الغاء', 'Cancelled event', False),
    (r'تعطل مركبة نتيجة حادث', 'Vehicle-vehicle collision', True),   # breakdown caused by a minor collision
    (r'تعطل|عطلانه', 'Vehicle breakdown', False),
    (r'دهس وهروب|صدم و ?هروب|الصدم والهروب', 'Hit and run', True),
    (r'دهس', 'Pedestrian run-over', True),
    # Names used from 2021 separate motorcycles (نارية) from bicycles (هوائية); the
    # 2018-2020 names ("حادث صدم دراجة") do not, so both go into one two-wheeler group.
    (r'دراجة|دراجتين', 'Two-wheeler (motorcycle/bicycle)', True),
    (r'تدهور', 'Rollover', True),
    (r'اصطدام بين', 'Vehicle-vehicle collision', True),
    (r'ضد مجهول', 'Collision with unknown party', True),
    (r'حيوان', 'Animal collision', None),             # resolved below: hitting an animal vs stray animals
    (r'حريق', 'Vehicle fire', True),
    (r'سقوط مركبة', 'Vehicle fall (pit/height/bridge)', True),
    (r'صدم (عمود|جدار|حاجز|حواجز|رصيف|شجرة|مبنى|علامة|إشارة|اشارة|لوحة|باب|جسر|جسم)|صدم جسر', 'Fixed-object collision', True),
    (r'صدم (مركبة|ترام|قطار|صهريج)', 'Special-vehicle collision', True),
    (r'تطاير|سقوط حمولة|انفصال مقطورة|سقوط (حاوية|رافعة)|سقوط شخص|إصابة راكب', 'Falling object / load / occupant', True),
    (r'حوادث مرورية اخرى', 'Other collision', True),
    (r'الوقوف خلف', 'Double parking', False),
    (r'مركبات مخالفة|بدون رخصة|دخول شاحنة|عكس اتجاه|التسابق|الاستعراضات', 'Traffic violation', False),
    (r'ازدحام', 'Congestion', False),
    (r'وجود|بقعة زيت|حفرة', 'Road hazard', False),
    (r'عبور شخص', 'Jaywalking', False),
    (r'طلب ثبات دورية|مسيرات|توقف مركبة|^مروري$', 'Other non-collision', False),
]

def map_category(base: str):
    """Return (group, is_collision). Unmatched or corrupted text -> ('Unreadable', False)."""
    for pat, group, coll in RULES:
        if re.search(pat, base):
            if group == 'Animal collision':
                return ('Animal collision', True) if 'صدم' in base else ('Road hazard', False)
            return group, coll
    return 'Unreadable', False
