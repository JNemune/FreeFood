import re
from json import load
from os import path


def checker(inp, type_):
    if inp is None:
        return False
    if (
        "تعویض" in inp
        or "معاوضه" in inp
        or "میخوام" in inp
        or "درخواستی" in inp
        or "درخواست" in inp
        or "عوض" in inp
        or "میخام" in inp
        or "می\u200cخوام" in inp
        or ("پایین" in inp and "بالا" in inp)
        or "کوی" in inp
        or "جابه جایی" in inp
        or "جابجایی" in inp
        or "جا به جایی" in inp
        or "هزینه" in inp
        or "خرید" in inp
        or "خرم" in inp
        or "?" in inp
        or "؟" in inp
        or "کسی" in inp
        or "نداره" in inp
        or "داره" in inp
        or "برای" in inp
        or "فروش" in inp
        or "تمن" in inp
        or "تومن" in inp
        or "تومان" in inp
        or len(inp) > 37
    ):
        return False
    match type_:
        case "FAN1":
            if "فنی" in inp and "پایین" in inp:
                return True
        case "FAN2":
            if "فنی" in inp and "بالا" in inp:
                return True
        case "MODR":
            if "کد" in inp and "دارم" in inp:
                return True
        case "MEHR":
            if "مهر" in inp and "دارم" in inp:
                return True
        case "OLUM":
            if (
                "علوم " in inp
                # and "دارم" in inp
                and not (
                    "فنون" in inp or "اج" in inp or "انسان" in inp or "معلوم" in inp
                )
            ):
                return True
        case "HONR":
            if "هنر" in inp:
                return True
    return False


if __name__ == "__main__":
    test_case = "HONR"

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
                # if tranc[i] != test_case:
                #     breakpoint()
                #     print(j)
            # elif tranc[i] == test_case:
            #     breakpoint()
            #     print(j)

        total = len(resault[i])
        print(
            tranc[i] + ":",
            round(count * 100 / total, 2),
            "%",
            "(" + str(count) + "/" + str(total) + ")",
        )
