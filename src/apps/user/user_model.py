from datetime import timezone
from uuid import uuid4

from flask import current_app
from sqlalchemy.ext.hybrid import hybrid_property

from src.commons.constants.constant import ROLES, UUID_V4_LENGTH
from src.commons.extensions import bcrypt, db
from src.commons.utils.datetime_utils import (get_local_utcoffset,
                                              localized_dt_string,
                                              make_tzaware, utc_now)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(UUID_V4_LENGTH), primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    first_name = db.Column(db.String(120), nullable=False, )
    last_name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default=ROLES.PHOTOGRAPHER)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, default=utc_now)
    updated_at = db.Column(db.DateTime, default=utc_now)

    def __repr__(self):
        return f"<Account email={self.email}, role={self.role}>"

    @hybrid_property
    def created_at_str(self):
        created_at_utc = make_tzaware(
            self.created_at, use_tz=timezone.utc, localize=False
        )
        return localized_dt_string(created_at_utc, use_tz=get_local_utcoffset())

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        log_rounds = current_app.config.get("BCRYPT_LOG_ROUNDS")
        hash_bytes = bcrypt.generate_password_hash(password, log_rounds)
        self.password = hash_bytes.decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
