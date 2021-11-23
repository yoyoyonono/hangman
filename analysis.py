from pathlib import Path
games = [eval(x) for x in Path('out.txt').read_text().splitlines()]

hardest = sorted(games, key=lambda x: x[1] if len(x[0]) > 0 else 0, reverse=False)
print('\n'.join(str(x) for x in hardest[:10]))

print(sum(x[1] for x in games) / len(games))