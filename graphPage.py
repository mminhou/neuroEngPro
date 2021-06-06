from module import *

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.graphWall = tk.PhotoImage(file='factory/image/result.png')

        # Wallpaper
        self.canvas = tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack(fill="both", expand=True)

        # Graph Title
        self.canvas.create_text(350, 100, text="Total Record", font=("Helvetica", 70, 'bold'))

        # Graph Image
        self.image = self.canvas.create_image(740, 500, image=self.graphWall)

        # Previous Button
        self.backBtn = tk.PhotoImage(file='factory/image/exitButton.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(1375, 60, window=backButton)

        # Update Button
        self.updateBtn = tk.PhotoImage(file='factory/image/exitButton.png')
        updateButton = tk.Button(self, text='update', font=("Helvetica", 70, 'bold'),
                               borderwidth=0, highlightthickness=0,
                               command=lambda: self.change_photo())
        self.canvas.create_window(750, 100, window=updateButton)

    def change_photo(self):
        filename = "factory/image/result.png"
        imageFile = Image.open(filename)
        self.photo = ImageTk.PhotoImage(imageFile)
        self.canvas.itemconfig(self.image, image=self.photo)