# task_15_1
"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id)
для продуктов. Создать пользовательский интерфейс.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

e = create_engine("sqlite:///products.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=e)
session = Session()


def menu() -> None:
    print(
        """
1. Add new product
2. Read table
3. Update some data of product by id
4. Delete product's data by id
0. Exit
"""
    )


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    comment = Column(Integer)

    def __init__(self, name: str, quantity: int, comment: str):
        self.name = name
        self.quantity = quantity
        self.comment = comment

    def new_product(self):
        session.add(Products(self.name, self.quantity, self.comment))

    @classmethod
    def read_table(cls) -> str:
        result = e.execute(
            f"""
            select * from {Products.__tablename__}
        """
        )
        return result

    @staticmethod
    def update(atr: str, tmp: str or int, item_id: int):
        e.execute(
            f"""
            update {Products.__tablename__} set {atr} = {tmp} where {Products.id} = {item_id}
        """
        )

    @staticmethod
    def delete_product(item_id: int):
        e.execute(
            f"""
            delete from {Products.__tablename__} where id = {item_id}
        """
        )


Base.metadata.create_all(e)

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose: ")

        try:
            choice = int(choice)
        except ValueError:
            print("not a number")
            break

        if choice == 1:
            name_product = input("Enter name product: ")
            numbers = input("Enter quantity of product: ")
            comments = input("Enter some comments: ")

            try:
                numbers = int(numbers)
            except ValueError:
                print("error")

            product = Products(name_product, numbers, comments)
            product.new_product()
            session.commit()

        if choice == 2:
            table = Products.read_table()
            for _ in table:
                print(_)

        if choice == 3:
            product_id = input("Enter product id: ")
            new_value = input("Enter new value: ")

            try:
                product_id = int(product_id)
                new_value = int(new_value)
            except ValueError:
                print("error")

            Products.update("quantity", new_value, product_id)
            session.commit()

        if choice == 4:
            product_id = input("Enter product id: ")

            try:
                product_id = int(product_id)
            except ValueError:
                print("error")

            Products.delete_product(product_id)
            session.commit()

        if choice == 0:
            exit()
