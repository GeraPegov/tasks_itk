from datetime import datetime


class Meta(type):
    def __call__(cls, *args, **kwargs):
        exempl = super().__call__(*args, **kwargs)
        exempl.created_at = datetime.now()
        return exempl
