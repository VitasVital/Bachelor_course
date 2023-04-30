using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using WebApplication2.Models;

namespace WebApplication2.interfaces
{
    public interface ICarsCategory
    {
        IEnumerable<Category> AllCategories { get; } //получает данные
    }
}
