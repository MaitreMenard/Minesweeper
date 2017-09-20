import tkinter as tk


class Smiley:
    """
    Note: The face doesn't change to the O-face when the user press a tile button, because Tkinter's buttons only
    support onButtonDown events. The O-face should be displayed when a button is down and the logic of tile revealing
    should happen when the button is released.
    """
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.smiley_face = tk.PhotoImage(file="resources/smiley.gif").subsample(2, 2)
        self.sunglasses_face = tk.PhotoImage(file="resources/sunglasses.gif").subsample(2, 2)
        self.dead_face = tk.PhotoImage(file="resources/dead.gif").subsample(2, 2)

        self.frame = tk.Frame(self.parent)
        self.frame.grid(row=0, column=3)
        self.button = None
        self.set_smiley_face()

    def _create_button_with_image(self, image):
        if self.button is not None:
            self.button.destroy()
        self.button = tk.Button(self.frame, image=image, command=self.callback, height=32, width=32)
        self.button.grid(padx=22)

    def set_smiley_face(self):
        self._create_button_with_image(self.smiley_face)

    def set_sunglasses_face(self):
        self._create_button_with_image(self.sunglasses_face)

    def set_dead_face(self):
        self._create_button_with_image(self.dead_face)
