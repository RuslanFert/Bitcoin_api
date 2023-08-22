from datetime import datetime
from pony.orm import *


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    tg_ID = Required(int, unique=True)
    nick = Optional(str)
    create_date = Required(datetime)
    walett = Required('Walett')
    sended_transactions = Set('Transaction', reverse='sender')
    received_transactions = Set('Transaction', reverse='reseiver')


class Walett(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Optional(User)
    balance = Required(float, default="0.0")
    private_key = Required(str, unique=True)
    addres = Required(str, unique=True)
    sended_transactions = Set('Transaction', reverse='sender_walett')
    received_transactions = Set('Transaction', reverse='receiver_walett')


class Transaction(db.Entity):
    id = PrimaryKey(int, auto=True)
    sender = Optional(User, reverse='sended_transactions')
    reseiver = Optional(User, reverse='received_transactions')
    sender_walett = Optional(Walett, reverse='sended_transactions')
    receiver_walett = Optional(Walett, reverse='received_transactions')
    sender_address = Optional(str)
    receiver_address = Optional(str)
    amount_btc_with_fee = Required(float)
    amount_btc_withouy_fee = Required(float)
    fee = Required(float)
    date_of_transaction = Required(datetime, default=datetime.now())
    tx_hash = Required(str, unique=True)
