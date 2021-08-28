import sys, threading, tkinter as tk, time, queue

import self as self

import Main

msg=''
class Gui(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def exitClick(self, event):
        exit(0)

    def sendMessageClick(self, event, textField):
       # print(textField.get())
        msg=textField.get()
        if msg!='':
            intent = Main.interpreter.parse(msg)["intent"]
            Main.send_message(msg, intent["name"])
            textField.delete(0, "end")  # clears textField
            root = tk.Tk()
            root.title("Laucer's chat")
            root.minsize(600, 400)
            root.bind(
                "<Return>",
                lambda event: self.sendMessageClick(event, textField))  # enter
            mainFrame = tk.Frame(root)
            chat = tk.Text(mainFrame)
            chat.insert('end', 'YOU: ' + msg + '\n\n')
            res = Main.respond(msg, intent["name"])
            chat.insert('end', 'BOT: ' + res + '\n\n')


root = tk.Tk()
root.title("Laucer's chat")
root.minsize(600, 400)
root.bind(
            "<Return>",
            lambda event: self.sendMessageClick(event, textField))  # enter

mainFrame = tk.Frame(root)
mainFrame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

        # ChatField
chat = tk.Text(mainFrame)

chat.configure(state="disabled")  # nie mozna po tym pisac
chat.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E)

        # TextFieldToSend
textField = tk.Entry(mainFrame)
textField.grid(column=0, row=1, sticky=tk.N + tk.S + tk.W + tk.E)

        # SendMessageButton
buttonSend = tk.Button(mainFrame)
buttonSend["text"] = "Send!"
buttonSend.grid(column=0, row=2, sticky=tk.N + tk.S + tk.W + tk.E)
buttonSend.bind("<Button-1>",
                lambda event: self.sendMessageClick(event, textField))

'''#usersPanel
		usersPanel = tk.Listbox(mainFrame)
		usersPanel.insert(1, "ALL")
		usersPanel.grid(column=2, row=0, sticky=tk.N + tk.S + tk.W + tk.E)

		#ExitButton
		buttonExit = tk.Button(mainFrame)
		buttonExit["text"] = "Exit"
		buttonExit["background"] = "gray"
		buttonExit.grid(column=2, row=2, sticky=tk.N + tk.S + tk.W + tk.E)
		buttonExit.bind("<Button-1>", self.exitClick)'''

root.mainloop()


GuiThread = Gui()
GuiThread.start()
