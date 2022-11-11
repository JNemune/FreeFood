from functools import partial
from json import dump, load
from tkinter import *
from tkinter import messagebox


class TkApp(object):
    def __init__(self) -> None:
        self.out = {
            "بالا": [],
            "پایین": [],
            "علوم": [],
            "مهر": [],
            "هنر": [],
            "زبان": [],
            "روانشناسی": [],
            "اجتماعی": [],
            "مدیریت": [],
            "استفاده": [],
            "الهیات": [],
            "علوم و فنون": [],
            "فیزیک": [],
            "متفرقه": [],
            "تعویض": [],
        }
        with open("sample.json", "r", encoding="utf-8") as f:
            self.inp = load(f)

        root = Tk()
        self.text = StringVar(root)
        self.import_text()

        root.geometry("700x300")
        Label(root, textvariable=self.text).pack(padx=20, pady=20)
        button_frame = Frame(root)
        button_frame.pack()
        for i_, i in enumerate(
            [
                "بالا",
                "پایین",
                "متفرقه",
                "استفاده",
                "تعویض",
                "علوم",
                "مهر",
                "هنر",
                "زبان",
                "روانشناسی",
                "اجتماعی",
                "مدیریت",
                "الهیات",
                "علوم و فنون",
                "فیزیک",
            ]
        ):
            Button(
                button_frame,
                text=i,
                font=20,
                width=15,
                background=["#ADD8E6", "#FFD580", "#90EE90"][i_ % 3],
                command=partial(self.asw_set, i),
            ).grid(row=i_ // 4, column=i_ % 4, padx=10, pady=10)

        root.mainloop()
        self.save()

    def import_text(self):
        self.text.set(self.inp.pop())

    def asw_set(self, i):
        self.out[i].append(self.text.get())
        self.import_text()

    def save(self):
        with open("resault.json", "r", encoding="utf-8") as f:
            tmp = load(f)
        for i in tmp:
            tmp[i] += self.out[i]
        with open("resault.json", "w", encoding="utf-8") as f:
            dump(tmp, f, ensure_ascii=False)
        with open("sample.json", "w", encoding="utf-8") as f:
            dump(self.inp + [self.text.get()], f, ensure_ascii=False)
        messagebox.showinfo("Remaining ...", str(len(self.inp) + 1))


if __name__ == "__main__":
    TkApp()
