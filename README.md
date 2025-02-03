`smartwrap` is an extension of the standard library [`textwrap`](https://docs.python.org/3/library/textwrap.html) which enables balanced text wrapping. 

Wrapped text is balanced when the number of characters across all rows is minimized, while keeping the number of rows identical to that of unbalanced wrapping. Note that this is numerical balancing – not optical balancing, which takes more factors into consideration such as kerning and letter size.

## Usage

### Example

```python
UDHR = """All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood."""

$ textwrap.wrap(UDHR)
['All human beings are born free and equal in dignity and rights. They',
 'are endowed with reason and conscience and should act towards one',
 'another in a spirit of brotherhood.']

$ smartwrap.wrap(UDHR, balanced=True)
['All human beings are born free and equal in dignity and',
 'rights. They are endowed with reason and conscience and',
 'should act towards one another in a spirit of brotherhood.']
```

### Hint

`smartwrap` is most useful when wrapping short pieces of text which could flow into multiple rows depending on the container size. To prevent awkward splitting of the text into one long row and one short row, `smartwrap` balances the number of letters between the rows. Some cases include labels on legends and buttons, quoted statements, etc.

```py
# Example: a pie chart has a label 'Social and cultural rights'; labels cannot be longer than 20 characters.

$ textwrap.wrap("Social and cultural rights", width=20)
['Social and cultural', 'rights']

$ smartwrap.wrap("Social and cultural rights", balanced=True, width=20)
['Social and', 'cultural rights']
```

Note that `smartwrap` can be used like `textwrap`. It returns the same outputs when `balanced` flag is set to False. Also it accepts the same arguments and has the same methods.

```python
$ smartwrap.wrap(UDHR) # no difference to `textwrap`
['All human beings are born free and equal in dignity and rights. They',
 'are endowed with reason and conscience and should act towards one',
 'another in a spirit of brotherhood.']

$ smartwrap.wrap(UDHR, balanced=True, width=50) # width arg and other args available
['All human beings are born free and equal in',
 'dignity and rights. They are endowed with',
 'reason and conscience and should act towards',
 'one another in a spirit of brotherhood.']

$ smartwrap.fill(UDHR, balanced=True, width=50) # .fill() and other methods available
'All human beings are born free and equal in\ndignity and rights. They are endowed with\nreason and conscience and should act towards\none another in a spirit of brotherhood.'
```
