# main.py
from r_2_4 import Flower

def main():
    flower = Flower("Rose", 5, 2.99)
    print(f"Name: {flower.get_name()}, Petals: {flower.get_petals()}, Price: {flower.get_price()}")

    flower.set_name("Tulip")
    flower.set_petals(6)
    flower.set_price(3.99)
    print(f"Name: {flower.get_name()}, Petals: {flower.get_petals()}, Price: {flower.get_price()}")

if __name__ == "__main__":
    main()
