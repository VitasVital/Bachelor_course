using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using WebApplication2.interfaces;
using WebApplication2.Models;

namespace WebApplication2.mocks
{
    public class MockCategory : ICarsCategory
    {
        public IEnumerable<Category> AllCategories //вернули все категории
        {
            get
            {
                return new List<Category> //создали и вернули категории
                {
                    new Category{categoryName="Электромобили",desc="Современный вид транспорта"},
                    new Category{categoryName="Классические автомобили",desc="Автомобили с двигателями внутреннего сгорания"}
                };
            }
        }
    }
}
