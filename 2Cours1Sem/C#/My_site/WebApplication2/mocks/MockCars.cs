using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using WebApplication2.interfaces;
using WebApplication2.Models;

namespace WebApplication2.mocks
{
    public class MockCars : IAllCars
    {
        private readonly ICarsCategory _categoryCars = new MockCategory(); //вытаскиваем категорию автомобиля, чтобы присвоить при создании автомобиля. Только для чтения
        public IEnumerable<Car> Cars
        {
            get
            {
                return new List<Car>
                {
                    new Car{name="Tesla Model S",
                        shortDesc="Характер мерзкий",
                        longDesc="Быстрый дерзкий, как пуля резкий",
                        img="/img/tesla.jpg",
                        price=45000,
                        isFavourite=true,
                        available=true,
                        Category=_categoryCars.AllCategories.First()}, //первый элемент листа в MockCategory, электромобиль
                    new Car{name="Nissan Leaf",
                        shortDesc="Маленький чутка",
                        longDesc="Не знаю, что это за малыш",
                        img="/img/nisan.jpg",
                        price=12000,
                        isFavourite=true,
                        available=false,
                        Category=_categoryCars.AllCategories.First()},
                    new Car{name="Renault Fluence Z.E. ",
                        shortDesc="Летает чаще, чем ты ходишь",
                        longDesc="Едем в соседнее село на дискотеку",
                        img="/img/renault.jpg",
                        price=62000,
                        isFavourite=true,
                        available=true,
                        Category=_categoryCars.AllCategories.First()},
                    new Car{name="Kia Rio",
                        shortDesc="Вжум вжум",
                        longDesc="Поехали за картошкой",
                        img="/img/kia.jpg",
                        price=14000,
                        isFavourite=false,
                        available=true,
                        Category=_categoryCars.AllCategories.Last()},
                    new Car{name="BMW 1 Series",
                        shortDesc="Развалится при выезде за город",
                        longDesc="Красивый, удобный, ласковый, нежный",
                        img="/img/bmw.jpg",
                        price=45000,
                        isFavourite=false,
                        available=true,
                        Category=_categoryCars.AllCategories.Last()},
                    new Car{name="Mercedes benz",
                        shortDesc="Новый мерин",
                        longDesc="В*** города заработал деняг",
                        img="/img/mercedes.jpg",
                        price=34000,
                        isFavourite=true,
                        available=true,
                        Category=_categoryCars.AllCategories.Last()},
                };
            }
        }
        public IEnumerable<Car> getFavCars { get; set; }

        public Car getObjectCar(int carId)
        {
            throw new NotImplementedException();
        }
    }
}
