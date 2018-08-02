class FiveCharEntry2(ttk.Entry):
    """An Entry that truncates to five characters on exit."""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(
                validate='focusout',
                validatecommand=(self.register(self._validate), '%P'),
                invalidatecommand=(self.register(self._on_invalid)))

    def _validate(self, proposed_value):
        return len(proposed_value) <= 5

    def _on_invalid(self):
        self.delete(5, tk.END)
