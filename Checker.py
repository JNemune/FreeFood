import re
from json import load
from os import path


def checker(inp, type_):
    match type_:
        case "FAN1":
            if (
                "فنی" in inp
                and "پایین" in inp
                and not (
                    "تعویض" in inp
                    or "معاوضه" in inp
                    or "میخوام" in inp
                    or "عوض" in inp
                    or "میخام" in inp
                    or "می\u200cخوام" in inp
                    or ("پایین" in inp and "بالا" in inp)
                    or "کوی" in inp
                    or "جابه جایی" in inp
                    or "جابجایی" in inp
                    or "جا به جایی" in inp
                    or len(inp) > 37
                )
            ):
                return True
        case "FAN2":
            if (
                "فنی" in inp
                and "بالا" in inp
                and not (
                    "تعویض" in inp
                    or "معاوضه" in inp
                    or "میخوام" in inp
                    or "عوض" in inp
                    or "میخام" in inp
                    or "می\u200cخوام" in inp
                    or ("پایین" in inp and "بالا" in inp)
                    or "کوی" in inp
                    or "جابه جایی" in inp
                    or "جابجایی" in inp
                    or "جا به جایی" in inp
                    or len(inp) > 37
                )
            ):
                return True
        case "MODR":
            if "کد" in inp and "دارم" in inp:
                return True
        case "MEHR":
            if len(inp) > 35:
                return False
            pattern = r"(سلام)*\s*(امروز)*\s*(نا*هار)*\s*(کد)*\s*(سلف)*\s*(مهر)\s*(.{2,12})*\s*((دارم)|(میخواد)|(میخاد))\s*\.*\?*؟*|(سلف مهر\.*\s*(اهدایی)*\.*)|(کد مهر\.*\s*(اهدایی)*)"
            prog = re.compile(pattern)
            res = prog.fullmatch(inp)
            return bool(res)
    return False


if __name__ == "__main__":
    test_case = "MEHR"

    tranc = {
        "بالا": "FAN2",
        "پایین": "FAN1",
        "علوم": "OLUM",
        "مهر": "MEHR",
        "هنر": "HONR",
        "زبان": "ZABN",
        "روانشناسی": "RAVN",
        "اجتماعی": "OLEJ",
        "مدیریت": "MODR",
        "استفاده": "ESTF",
        "الهیات": "ELHT",
        "علوم و فنون": "FONN",
        "فیزیک": "FIZK",
        "متفرقه": "ETC.",
        "تعویض": "CHNG",
    }
    with open(path.join(".", "resault.json"), "r", encoding="UTF-8") as f:
        resault = load(f)

    for i in tranc:
        count = int()
        for j in resault[i]:
            if checker(j, test_case):
                count += 1

        total = len(resault[i])
        print(
            tranc[i] + ":",
            round(count * 100 / total, 2),
            "%",
            "(" + str(count) + "/" + str(total) + ")",
        )
