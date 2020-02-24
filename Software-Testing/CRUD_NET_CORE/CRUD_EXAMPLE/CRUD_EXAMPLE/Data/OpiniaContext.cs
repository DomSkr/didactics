using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using CRUD_EXAMPLE.Models;

namespace CRUD_EXAMPLE.Data
{
    public class OpiniaContext: DbContext
    {
        public OpiniaContext(DbContextOptions<OpiniaContext> options)
            : base(options)
        {
        }

        public DbSet<Opinia> Opinia { get; set; }
    }
}
