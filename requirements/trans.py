if __name__ == "__main__":
    from openccc.opencc import OpenCC
else:

    from requirements.openccc.opencc import OpenCC
import tkinter


def convert_text(text, conversion_type):
    return OpenCC(conversion_type).convert(text)


def main():
    global do_conversion, trans_buttons, input_text, output_text, window
    conversion_types = [
        "hk2s",
        "s2hk",
        "s2t",
        "s2tw",
        "s2twp",
        "t2hk",
        "t2s",
        "t2tw",
        "tw2s",
        "tw2sp",
    ]
    window = tkinter.Tk()
    input_text = tkinter.Text(window, height=50, width=70, font=("Dengxian", 10))
    input_text.pack(side="left")
    output_text = tkinter.Text(window, height=50, width=70, font=("Dengxian", 10))
    output_text.pack(side="right")
    output_text.config(state="disabled")
    trans_buttons = []

    def do_conversion(conversion_type):
        output_text.config(state="normal")
        output_text.delete("0.0", "end")
        output_text.insert(tkinter.INSERT, convert_text(input_text.get("0.0", "end")[:-1], conversion_type))
        output_text.config(state="disabled")

    for conv_type in conversion_types:
        trans_buttons.append(tkinter.Button(window, text=conv_type, command=lambda type=conv_type: do_conversion(type)))
    for btn in trans_buttons:
        btn.pack()
    if __name__ == "__main__":
        window.mainloop()


if __name__ == "__main__":
    main()
