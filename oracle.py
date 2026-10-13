import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

EAR = 15
CORBEL_SPAN = 60

def mantel_plan(openingCm):
    if not (openingCm > 0):
        return {"error": "the opening must be positive"}
    shelf = round1(openingCm + 2 * EAR)
    if openingCm < 90: verdict = "a petite fireplace"
    elif openingCm <= 130: verdict = "a standard fireplace"
    else: verdict = "a grand fireplace"
    return {"shelf": shelf, "verdict": verdict}

def corbel_plan(shelfCm):
    if not (shelfCm > 0):
        return {"error": "the shelf must be positive"}
    corbels = max(2, math.ceil(shelfCm / CORBEL_SPAN))
    spacing = round1(shelfCm / (corbels - 1))
    if corbels == 2: verdict = "a pair of corbels"
    else: verdict = "a row of corbels"
    return {"corbels": corbels, "spacing": spacing, "verdict": verdict}

def leg_plan(bottomCm, shelfThickCm):
    if not (bottomCm > 0) or not (shelfThickCm > 0):
        return {"error": "the shelf bottom and the shelf thickness must be positive"}
    if shelfThickCm >= bottomCm:
        return {"error": "the shelf is thicker than its height"}
    leg = round1(bottomCm - shelfThickCm)
    if leg < 90: verdict = "a low mantel"
    elif leg <= 120: verdict = "a classic mantel"
    else: verdict = "a tall mantel"
    return {"leg": leg, "verdict": verdict}

def render_mantel(r, openingCm):
    return ("An opening " + fmt(openingCm) + " cm wide takes a labeled " + fmt(r["shelf"])
            + " cm shelf with " + fmt(EAR) + " cm ears - " + r["verdict"] + ".")

def render_corbel(r, shelfCm):
    return ("A shelf " + fmt(shelfCm) + " cm takes " + plural(r["corbels"], "corbel")
            + " at " + fmt(r["spacing"]) + " cm centers - " + r["verdict"] + ".")

def render_leg(r, bottomCm, shelfThickCm):
    return ("A shelf bottom at " + fmt(bottomCm) + " cm with a labeled " + fmt(shelfThickCm)
            + " cm shelf takes legs " + fmt(r["leg"]) + " cm tall - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[100],[70],[0],[90],[131],[130],[150],[85.5],[200],[120]]:
    add("mantelPlan", mantel_plan, render_mantel, a)
for a in [[130],[240],[0],[60],[59],[120],[121],[180],[100],[95.5]]:
    add("corbelPlan", corbel_plan, render_corbel, a)
for a in [[120,10],[60,10],[10,10],[0,10],[120,0],[150,12],[100,10],[90,8],[130,10],[115.5,10]]:
    add("legPlan", leg_plan, render_leg, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
