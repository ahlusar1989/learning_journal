from wtforms import PasswordField
from wtforms import (
	Form,
	HiddenField,
	TextField,
	TextAreaField,
	validators,
	)

strip_filter = lambda x: x.strip() if x else None

# and a new form class
class LoginForm(Form):
    username = TextField(
        'Username', [validators.Length(min=1, max=255)]
    )
    password = PasswordField(
        'Password', [validators.Length(min=1, max=255)]
    )


class EntryCreateForm(Form):
	title = Textfield(
		'Entry Title',
		[validators.Length(min = 1, max = 225)],
		filters = [strip_filter])
	body = TextAreafield(
		'Entry Body',
		[validators.Length(min = 1, max = 225)],
		filters = [strip_filter])