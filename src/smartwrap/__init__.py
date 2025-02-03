import textwrap


class SmartWrapper(textwrap.TextWrapper):
    def __init__(self, *args, **kwargs):
        if "balanced" in kwargs:
            balanced = kwargs["balanced"]
            del kwargs["balanced"]
        else:
            balanced = False

        super().__init__(*args, **kwargs)

        self.balanced = balanced

    def wrap(self, text) -> list:
        """Override the parent method."""

        wrapped_text = super().wrap(text)

        if self.balanced:
            original_width = self.width  # Remember the input width, to reset it later
            n_lines = len(wrapped_text)

            while self.width > 0:

                self.width -= 1
                rewrapped_text = super().wrap(text)

                # If number of lines in rewrapped text is greater than in originally wrapped text,
                # return the wrapped text from the previous iteration.
                if len(rewrapped_text) > n_lines:
                    # Reset self.width to the original width
                    self.width = original_width
                    break
                else:
                    wrapped_text = rewrapped_text

        return wrapped_text


# Redefine convenience functions with SmartWrapper


def wrap(text, width=70, **kwargs):
    w = SmartWrapper(width=width, **kwargs)
    return w.wrap(text)


def fill(text, width=70, **kwargs):
    w = SmartWrapper(width=width, **kwargs)
    return w.fill(text)


def shorten(text, width, **kwargs):
    w = SmartWrapper(width=width, max_lines=1, **kwargs)
    return w.fill(" ".join(text.strip().split()))
