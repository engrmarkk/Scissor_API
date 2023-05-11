from ..extensions import db
import random
import string
import qrcode
from io import BytesIO
from PIL import Image
from datetime import datetime


def generate_current_date():
    current_date = f'{datetime.now().day}-{datetime.now().month}-{datetime.now().year}'
    return current_date


class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(5), unique=True, nullable=False)
    visit = db.Column(db.Integer, default=0)
    qr_code = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.String(20), default=generate_current_date())

    # Define your prefix here
    # PREFIX = "https://localhost:5000/"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.create_short_url()
        self.qr_code = self.generate_qr_code()

    def __repr__(self):
        return f'<Link {self.url}>'

    def save(self):
        # self.short_url=self.create_short_url()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def create_short_url(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(random.choices(characters, k=5))
        link = self.query.filter_by(short_url=short_url).first()
        if link:
            return self.create_short_url()
        return short_url

    def generate_qr_code(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.short_url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        buffer.seek(0)
        qr_code = buffer.getvalue()
        return qr_code
