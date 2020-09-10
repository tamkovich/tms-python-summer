"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id)
для продуктов. Создать пользовательский интерфейс.
"""


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///products.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    comment = Column(TEXT)

    def __init__(self, name: str,
                 price: float,
                 quantity: float,
                 comment: str):
        """
        Конструктор продукта
        :param name: название продукта
        :param price: цена продукта
        :param quantity: количество продукта в наличие
        :param comment: комментарий, описание.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.comment = comment

    def __repr__(self):
        return f'name: {self.name}, ' \
               f'price: {self.price}, ' \
               f'quantity: {self.quantity}, ' \
               f'comment: {self.comment}.'

    def add_product(self):
        session.add(Product(self.name, self.price, self.quantity, self.comment))
        return session.commit()

    @classmethod
    def update_name(cls, x: int, name: str):
        upd = session.query(Product).filter(Product.id == x).one()
        upd.name = name
        session.commit()

    @classmethod
    def update_price(cls, x: int, price: float):
        upd = session.query(Product).filter(Product.id == x).one()
        upd.price = price
        session.commit()

    @classmethod
    def update_quantity(cls, x: int, quantity: float):
        upd = session.query(Product).filter(Product.id == x).one()
        upd.quantity = quantity
        session.commit()

    @classmethod
    def update_comment(cls, x: int, comment: str):
        upd = session.query(Product).filter(Product.id == x).one()
        upd.comment = comment
        session.commit()

    @classmethod
    def delete_product(cls, prod_id: int):
        session.delete(session.query(Product).get(prod_id))
        session.commit()

    @classmethod
    def read_product(cls, name: str):
        """
        чтение строки конкретного продукта
        :param name: название продукта
        """
        print(session.query(Product).filter_by(name=name).all())


while True:
    print("for add input 'a', for upgrade input 'u', "
          "for delete input 'd', for read input 'r', "
          "for exit input 'e'.")
    choose = input('Enter your choose: ')
    if choose == 'a':
        print('Select a new product')
        product = Product(input("Enter a name new product: "),
                          int(input("Enter a price this product: ")),
                          int(input("Enter a quantity this product: ")),
                          input("Enter a comment about this product: "))
        product.add_product()
    if choose == 'u':
        print('Select id product, what need update')
        x = int(input('id: '))
        while True:
            print('Select, what lane are you want update:')
            print('Lines for input: '
                  'name - n, price - p, quantity - q, comment - c, e - exit')
            line = input('Select a line: ')
            if line == 'n':
                name = input('Select new name for this product: ')
                Product.update_name(x, name)
            elif line == 'p':
                price = float(input('Select new price for this product: '))
                Product.update_price(x, price)
            elif line == 'q':
                quantity = float(input('Select new quantity for this product: '))
                Product.update_quantity(x, quantity)
            elif line == 'c':
                comment = input('Select new comment for this product: ')
                Product.update_comment(x, comment)
            elif line == 'e':
                break
            else:
                print('Error! Input your select (n, p, q, c, e)')
                continue
    if choose == 'd':
        while True:
            print("for cancel delete Enter '00'")
            prod_id = int(input('Select id product for delete: '))
            Product.delete_product(prod_id)
    if choose == 'r':
        name = input("Enter a name product for watch: ")
        Product.read_product(name)
    if choose == 'e':
        break
    elif choose not in ['a', 'd', 'u', 'c', 'e']:
        print('Incorrect Input! Enter your choose (a,u,d,c,e)')
        continue
