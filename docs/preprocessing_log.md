# Preprocessing log

| Step | Rows removed | Rows remaining |
|---|---:|---:|
| 1. Loaded raw file | 0 | 757,305 |
| 2a. Dropped exact duplicate rows | 869 | 756,436 |
| 2b. Kept latest record per acci_id | 3,259 | 753,177 |
| 4. Kept traffic collisions only | 309,443 | 443,734 |
| 5. Dropped missing, zero or out-of-Dubai coordinates | 1,011 | 442,723 |
| 6. Dropped unparseable or future timestamps | 33 | 442,690 |

Coordinates swapped and fixed: 35,540

## Non-collision records excluded in step 4

| Category | Rows |
|---|---:|
| Vehicle breakdown | 172,160 |
| Double parking | 60,796 |
| Traffic violation | 32,662 |
| Road hazard | 27,435 |
| Congestion | 9,208 |
| Other non-collision | 5,419 |
| Jaywalking | 1,527 |
| Cancelled event | 206 |
| Unreadable | 30 |

## Collision types kept

| Type | Rows | % Serious |
|---|---:|---:|
| Fixed-object collision | 206,128 | 1.8 |
| Vehicle-vehicle collision | 99,241 | 18.7 |
| Two-wheeler (motorcycle/bicycle) | 52,438 | 46.8 |
| Hit and run | 34,498 | 2.4 |
| Collision with unknown party | 16,003 | 0.0 |
| Pedestrian run-over | 12,259 | 49.5 |
| Rollover | 8,473 | 30.4 |
| Falling object / load / occupant | 7,859 | 1.4 |
| Vehicle fire | 3,177 | 37.7 |
| Animal collision | 1,409 | 3.1 |
| Vehicle fall (pit/height/bridge) | 755 | 5.6 |
| Special-vehicle collision | 431 | 6.0 |
| Other collision | 19 | <NA> |

## Severity

| Class | Rows |
|---|---:|
| Minor | 378,739 |
| Serious | 57,163 |
| nan | 6,788 |

## Months flagged as incomplete

2018-10, 2021-03, 2023-01, 2025-10, 2026-04, 2026-10

Date range: 2018-08-13 08:17:21 to 2026-10-07 10:51:10
